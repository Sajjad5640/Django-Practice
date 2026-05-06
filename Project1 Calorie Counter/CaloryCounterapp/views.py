from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from datetime import date
from CaloryCounterapp.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from CaloryCounterapp.forms import *
from django.db.models import Sum,Count
# Create your views here.
def register_page(request):
    if request.method == 'POST':
        form_data = RegistrationFomr(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'Registration is Successful Bro')
            return redirect('login_page')

    form_data = RegistrationFomr()
    context = {
        'form_data' : form_data,
        'form_name' : 'Registraion Form',
        'form_btn' : 'Register'
    }

    return render(request, 'master/base-form.html', context)

def login_page(request):

    if request.method == 'POST':
        form_data = LoginForm(request, data=request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('home_page')


    form_data = LoginForm()
    context={
        'form_data' : form_data,
        'form_name' : 'Login Page',
        'form_btn' : 'Login'
    }

    return render(request, 'master/base-form.html', context)
@login_required
def home_page(request):
    try:
        current_user = request.user
        bmr = round(request.user.user_info.bmr, 2)
    except:
        bmr = 0

    today = date.today()
    today_consumed_data= Consumed_Calories_Model.objects.filter(
        consumed_by = current_user,
        created_at = today
    )
    total_consumed_data = Consumed_Calories_Model.objects.aggregate(
        total_calorie=Sum('calorie'),
        total_count = Count('calorie'),

    )
    total_cal = total_consumed_data['total_calorie'] or 0
    less_more = bmr - total_cal

    if bmr > total_cal:
        suggestion = 'Eat more'
    else:
        suggestion = 'Eat less'
    context={
        'required_calorie' : bmr,
        'today_consumed_data' : today_consumed_data,
        'total_count' : total_consumed_data['total_count'],
        'consumed_calories' : total_cal,
        'less_more' : less_more,
        'suggestion' : suggestion
    }

    return render(request, 'dashboard.html', context)
@login_required

def logout_page(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('login_page')

@login_required
def profile_page(request):

    return render(request, 'profile.html')

@login_required
def update_page(request):
    try:
        current_user = request.user.user_info
    except:
        current_user = None

    if request.method == 'POST':
        form_data = ProfileUpdateFrom(request.POST, instance=current_user)
        #using commit false as we are excluded 2 fields 
        # but we need to access the database
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            weight = data.weight
            height = data.height
            age = data.age
            if data.gender == 'Male':
                bmr = 66.47+(13.75 * weight) + (5.003 * height) - (6.775 *age)

            else:
                bmr = 655.1+(9.563 * weight) + (1.850 * height) - (4.676 *age)

            data.bmr = bmr
            data.save()
            messages.success(request, 'Profile Update Successfull Bro')
            return redirect('profile_page')

    form_data = ProfileUpdateFrom(instance=current_user)
    context={
        'form_data' : form_data,
        'form_name' : 'Update Profile Info',
        'form_btn' : 'Update'
    }

    return render(request, 'master/base-form.html', context)

def consumed_calories(request):
    consumed_data = Consumed_Calories_Model.objects.filter(consumed_by = request.user)
    context = {
        'consumed_data': consumed_data
    }

    return render(request, 'calory-list.html', context)

def add_calorie(request):
    if request.method == 'POST':
        form_data = ConsumedCaloireForm(request.POST)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.consumed_by = request.user
            data.save()
            messages.success(request, 'successful Bro')
            return redirect('consumed_calories')

    form_data = ConsumedCaloireForm()
    context={
        'form_data' : form_data,
        'form_name' : 'Add Calorie Info',
        'form_btn' : 'Add Calorie'
    }
    return render(request, 'master/base-form.html', context)

def edit_calorie(request, id):
    try:
        data = Consumed_Calories_Model.objects.get(id=id)
    except:
        data = None
    if request.method == 'POST':
        form_data = ConsumedCaloireForm(request.POST, instance=data)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.consumed_by = request.user
            data.save()
            messages.success(request, 'successful Bro')
            return redirect('consumed_calories')

    form_data = ConsumedCaloireForm(instance=data)
    context={
        'form_data' : form_data,
        'form_name' : 'Edit Calorie Info',
        'form_btn' : 'Update Calorie'
    }
    return render(request, 'master/base-form.html', context)

def delete_calorie(request, id):
    try:
        data = Consumed_Calories_Model.objects.get(id=id)
    except:
        data = None
    data.delete()
    messages.success(request, 'success Bro')
    return redirect('consumed_calories')