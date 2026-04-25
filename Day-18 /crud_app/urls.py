from django.urls import path
from crud_app.views import student_list_page,add_student_page,student_info,delete_student,edit_student

urlpatterns = [
    path('',student_list_page, name = 'student'),
    path('add_student/',add_student_page, name = 'add_student'),
    path('student-info/<int:s_id>/', student_info, name = 'student_info'),
    path('student-delete/<int:s_id>/', delete_student, name = 'delete_student'),
    path('student-edit/<int:s_id>/', edit_student, name = 'edit_student')
]