from django.db import models

# Create your models here.


class UserInformation(models.Model):
    Full_Name = models.CharField(max_length = 50)
    Address = models.CharField(max_length = 100)
    Owner_info = models.CharField(max_length = 100)
    Employee_size = models.IntegerField()