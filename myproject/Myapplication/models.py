from django.db import models

# Create your models here.
# from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    item_name = models.CharField(max_length=50, null=False, blank=False)
    country_of_origin = models.CharField(max_length=50, null=False, blank=False)  # Changed to CharField
    total_quantity = models.IntegerField(default=0,null=False, blank=False)
    issued_quantity = models.IntegerField(default=0,null=False, blank=False)
    received_quantity = models.IntegerField(default=0,null=False, blank=False)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)  # Changed to DecimalField
    # receipt_no = models.CharField(max_length=10,default=0,null=False, blank=False)
    # part_number=models.IntegerField(null=False, blank=False)
    # receipt_number=models.IntegerField(null=False, blank=False) 

    def __str__(self):
        return self.item_name
    
class Sale(models.Model):
    item =models.ForeignKey(Product,on_delete=models.CASCADE, null=False, blank=False)
    quantity=models.IntegerField(null=False, blank=False)
    amount_received = models.IntegerField(null=False, blank=False)
    issued_to =models.CharField(max_length =100,null =False,blank =False)
    unit_price =models.DecimalField (max_digits=10, decimal_places=2, null=False, blank=False)
    branch_name =models.CharField(max_length=50, null=False, blank=False)
    
    def get_total(self):
        total = self.quantity *self.item.unit_price
        return int(total)
    def get_change(self):
        change = self.get_total()-self.amount_received
        return abs(int(change))

    def __str__ (self):
            
        return self.item.item_name
    