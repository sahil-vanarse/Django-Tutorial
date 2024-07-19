from django.contrib import admin
from .models import Receipe, StudentId, Student, Department, Subject, StudentsMarks, ReportCard
from django.db.models import *

#username : sahil-vanarse-tutorial
#password : S#@5ahil1P

# Register the models
admin.site.register(Receipe)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)

class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register(StudentsMarks, SubjectMarksAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student', 'student_rank', 'total_marks', 'date_of_report_card_generation']
    ordering = ['student_rank']

    def total_marks(self, obj):
        # Calculate the total marks for the student
        total = StudentsMarks.objects.filter(student=obj.student).aggregate(total_marks=Sum('marks'))['total_marks']
        return total if total is not None else 0

    # Add a title for the `total_marks` column in the admin panel
    total_marks.short_description = 'Total Marks'

admin.site.register(ReportCard, ReportCardAdmin)
