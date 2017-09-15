from django.db import models


class Device(models.Model):
    def __str__(self):
        return 'Device(pk="%s")' % self.pk

    def __repr__(self):
        return self.__str__()


class Content(models.Model):
    def __str__(self):
        return 'Content(pk="%s")' % self.pk

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


class PersonScene(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='scenes'
    )
    appear = models.DateTimeField()
    disappear = models.DateTimeField()

    def __str__(self):
        return 'PersonScene(pk="%s")' % self.pk

    def __repr__(self):
        return self.__str__()


class Event(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='events'
    )
    content = models.ForeignKey(
        Content,
        on_delete=models.CASCADE,
        related_name='events'
    )
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True)

    def __str__(self):
        return 'Event(pk="%s")' % self.pk

    def __repr__(self):
        return self.__str__()