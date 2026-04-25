from django.db import models

class TeacherModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return f"{self.name}-{self.email}"
class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    roll_number = models.IntegerField()


    def __str__(self):
        return f"{self.name}-{self.roll_number}"
class DepartmentModel(models.Model):
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    office_number = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name}-{self.office_number}"
class CourseModel(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    credit = models.IntegerField()


    def __str__(self):
        return f"{self.title}-{self.credit}"
class ExamModel(models.Model):
    subject = models.CharField(max_length=100)
    date = models.DateField()
    total_marks = models.IntegerField()


    def __str__(self):
        return f"{self.subject}-{self.total_marks}"
class ClassroomModel(models.Model):
    room_number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    building = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.room_number}-{self.building}"
class AttendanceModel(models.Model):
    student_name = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.student_name}-{self.status}"
