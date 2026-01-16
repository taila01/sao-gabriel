
from django.db import models
from app_admin.models import Users

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.FloatField() 
    fk_category_id = models.IntegerField()

    class Meta:
        managed = False 
        db_table = 'product'

    def __str__(self):
        return self.name

class Store(models.Model):
    id_store = models.AutoField(primary_key=True)
    fk_users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    qt_product = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'store'