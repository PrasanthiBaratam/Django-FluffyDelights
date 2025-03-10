from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    pic = models.ImageField(upload_to='products/',null = True,blank = True)  # Ensure this line exists


    def __str__(self):
        return self.name


# Create your models here.
