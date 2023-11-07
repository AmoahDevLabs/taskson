from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name
