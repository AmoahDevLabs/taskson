import json

from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .forms import PersonForm
from .models import Person


class CRUDView(TemplateView):
    template_name = 'person/person.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['persons'] = Person.objects.all()
        context['form'] = PersonForm()

        return context


class CRUDAPIView(View):
    def get(self, request, *args, **kwargs):
        persons = Person.objects.all()
        return JsonResponse({'persons': list(persons.values())})


class PersonCreateView(View):
    def post(self, request, *args, **kwargs):
        # Parse JSON data from the request body
        data = json.loads(request.body)
        form = PersonForm(data)

        if form.is_valid():
            person = form.save()
            return JsonResponse({'message': 'Person created successfully', 'person_id': person.id}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)


class PersonUpdateView(View):
    def post(self, request, person_id, *args, **kwargs):
        # Check if the person with the given ID exists
        try:
            person = Person.objects.get(pk=person_id)
        except Person.DoesNotExist:
            return JsonResponse({'error': 'Person not found'}, status=404)

        # Parse JSON data from the request body
        data = json.loads(request.body)
        form = PersonForm(data, instance=person)

        if form.is_valid():
            person = form.save()
            return JsonResponse({'message': 'Person updated successfully', 'person_id': person.id})
        else:
            return JsonResponse({'errors': form.errors}, status=400)


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
