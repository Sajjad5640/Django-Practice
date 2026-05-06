from django import forms
from CaloryCounterapp.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class RegistrationFomr(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass

class ProfileUpdateFrom(forms.ModelForm):
    class Meta:
        model = User_Info_Model
        fields = '__all__'
        exclude = ['user' , 'bmr']

class ConsumedCaloireForm(forms.ModelForm):
    class Meta:
        model = Consumed_Calories_Model
        fields = '__all__'
        exclude = ['consumed_by']