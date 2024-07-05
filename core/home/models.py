from django.db import models # type: ignore

# Create your models here.

# in models there is the class known as model which is used for the database
class Student(models.Model):

    # this fields comes under the models class
    # id = models.AutoField()
    name = models.CharField(max_length=100) # character field
    age = models.IntegerField() # if blank means he can put any else none will be added. We can add default parameter in it so that we can set default age if the used dont add it
    email = models.EmailField(null=True, blank=True) # for the email 
    address = models.TextField(null=True, blank=True) # for the address
    # image = models.ImageField() # for the image
    # file = models.FileField() # for the any other file

class Car(models.Model):
    car_name = models.CharField(max_length=50)
    speed = models.IntegerField(default = 50)

    def __str__(self):
        return self.car_name

