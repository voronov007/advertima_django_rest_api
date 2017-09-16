from django.shortcuts import get_object_or_404, render
from django.http.response import JsonResponse

from .models import *


def viewer_count(request, start_timestamp, end_timestamp, device_id,
                 content_id):
    content = get_object_or_404(Content, pk=content_id)
    # return render(request, 'dashboard/viewer_count.html', {'content': content})
    return JsonResponse({'content': content})


def avg_age(request, start_timestamp, end_timestamp, device_id, content_id):
    content = get_object_or_404(Content, pk=content_id)
    # return render(request, 'dashboard/viewer_count.html', {'content': content})
    return JsonResponse({'content': content})

def gender_dist(request, start_timestamp, end_timestamp, device_id,
                content_id):
    content = get_object_or_404(Content, pk=content_id)
    # return render(request, 'dashboard/viewer_count.html', {'content': content})
    return JsonResponse({'content': content})
