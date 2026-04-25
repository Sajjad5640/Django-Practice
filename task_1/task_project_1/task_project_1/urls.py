
from django.contrib import admin
from django.urls import path
from task_project_1.views import dashboard_page, profile_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',dashboard_page, name = 'dashboard'),
    path('profile/',profile_page, name = 'profile')
]
