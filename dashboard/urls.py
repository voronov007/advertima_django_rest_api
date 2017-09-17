from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^viewer-count/$', views.viewer_count, name='viewer_count'),
    url(r'^avg-age/$', views.avg_age, name='avg_age'),
    url(r'^gender-dist/$', views.gender_dist, name='gender_dist')
]