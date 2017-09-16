from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^viewer-count/'
        r'(?start=(?P<start_timestamp>\w+))'
        r'(?end=(?P<end_timestamp>\w+))'
        r'(?device=(?P<device_id>\d+))'
        r'(?content=(?P<content_id>\d+))$', views.viewer_count,
        name='viewer_count'),
    url(r'^avg-age/'
        r'(?start=(?P<start_timestamp>\w+))'
        r'(?end=(?P<end_timestamp>\w+))'
        r'(?device=(?P<device_id>\d+))'
        r'(?content=(?P<content_id>\d+))$', views.avg_age,
        name='avg_age'),
    url(r'^gender-dist/'
        r'(?start=(?P<start_timestamp>\w+))'
        r'(?end=(?P<end_timestamp>\w+))'
        r'(?device=(?P<device_id>\d+))'
        r'(?content=(?P<content_id>\d+))$', views.gender_dist,
        name='gender_dist')
]