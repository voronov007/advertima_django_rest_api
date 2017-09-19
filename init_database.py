import os
import csv
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advertima_backend.settings")
import django
django.setup()
from django.contrib.auth.models import User
from django.conf import settings

from dashboard.models import *


PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))


class Generator:
    def create_admin(self):
        admin, _ = User.objects.get_or_create(username='admin')
        admin.is_staff = True
        admin.is_superuser = True
        admin.set_password('superadmin')
        admin.save()

    def upload_events(self):
        content_id_col = 0
        device_id_col = 1
        event_type_col = 2
        event_time_col = 3
        file_path = os.path.join(PROJECT_ROOT, 'init_data', 'events.csv')
        t1 = datetime.now()
        devices = {}
        contents = {}
        device_content_dict = {}
        device_content_list = []
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                device_id = int(row[device_id_col])
                device = devices.get(device_id)
                if not device:
                    device = Device.objects.create(device_id=device_id)
                    devices[device_id] = device

                content_id = int(row[content_id_col])
                content = contents.get(content_id)
                if not content:
                    content = Content.objects.create(
                        content_id=content_id)
                    contents[content_id] = content

                event_time = datetime.strptime(
                    row[event_time_col], settings.TIME_FORMAT)
                event_type = row[event_type_col]
                key = '%s_%s' % (device_id, content_id)
                if event_type == 'start':
                    device_content_dict[key] = DeviceContent(
                        device=device, content=content,
                        start_time=event_time
                    )
                    # DeviceContent.objects.create(
                    #     device=device_obj, content=content_obj, start_time=event_time)
                else:
                    device_content = device_content_dict[key]
                    device_content.end_time = event_time
                    device_content_list.append(device_content)
                    # DeviceContent.objects.filter(
                    #     device=device_obj, content=content_obj, end_time__isnull=True
                    # ).update(end_time=event_time)
        DeviceContent.objects.bulk_create(device_content_list)
        t2 = datetime.now()
        delta = (t2 - t1).total_seconds()
        print('Upload events took "%s" minutes' % (delta / 60.0))

    def upload_persons(self):
        device_id_col = 0
        appears_col = 1
        disappears_col = 2
        age_col = 3
        gender_col = 4
        file_path = os.path.join(PROJECT_ROOT, 'init_data', 'persons.csv')
        t1 = datetime.now()
        devices = {}
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            persons = []
            for row in reader:
                device_id = int(row[device_id_col])
                device = devices.get(device_id)
                if not device:
                    device, _ = Device.objects.get_or_create(device_id=device_id)
                    devices[device_id] = device

                age = int(row[age_col])
                appear = datetime.strptime(
                    row[appears_col], settings.TIME_FORMAT)
                disappear = datetime.strptime(
                    row[disappears_col], settings.TIME_FORMAT)
                gender = row[gender_col]
                persons.append(
                    Person(
                        age=age, gender=gender, appear=appear,
                        disappear=disappear, device=device
                    )
                )
            Person.objects.bulk_create(persons)
        t2 = datetime.now()
        delta = (t2 - t1).total_seconds()
        print('Upload persons took "%s" minutes' % (delta/60.0))

    def start(self):
        # Initialize basic data
        self.create_admin()
        self.upload_events()
        self.upload_persons()

if __name__ == '__main__':
    generator = Generator()
    generator.start()
