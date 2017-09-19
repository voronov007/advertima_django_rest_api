from datetime import datetime

from django.conf import settings
from django.db.models import QuerySet

from ..models import DeviceContent


def check_params(start, end, device_id, content_id) -> dict:
    """
        Description:
            check GET parameters, convert values if necessary and
            return dict with corrected values. If an error was occurred then
            `error` key and value will be added to the result dict
    """
    if not start:
        return {'error': "<start_timestamp> is required"}

    try:
        start = datetime.strptime(start, settings.TIME_FORMAT)
    except ValueError:
        return {'error': "<start_timestamp> has wrong time format. Use"
                         "'yyyy-mm-dd hh:mm:ss' format"}

    if not end:
        return {'error': "<end_timestamp> is required"}

    try:
        end = datetime.strptime(end, settings.TIME_FORMAT)
    except ValueError:
        return {'error': "<end_timestamp> has wrong time format. Use"
                         "'yyyy-mm-dd hh:mm:ss' format"}

    if start > end:
        return {'error': "<end_timestamp> must be higher than "
                         "<start_timestamp>"}

    if not device_id:
        return {'error': "<device_id> is required"}

    try:
        device_id = int(device_id)
    except ValueError:
        return {'error': "device_id must be integer"}

    if not content_id:
        return {'error': "<content_id> is required"}

    try:
        content_id = int(content_id)
    except ValueError:
        return {'error': "<content_id> must be integer"}

    return {
        'start': start,
        'end': end,
        'device': device_id,
        'content': content_id
    }


def get_device_content(device_id: int, content_id: int,
                       start: datetime, end: datetime) -> QuerySet:
    """
        Description:
            get all device-content pairs from the listed range: [start, end]
    """
    return DeviceContent.objects.filter(
        device__device_id=device_id,
        content__content_id=content_id,
        start_time__lte=end,
        end_time__gte=start
    ).order_by('start_time')
