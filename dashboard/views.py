from django.conf import settings
from django.http.response import JsonResponse
from django.db.models import Sum, Count

from .models import *
from .utils.viiews_utils import check_params


def viewer_count(request):
    params = check_params(request.GET.get('start'), request.GET.get('end'),
                          request.GET.get('device'), request.GET.get('content'))
    error = params.get('error')
    if error:
        return error

    start = params.get('start')
    end = params.get('end')
    device_id = params.get('device')
    content_id = params.get('content')

    device_content = DeviceContent.objects.filter(
        device__id=device_id,
        content__id=content_id,
        start_time__range=(start, end),
        end_time__range=(start, end)
    ).order_by('start_time')
    if not device_content.exists():
        return JsonResponse({'error': 'Device with content were not found'})

    # device = Device.objects.get(device_id=device_id)
    viewers = 0
    for el in device_content:
        start_time = el.start_time if el.start_time > start else start
        end_time = el.end_time if el.end_time < end else end

        viewers += Person.objects.filter(
            device__id=device_id,
            appear__range=(start_time, end_time),
            disappear__range=(start_time, end_time)
        ).count()

    # content = get_object_or_404(Content, pk=content_id)
    # return JsonResponse({'content': content_id})
    return JsonResponse({
        "start": start.strftime(settings.TIME_FORMAT),
        "end": end.strftime(settings.TIME_FORMAT),
        "device_id": device_id,
        "content_id": content_id,
        "views": viewers})


def avg_age(request):
    params = check_params(request.GET.get('start'), request.GET.get('end'),
                          request.GET.get('device'), request.GET.get('content'))
    error = params.get('error')
    if error:
        return error

    start = params.get('start')
    end = params.get('end')
    device_id = params.get('device')
    content_id = params.get('content')

    device_content = DeviceContent.objects.filter(
        device__id=device_id,
        content__id=content_id,
        start_time__range=(start, end),
        end_time__range=(start, end)
    ).order_by('start_time')
    if not device_content.exists():
        return JsonResponse({'error': 'Device with content were not found'})

    # device = Device.objects.get(device_id=device_id)
    total_count = 0
    total_sum = 0
    for el in device_content:
        start_time = el.start_time if el.start_time > start else start
        end_time = el.end_time if el.end_time < end else end

        aggregation = Person.objects.filter(
            device__id=device_id,
            appear__range=(start_time, end_time),
            disappear__range=(start_time, end_time)
        ).all().aggregate(Sum('age'), Count('age'))
        total_count += aggregation.get('age__count', 0)
        current_sum = aggregation.get('age__sum')
        current_sum = current_sum if current_sum else 0
        total_sum += current_sum
    average_age = 0 if total_count == 0 else total_sum/(total_count*1.0)

    return JsonResponse({
        "start": start.strftime(settings.TIME_FORMAT),
        "end": end.strftime(settings.TIME_FORMAT),
        "device_id": device_id,
        "content_id": content_id,
        "avg_age": average_age})


def gender_dist(request):
    params = check_params(request.GET.get('start'), request.GET.get('end'),
                          request.GET.get('device'), request.GET.get('content'))
    error = params.get('error')
    if error:
        return error

    start = params.get('start')
    end = params.get('end')
    device_id = params.get('device')
    content_id = params.get('content')

    device_content = DeviceContent.objects.filter(
        device__id=device_id,
        content__id=content_id,
        start_time__range=(start, end),
        end_time__range=(start, end)
    ).order_by('start_time')
    if not device_content.exists():
        return JsonResponse({'error': 'Device with content were not found'})

    male_count = 0
    female_count = 0
    for el in device_content:
        start_time = el.start_time if el.start_time > start else start
        end_time = el.end_time if el.end_time < end else end

        aggregation = Person.objects.filter(
            device__id=device_id,
            appear__range=(start_time, end_time),
            disappear__range=(start_time, end_time)
        ).all().values('gender')
        print(aggregation)
    #     total_count += aggregation.get('age__count', 0)
    #     current_sum = aggregation.get('age__sum')
    #     current_sum = current_sum if current_sum else 0
    #     total_sum += current_sum
    # average_age = 0 if total_count == 0 else total_sum/(total_count*1.0)

    return JsonResponse({
        "start": start.strftime(settings.TIME_FORMAT),
        "end": end.strftime(settings.TIME_FORMAT),
        "device_id": device_id,
        "content_id": content_id,
        "gender-dist": {'male': 0, 'female': 0}
    })
