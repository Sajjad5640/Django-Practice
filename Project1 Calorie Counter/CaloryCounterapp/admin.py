from django.contrib import admin
from CaloryCounterapp.models import *

# Register your models here.
admin.site.register([
    User,
    User_Info_Model,
    Consumed_Calories_Model,
])