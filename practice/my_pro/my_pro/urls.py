
from django.contrib import admin
from django.urls import path
# from my_pro.views import home_page
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name ='home'),
    path('about/', about_page, name ='about'),
    path('contact/', contact_page, name ='contact'),
]
