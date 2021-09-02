from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=100,unique=True,blank=True)
    author=models.CharField(max_length=80)
    price=models.PositiveIntegerField()
    copies=models.PositiveIntegerField()
    


    def __str__(self):
        return self.book_name



#book=Book(book_name="11 minutes",author="paulo",price=250,copies=200)
#book.save()

#books=Book.objects.all()


# orm query for fetching a specific record
#   reference_name= model_name.objects.get(filed_name=value)
#book=Book.objects.get(id=1)


# orm query for updating a specific record
# book=Book.objets.get(id=1)
# book.price=250
# book.save


class Order(models.Model):

    product=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    options=(
        ("delivered","delivered"),
        ("intransit","intransit"),
        ("cancelled","cancelled"),
        ("ordered","ordered")
    )

    status=models.CharField(max_length=20,choices=options,default="ordered")
    phone_number=models.CharField(max_length=20)
    exp_delivery_date=models.DateField(null=True)