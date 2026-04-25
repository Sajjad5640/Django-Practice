from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} - {self.email}"