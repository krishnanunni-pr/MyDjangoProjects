from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_name=models.CharField(max_length=100,unique=True)
    departments=models.CharField(max_length=80)
    salary=models.PositiveIntegerField()
    exp=models.PositiveIntegerField()


    def __str__(self):
        return self.emp_name



# employee=Employee(emp_name="arun",dptmt="Hr",salary=50000,exp=2)
# employee.save()
