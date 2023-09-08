import random
import string
from datetime import date, timedelta
from django.utils.crypto import get_random_string
from gba_search.models import Person


def random_dni():
    return ''.join(random.choice(string.digits) for _ in range(8))


def random_name():
    first_names = ["Alice", "Bob", "Charlie", "David",
                   "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]
    return random.choice(first_names)


def random_lastname():
    last_names = ["Smith", "Johnson", "Williams", "Jones",
                  "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    return random.choice(last_names)


def random_birth_day():
    start_date = date.today() - timedelta(days=365 * 50)  # 50 years ago
    end_date = date.today() - timedelta(days=365 * 18)   # 18 years ago
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))


for _ in range(20):
    dni = random_dni()
    name = random_name()
    lastname = random_lastname()
    birth_day = random_birth_day()
    is_gba = random.choice([True, False])
    person = Person.objects.create(
        dni=dni, name=name, lastname=lastname, birth_day=birth_day, is_gba=is_gba)
    person.save()
