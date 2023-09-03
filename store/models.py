from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.cat_name

class product(models.Model):
    name = models.CharField(max_length=100, default='')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.CharField(max_length=50, default='')
    description = models.TextField()


    def __str__(self):
        return self.name
    def summary(self):
        return self.description[:40]

class Cart(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=10, default='')
    def __str__(self):
        return self.product.name

# class Customer(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=20)
#     address = models.TextField()

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"
class Order(models.Model):
    name = models.CharField(max_length=100, default='')
    address = models.TextField(default='')

    def __str__(self):
        return f"{self.name}"
