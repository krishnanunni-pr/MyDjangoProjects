from django.db import models
from datetime import date,timedelta
# Create your models here.

class Mobile(models.Model):
    mobile_name=models.CharField(max_length=60,unique=True)
    brand_name=models.CharField(max_length=60)
    price=models.PositiveIntegerField()
    copies=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.mobile_name


class Order(models.Model):
    edd=date.today()+timedelta(days=4)
    product=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    user=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    options = (
        ("delivered", "delivered"),
        ("intransit", "intransit"),
        ("cancelled", "cancelled"),
        ("ordered", "ordered")
    )

    status = models.CharField(max_length=30, choices=options, default="ordered")
    phone_number = models.CharField(max_length=20)
    exp_delivery_date = models.DateField(default=edd,null=True)