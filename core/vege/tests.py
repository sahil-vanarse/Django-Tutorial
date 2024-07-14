from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
for user in User.objects.all():
    print(user.username, user.email)

