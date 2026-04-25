
from django.contrib import admin
from django.urls import path
from class_project2.views import homepage, about_page, contact_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage, name = 'home'),
    path('about/',about_page, name = 'about'),
    path('contact/',contact_page, name = 'contact')
]
