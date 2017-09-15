import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advertima_backend.settings")
import django
django.setup()

from django.contrib.auth.models import User


class Generator:
    def create_admin(self):
        admin, _ = User.objects.get_or_create(username='admin')
        admin.is_staff = True
        admin.is_superuser = True
        admin.set_password('superadmin')
        admin.save()

    def start(self):

        # Initialize basic data
        self.create_admin()

if __name__ == '__main__':
    generator = Generator()
    generator.start()
