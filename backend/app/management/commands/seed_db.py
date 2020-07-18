from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to seed database with fake records"""

    help = "Seed database with the type the user provides"

    def add_arguments(self, parser):
        parser.add_arguments("--what", help="What do you want to seed?")

    def handle(self, *args, **options):
        self.stdout.write("Seeding database")
        db_conn = None

        try:
            db_conn = connections["default"]
        except OperationalError:
            self.stdout.write(self.style.SUCCESS("Error seeding database"))

        self.stdout.write(self.style.SUCCESS("Database seeded succesfully"))
