from django.core.management import BaseCommand
from faker import Faker

from search.models import Product
from random import randrange


class Command(BaseCommand):

    def handle(self, *args, **options):
        faker = Faker()

        for _ in range(50):
            Product.objects.create(
                title=faker.name(),
                description=faker.text(200),
                image=faker.image_url(),
                price=randrange(10, 100)
            )
