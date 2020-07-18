from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from django_seed import Seed

CustomUser = get_user_model()


class Command(BaseCommand):
    """Django command to seed database with a test user"""

    help = "Seed database with test user"

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING(f"Seeding database with a test user users"))

        seeder = Seed.seeder()

        seeder.add_entity(CustomUser, 1, {"email": "test1@test.com", "password": "test123456", "is_staff": False, "is_superuser": False,})

        inserted_pks = seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"Database seeded with test user succesfully"))
