from django.shortcuts import render
from school_app.models import TeacherModel, StudentModel, DepartmentModel, CourseModel, ExamModel, ClassroomModel, AttendanceModel

def home_page(req):

    return render (req, 'home.html')

def teacher_page(req):
    teacher_data = TeacherModel.objects.all()
    context = {
        "teacher_data" : teacher_data
    }

    return render(req, 'teacher.html',context = context)
def student_page(req):
    student_data = StudentModel.objects.all()
    context = {
        "student_data" : student_data
    }

    return render(req, 'student.html',context = context)
def department_page(req):
    department_data = DepartmentModel.objects.all()
    context = {
        "department_data" : department_data
    }

    return render(req, 'department.html',context = context)
def course_page(req):
    course_data = CourseModel.objects.all()
    context = {
        "course_data" : course_data
    }

    return render(req, 'course.html',context = context)
def exam_page(req):
    exam_data = ExamModel.objects.all()
    context = {
        "exam_data" : exam_data
    }

    return render(req, 'exam.html',context = context)
def classroom_page(req):
    classroom_data = ClassroomModel.objects.all()
    context = {
        "classroom_data" : classroom_data
    }

    return render(req, 'classroom.html',context = context)
def attendance_page(req):
    attendance_data = AttendanceModel.objects.all()
    context = {
        "attendance_data" : attendance_data
    }

    return render(req, 'attendance.html',context = context)