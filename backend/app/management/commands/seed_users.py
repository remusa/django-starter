from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

from django_seed import Seed

CustomUser = get_user_model()


class Command(BaseCommand):
    """Django command to seed database with users"""

    help = "Seed database with users"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, type=int, help="How many users?")

    def handle(self, *args, **options):
        number = options.get("number")
        self.stdout.write(self.style.WARNING(f"Seeding database with {number} users"))

        seeder = Seed.seeder()

        seeder.add_entity(CustomUser, number, {"is_staff": False, "is_superuser": False,})

        inserted_pks = seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"Database seeded with {number} users succesfully"))
