from django.contrib import admin

from .models import *


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        'id', '__str__',
    )
    list_filter = ('id',)
    list_display_links = ('id', '__str__')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'id', '__str__',
    )
    list_filter = ('id',)
    list_display_links = ('id', '__str__')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'gender', 'age'
    )
    list_filter = ('id', 'gender', 'age')
    list_display_links = ('id', )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'start', 'end'
    )
    list_filter = ('id', )
    list_display_links = ('id', )

