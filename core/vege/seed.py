from faker import Faker #type: ignore
import random
from .models import Department, Student, StudentId, Receipe, Subject, StudentsMarks


fake = Faker()


def create_subjects_marks(n):
    try:
        students = Student.objects.all()
        for student in students:
            subjects = Subject.objects.all()
            for subject in subjects:
                StudentsMarks.objects.create(
                    student = student,
                    subject = subject,
                    marks = random.randint(0, 100)
                )

    except Exception as e:
        print(e)

def seed_db(n=10):
    for _ in range(n):
        try:
            department_objs = Department.objects.all()
            random_index = random.randint(0, len(department_objs)-1)  # Adjusted index calculation
            student_id = f'23AMCA{random.randint(1101100, 1289034)}'
            department = department_objs[random_index]
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20, 30)
            student_address = fake.address()

            student_id_objs = StudentId.objects.create(student_id=student_id)

            student_objs = Student.objects.create(
                department=department,
                student_id=student_id_objs,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address
            )
        except Exception as e:
            print(e)
