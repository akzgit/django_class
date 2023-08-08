import random
from django.contrib.auth.models import User
from faker import Faker

fake = Faker()

def create_fake_users(num_users=10):
    for _ in range(num_users):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()

        User.objects.create(first_name=first_name, last_name=last_name, email=email)

if __name__ == "__main__":
    create_fake_users()
