from django.contrib import admin
from school_app.models import StudentModel, TeacherModel
# Register your models here.

admin.site.register(StudentModel)
admin.site.register(TeacherModel)