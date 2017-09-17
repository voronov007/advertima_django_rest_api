from django.shortcuts import get_object_or_404, render
from django.http.response import JsonResponse

from .models import *


def viewer_count(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    device_id = request.GET.get('device')
    content_id = request.GET.get('content')
    # content = get_object_or_404(Content, pk=content_id)
    return JsonResponse({'content': content_id})


def avg_age(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    device_id = request.GET.get('device')
    content_id = request.GET.get('content')
    return JsonResponse({'content': content})


def gender_dist(request):
    start = request.GET.get('start')
    end = request.GET.get('end')
    device_id = request.GET.get('device')
    content_id = request.GET.get('content')
    return JsonResponse({'content': content})
