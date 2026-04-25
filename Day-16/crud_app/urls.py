from django.urls import path
from .views import student_info,add_student

urlpatterns = [
    path('', student_info, name = 'student'),
    path('add-student/', add_student, name = 'add-student'),
]