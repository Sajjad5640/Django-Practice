from django.shortcuts import render, redirect
from crud_app.models import StudentModel
# Create your views here.
def student_info(req):
    student_data = StudentModel.objects.all()
    context = {
       "student_data" : student_data
    }
    return render (req, 'student.html', context= context)

def add_student(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        address = req.POST.get('address')
        admission_date = req.POST.get('admission_date')
        StudentModel.objects.create(
            name = name,
            email = email,
            address = address,
            admission_date = admission_date
        )

        return redirect('student')

    return render (req, 'add_student.html')