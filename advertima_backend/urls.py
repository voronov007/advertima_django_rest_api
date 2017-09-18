from django.conf.urls import url, include
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^', include('dashboard.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('admin:index'))),
]
