from django.db import models

class StudentModel (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    admission_date = models.DateField()

    def __str__(self):
        return f"{self.name}-{self.email}"


