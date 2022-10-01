from django.core.management.base import BaseCommand
from accounts.models import Customer

from faker import Faker

CustomerModel = Customer


class Command(BaseCommand):
    """
    python manage.py fake-customers 500
    """

    help = "Create random boards"  # noqa A003

    def add_arguments(self, parser):
        parser.add_argument("total", type=int, choices=range(1, 1000), help='Number of users to create')

    def handle(self, *args, **options):
        fake = Faker()
        total = options['total']
        obj = [
            CustomerModel(
                name=fake.name(),
                last_name=fake.last_name(),
                date_birth=fake.date(),
                password=fake.password(),
                about_human=fake.text(),
                username=fake.user_name(),
                email=fake.email(),
                country=fake.country(),
                city=fake.city(),
            )
            for _ in range(total)
        ]

        CustomerModel.objects.bulk_create(obj)
        print("Customer Created!")  # noqa T001
