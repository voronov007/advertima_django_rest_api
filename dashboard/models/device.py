from django.db import models

from .content import Content


__all__ = ['Device', 'DeviceContent']


class Device(models.Model):
    contents = models.ManyToManyField(
        Content, through='DeviceContent', related_name='devices')
    device_id = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return 'Device(pk="%s", device_id="%s")' % (self.pk, self.device_id)

    def __repr__(self):
        return self.__str__()


class DeviceContent(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

    start_time = models.DateTimeField(db_index=True,)
    end_time = models.DateTimeField(db_index=True, blank=True, null=True)

    def __str__(self):
        return 'DeviceContent(pk="%s", device="%s", content="%s", start="%s", ' \
               'end="%s")' % (self.pk, self.device.device_id,
                              self.content.content_id, self.start_time,
                              self.end_time)

    def __repr__(self):
        return self.__str__()
