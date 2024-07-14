from faker import Faker
from faker.providers import internet
import random
from .models import *

fake = Faker()

def seed_db(n=10):
    for i in range(n):
        department_objs = Department.objects.all()
        random_index = random.randint(0, len(department_objs))
        student_id = f'23AMCA{random.randint(1101100, 1289034)}'
        department = department_objs[random_index]
        student_name = fake.name()
        student_email = fake.email()
        student_age = random.randint(20, 30)
        student_address = fake.address()

        student_id_objs = StudentId.objects.create(student_id = student_id)

        student_objs = Student.objects.create(
            department = department
            student_id = student_id_objs
            student_name = student_name
            student_email = student_email
            student_age = student_age
            student_address = student_address
        )