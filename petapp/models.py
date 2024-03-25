from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    desc=models.TextField(max_length=200)
    phone=models.IntegerField()


    def __str__(self):
        return self.name
    

class Product(models.Model):
    Product_ID=models.AutoField
    Product_Name=models.CharField( max_length=50)
    Product_Category=models.CharField(max_length=50 ,default="")
    Product_SubCategory=models.CharField(max_length=50)
    Product_Price=models.IntegerField(default=0)
    Product_Desc=models.CharField(max_length=300)
    Product_Image=models.ImageField(upload_to='images/image', height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.Product_Name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address1= models.CharField(max_length=255)
    address2= models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    payment_details = models.TextField()
    phone = models.CharField(max_length=20)

    def _str_(self):
        return self.order_id
    
class orderupdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField()
    update_desc=models.CharField(max_length=50)
    deliverd=models.BooleanField()
    time_stamp=models.DateField()

    def _str_(self):
        return self.update_id