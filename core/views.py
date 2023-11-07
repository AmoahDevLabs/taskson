from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .forms import PersonForm, DateForm
from .models import Person


class CRUDView(TemplateView):
    template_name = 'person/person.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persons'] = Person.objects.all()
        context['form'] = PersonForm()
        context['date_form'] = DateForm()

        return context


class PersonBaseView(View):
    def handle_form(self, request, form, date_form, person_id=None):
        if form.is_valid() and date_form.is_valid():
            if person_id:
                try:
                    person = Person.objects.get(pk=person_id)
                    person.name = form.cleaned_data['name']
                    person.address = form.cleaned_data['address']
                    person.age = form.cleaned_data['age']
                    person.date = date_form.cleaned_data['date']
                    person.save()
                    person_data = {
                        'id': person.id,
                        'name': person.name,
                        'address': person.address,
                        'age': person.age,
                        'date': person.date.strftime('%Y-%m-%d')
                    }
                    return JsonResponse({'status': 'success', 'person': person_data})
                except Person.DoesNotExist:
                    return JsonResponse({'status': 'error', 'message': 'Person not found or already deleted.'},
                                        status=404)
            else:
                person = form.save(commit=False)
                person.date = date_form.cleaned_data['date']
                person.save()
                person_data = {
                    'id': person.id,
                    'name': person.name,
                    'address': person.address,
                    'age': person.age,
                    'date': person.date.strftime('%Y-%m-%d')
                }
                return JsonResponse({'status': 'success', 'person': person_data})
        else:
            errors = form.errors
            return JsonResponse({'status': 'error', 'errors': errors}, status=400)


class PersonCreateView(PersonBaseView):
    def post(self, request):
        date_form = DateForm(request.POST)
        form = PersonForm(request.POST)
        return self.handle_form(request, form, date_form)


class PersonUpdateView(PersonBaseView):
    def post(self, request, person_id):
        date_form = DateForm(request.POST)
        form = PersonForm(request.POST)
        return self.handle_form(request, form, date_form, person_id)


class PersonDeleteView(View):
    def post(self, request):
        person_id = request.POST.get('person_id')
        try:
            person = Person.objects.get(pk=person_id)
            person.delete()
            response = {
                'status': 'success',
                'message': 'Person deleted successfully.',
            }
        except Person.DoesNotExist:
            response = {
                'status': 'error',
                'message': 'Person not found or already deleted.',
            }
        return JsonResponse(response)
