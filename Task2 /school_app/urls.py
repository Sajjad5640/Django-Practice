from django.urls import path
from .views import home_page, teacher_page,add_teacher_page

urlpatterns = [
    path('', home_page, name = 'home'),
    path('teacher/', teacher_page, name = 'teacher'),
    path('add-teacher/', add_teacher_page, name = 'add_teacher'),
]