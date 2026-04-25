from django.db import models

# Create your models here.

class TeacherModel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

