from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="fine/imges", default="")

    def __str__(self):
        return self.product_name

class Inquiry(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=111)
    message = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name