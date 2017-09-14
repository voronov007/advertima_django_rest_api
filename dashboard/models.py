from django.db import models


class Device(models.Model):
    def __str__(self):
        return 'Device(pk="%s")' % self.pk

    def __repr__(self):
        return self.__str__()


class Person(models.Model):
    age = models.PositiveIntegerField()

    MALE = 'male'
    FEMALE = 'female'
    TYPE_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=7, choices=TYPE_CHOICES)

    def __str__(self):
        return 'Person(pk="%s")' % self.pk

    def __repr__(self):
        return self.__str__()


class PersonAppear(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='appears',
        primary_key=True
    )
    appear = models.DateTimeField()
    disappear = models.DateTimeField()

    def __str__(self):
        return 'PersonAppear(pk="%s")' % self.pk

    def __repr__(self):
        return self.__str__()


class Event(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='events',
        primary_key=True
    )
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True)

    def __str__(self):
        return 'Event(pk="%s")' % self.pk

    def __repr__(self):
        return self.__str__()