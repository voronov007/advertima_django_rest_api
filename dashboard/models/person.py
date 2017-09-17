from django.db import models

from .device import Device


__all__ = ['Person', ]


class Person(models.Model):
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name='persons'
    )
    age = models.PositiveIntegerField()

    MALE = 'male'
    FEMALE = 'female'
    TYPE_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=7, choices=TYPE_CHOICES)
    appear = models.DateTimeField()
    disappear = models.DateTimeField()

    def __str__(self):
        return 'Person(pk="%s")' % self.pk

    def __repr__(self):
        return self.__str__()