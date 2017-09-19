from django.conf import settings
from django.http.response import JsonResponse
from django.db.models import Sum, Count

from .models import *
from .utils.viiews_utils import check_params, get_device_content


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

    device_content = get_device_content(device_id, content_id, start, end)
    if not device_content.exists():
        return JsonResponse({'error': 'Device with content were not found'})

    viewers = 0
    for el in device_content:
        # clarify time ranges for each device-content
        start_time = el.start_time if el.start_time > start else start
        end_time = el.end_time if el.end_time < end else end

        # get persons by time range of each device-content event
        viewers += Person.objects.filter(
            device__device_id=device_id,
            appear__lte=end_time,
            disappear__gte=start_time
        ).count()

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

    device_content = get_device_content(device_id, content_id, start, end)
    if not device_content.exists():
        return JsonResponse({'error': 'Device with content were not found'})

    total_count = 0
    total_sum = 0
    for el in device_content:
        # clarify time ranges for each device-content
        start_time = el.start_time if el.start_time > start else start
        end_time = el.end_time if el.end_time < end else end

        # get aggregated dict of values by time range of each device-content
        aggregation = Person.objects.filter(
            device__device_id=device_id,
            appear__lte=end_time,
            disappear__gte=start_time
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

    device_content = get_device_content(device_id, content_id, start, end)
    if not device_content.exists():
        return JsonResponse({'error': 'Device with content were not found'})

    male_count = 0
    female_count = 0
    for el in device_content:
        # clarify time ranges for each device-content
        start_time = el.start_time if el.start_time > start else start
        end_time = el.end_time if el.end_time < end else end

        # get aggregated QuerySet by time range of each device-content
        aggregation = Person.objects.filter(
            device__device_id=device_id,
            appear__lte=end_time,
            disappear__gte=start_time
        ).all().values('gender').annotate(count=Count('gender')).distinct()

        if aggregation.exists():
            for item in aggregation:
                gender = item['gender']
                if gender == Person.MALE:
                    male_count += item['count']
                else:
                    female_count += item['count']

    total_count = male_count + female_count
    if total_count == 0:
        male_weight = 0
        female_weight = 0
    else:
        male_weight = male_count/(total_count*1.0)
        male_weight = round(male_weight, 2)
        female_weight = female_count/(total_count*1.0)
        female_weight = round(female_weight, 2)

    return JsonResponse({
        "start": start.strftime(settings.TIME_FORMAT),
        "end": end.strftime(settings.TIME_FORMAT),
        "device_id": device_id,
        "content_id": content_id,
        "gender-dist": {'male': male_weight, 'female': female_weight}
    })
