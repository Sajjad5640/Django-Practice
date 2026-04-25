from django.shortcuts import render,redirect

# Create your views here.
from school_app.models import TeacherModel

def home_page(req):

    return render( req, 'home.html')

def teacher_page(req):

    teacher_data = TeacherModel.objects.all()

    context = {
        "teacher_data": teacher_data
    }

    return render (req,'teacher.html',context=context)

def add_teacher_page (req):
    if req.method == 'POST':
        name = req.POST.get('name')
        address = req.POST.get('address')
        email = req.POST.get('email')

        TeacherModel.objects.create(
            name =name,
            address= address,
            email = email
        )
        return redirect('teacher')


    return render (req, 'add_teacher.html')