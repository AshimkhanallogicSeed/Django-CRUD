from django.db import models


class Students(models.Model):  
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=101)
    address = models.CharField(max_length=100)
    marks = models.IntegerField(default=100)
    student_image = models.ImageField(upload_to="std_image")
