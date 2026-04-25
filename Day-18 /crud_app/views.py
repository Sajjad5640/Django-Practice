from django.shortcuts import render,redirect
from crud_app.models import StudentModel
# Create your views here.

def student_list_page (request):
    student_data = StudentModel.objects.all()
    context = {
        'student_data' : student_data
    }
    return render (request, 'student_list.html',context = context)


def add_student_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        StudentModel.objects.create(
            name = name,
            address = address,
            email = email
        )
        return redirect('student')

    return render (request,'add_student.html')

def student_info(request,s_id):

    student_data = StudentModel.objects.get(id = s_id)
    context = {
        'student_data' : student_data
    }
    return render(request, 'student_detail.html',context=context)

def delete_student(request, s_id):
    StudentModel.objects.get(id = s_id).delete()

    return redirect('student')

def edit_student(request,s_id):
    student_data = StudentModel.objects.get(id = s_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        student_data.name = name
        student_data.address = address
        student_data.name = email
        student_data.save()
        return redirect('student')
    context = {
        'student_data' : student_data
    }
    


    return render(request,'edit_student.html',context=context)