from django.shortcuts import render,redirect
from school_app.models import StudentModel, TeacherModel
# Create your views here.

def student_info(request):
    student_data = StudentModel.objects.all()

    context = {
        'student_data' : student_data
    }
    return render (request, 'student_info.html', context=context)
def teacher_info(request):
    teacher_data = TeacherModel.objects.all()

    context = {
        'teacher_data' : teacher_data
    }
    return render (request, 'teacher_info.html', context=context)

def add_teacher(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        TeacherModel.objects.create(
            name = name,
            email = email,
            age = age
        )
        return redirect('teacher')

    return render (request, 'add_teacher.html')
def add_student(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        StudentModel.objects.create(
            name = name,
            email = email,
            age = age
        )
        return redirect('student')

    return render (request, 'add_student.html')