from django.shortcuts import render, redirect
from crud_op_app.models import StudentModel
# Create your views here.

def student_info(request):
    student_data = StudentModel.objects.all()

    context = {
        'student_data' : student_data
    }

    return render (request, 'student_list.html', context=context)


def add_student_info (request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        age = request.POST.get('age')

        StudentModel.objects.create(
            name = name,
            email = email,
            address = address,
            age = age
        )
        return redirect('student')


    return render (request, 'add_student.html')