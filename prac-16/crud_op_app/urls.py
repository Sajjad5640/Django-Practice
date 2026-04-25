from django.urls import path
from .views import student_info,add_student_info
urlpatterns = [
    path('', student_info, name = "student"),
    path('add_student/', add_student_info, name = "add_student"),
]