from django.contrib import admin #type: ignore


# username = sahil-vanarse-tutorial
# password = S#@5ahil1P
# Register your models here.
from .models import *
admin.site.register(Receipe)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)

class SubjectMarksAdmin(admin.ModelAdmin):
    # list_display is the method we will override it
    list_display = ['student', 'subject', 'marks']
admin.site.register(StudentsMarks, SubjectMarksAdmin)
