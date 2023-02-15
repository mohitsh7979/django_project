from django.db import models

# Create your models here.


class Farmer(models.Model):
    name=models.CharField(max_length=30)
    Father_name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    village=models.CharField(max_length=30)
    mobile_no=models.IntegerField()



