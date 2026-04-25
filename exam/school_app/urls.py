from django.urls import path
from .views import student_info, teacher_info,add_student, add_teacher

urlpatterns = [
    path  ('', student_info, name ='student' ),
    path  ('teacher/', teacher_info, name ='teacher' ),
    path  ('add-teacher/', add_teacher, name ='add-teacher' ),
    path  ('add-student/', add_student, name ='add-student' ),
]