import os
import csv
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advertima_backend.settings")
import django
django.setup()
from django.contrib.auth.models import User

from dashboard.models import *


PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


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
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                device, _ = Device.objects.get_or_create(
                    device_id=row[device_id_col])
                content, _ = Content.objects.get_or_create(
                    content_id=row[content_id_col])
                event_time = datetime.strptime(row[event_time_col], TIME_FORMAT)
                event_type = row[event_type_col]
                if event_type == 'start':
                    DeviceContent.objects.create(
                        device=device, content=content, start_time=event_time)
                else:
                    DeviceContent.objects.filter(
                        device=device, content=content, end_time__isnull=True
                    ).update(end_time=event_time)
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
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            persons = []
            for row in reader:
                device, _ = Device.objects.get_or_create(
                    device_id=row[device_id_col])
                age = int(row[age_col])
                appear = datetime.strptime(row[appears_col], TIME_FORMAT)
                disappear = datetime.strptime(row[disappears_col], TIME_FORMAT)
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
        print('Upload person took "%s" minutes' % (delta/60.0))

    def start(self):
        # Initialize basic data
        self.create_admin()
        self.upload_events()
        self.upload_persons()

if __name__ == '__main__':
    generator = Generator()
    generator.start()
