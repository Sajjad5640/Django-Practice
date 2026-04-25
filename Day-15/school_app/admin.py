from django.contrib import admin
from school_app.models import TeacherModel, StudentModel, DepartmentModel, CourseModel, ExamModel, ClassroomModel, AttendanceModel

# Register your models here.
admin.site.register(TeacherModel)
admin.site.register(StudentModel)
admin.site.register(DepartmentModel)
admin.site.register(CourseModel)
admin.site.register(ExamModel)
admin.site.register(ClassroomModel)
admin.site.register(AttendanceModel)
