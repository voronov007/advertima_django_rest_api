from django.db import models

from .content import Content


__all__ = ['Device', 'DeviceContent']


class Device(models.Model):
    contents = models.ManyToManyField(
        Content, through='DeviceContent', related_name='devices')
    device_id = models.PositiveIntegerField()

    def __str__(self):
        return 'Device(pk="%s")' % self.pk

    def __repr__(self):
        return self.__str__()


class DeviceContent(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'DeviceContent(pk="%s")' % self.pk

    def __repr__(self):
        return self.__str__()
# class Event(models.Model):
#     device = models.ForeignKey(
#         Device,
#         on_delete=models.CASCADE,
#         related_name='events'
#     )
#     person = models.ForeignKey(
#         Person,
#         on_delete=models.CASCADE,
#         related_name='events'
#     )
#     content = models.ForeignKey(
#         Content,
#         on_delete=models.CASCADE,
#         related_name='events'
#     )
#     start = models.DateTimeField()
#     end = models.DateTimeField(blank=True)
#
#     def __str__(self):
#         return 'Event(pk="%s")' % self.pk
#
#     def __repr__(self):
#         return self.__str__()