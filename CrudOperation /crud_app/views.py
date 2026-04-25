from django.shortcuts import render, redirect
from crud_app.models import StudentModel
# Create your views here.

def student_info(request):
    student_data = StudentModel.objects.all()

    context = {
        'student_data' : student_data
    }

    return render (request, 'student_list.html', context=context)