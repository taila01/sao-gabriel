from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name


from django.db import models

class Users(models.Model):
    id_users = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    birth = models.CharField(max_length=8)
    cpf = models.IntegerField()
    telephone = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    
    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.name
