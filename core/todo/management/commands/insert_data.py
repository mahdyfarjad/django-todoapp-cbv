from django.core.management.base import BaseCommand

from faker import Faker
import random
from datetime import datetime

from accounts.models import User, Profile
from todo.models import Task


class Command(BaseCommand):
    help = "inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.faker = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.faker.email(), password="test@123456")
        profile = Profile.objects.get(user=user)
        profile.user=user
        profile.first_name = self.faker.first_name()
        profile.last_name = self.faker.last_name()
        profile.save()

        for _ in range(5):
            Task.objects.create(
                user = user,
                title = self.faker.paragraph(nb_sentences=1),
                complete = random.choice([True, False]),
            )

        
        