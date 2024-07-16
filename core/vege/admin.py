from django.contrib import admin #type: ignore


# username = sahil-vanarse-tutorial
# password = S#@5ahil1P
# Register your models here.
from .models import *
admin.site.register(Receipe)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Department)
