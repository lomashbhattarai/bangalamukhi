from django.db import models

class Item(models.Model):
    name= models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/',null=True,blank=True )
    marked_price = models.IntegerField(null=True)
    cost_price = models.IntegerField(null=True,blank=True)
    buy_date = models.DateTimeField(null=True,blank=True)
    sold_date = models.DateTimeField(null=True,blank=True)
    description = models.CharField(max_length=10000,null=True,blank=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name= models.CharField(max_length=30)
    delivery_address = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Trans(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE,related_name ="trans")
    customer= models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="trans")
    no_of_items = models.IntegerField(null=True)

    def __str__(self):
        return self.item
