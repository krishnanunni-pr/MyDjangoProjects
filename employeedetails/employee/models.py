from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name=models.CharField(max_length=100,unique=True)
    department=models.CharField(max_length=80)
    salary=models.PositiveIntegerField()
    exp=models.PositiveIntegerField()


    def __str__(self):
        return self.emp_name

