from django.db import models

__all__ = ['Content', ]


class Content(models.Model):
    content_id = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return 'Content(pk="%s")' % self.pk

    def __repr__(self):
        return self.__str__()