import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ProTwo.settings")

import django
django.setup()

from faker import Faker
from AppTwo.models import User

def populate(N = 5):
    Faken = Faker()
    for enrty in range(N):
        fake_firstname = Faken.first_name()
        fake_secondname = Faken.last_name()
        fake_email = Faken.email()
        user = User.objects.get_or_create(first_name = fake_firstname,second_name = fake_secondname,email = fake_email)[0]
        user.save()
    return user

if __name__ == '__main__':
    print("Populate Script!")
    populate(30)
    print("Populate Completed!")
