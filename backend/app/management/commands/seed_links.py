import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

from django_seed import Seed
from links.models import Link

CustomUser = get_user_model()


class Command(BaseCommand):
    """Django command to seed database with links"""

    help = "Seed database with links"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, type=int, help="How many links?")

    def handle(self, *args, **options):
        number = options.get("number")
        self.stdout.write(self.style.WARNING(f"Seeding database with {number} links"))

        seeder = Seed.seeder()

        users = CustomUser.objects.all().filter(is_staff=False, is_superuser=False)

        seeder.add_entity(
            Link,
            number,
            {
                "owner": lambda x: random.choice(users),
                "favorited": lambda x: bool(random.getrandbits(1)),
                "article_url": lambda x: seeder.faker.url(),
                "audio_url": lambda x: "",
            },
        )

        inserted_pks = seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"Database seeded with {number} links succesfully"))
