from django.db import models

# Create your models here.

class Mobile(models.Model):
    mobile_name=models.CharField(max_length=60,unique=True)
    brand_name=models.CharField(max_length=60)
    price=models.PositiveIntegerField()
    copies=models.PositiveIntegerField()


    def __str__(self):
        return self.mobile_name


class Order(models.Model):
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
    exp_delivery_date = models.DateField(null=True)