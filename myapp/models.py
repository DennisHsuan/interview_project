from django.db import models
#新增django.user模組
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ProductModel(models.Model):
    pname = models.CharField(max_length=30, null=False)
    pprice = models.IntegerField(null=False)
    pimage = models.CharField(max_length=40, null=False)
    pdescription = models.TextField(null = False)

class User(AbstractUser):#使用django內鍵新增帳號，來增加需要的欄位
    cBirthday = models.DateField(null=True)
    cPhone = models.CharField(max_length=10) 