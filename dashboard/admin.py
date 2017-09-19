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
    list_filter = ('gender', 'age')
    list_display_links = ('id', )


@admin.register(DeviceContent)
class DeviceContentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'get_device_id', 'get_content_id', 'start_time', 'end_time'
    )
    list_filter = ('device__device_id', 'content__content_id', )
    list_display_links = ('id', )

    def get_device_id(self, obj):
        return obj.device.device_id

    def get_content_id(self, obj):
        return obj.content.content_id

