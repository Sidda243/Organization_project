from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Organization(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    Company=models.CharField(max_length=100,primary_key=True)
    Image=models.ImageField()
    Discription=models.TextField()
    Founder=models.CharField(max_length=100)
    Established_On=models.DateField()
    Company_Type=models.CharField(max_length=100)
    Profit=models.IntegerField()
    Projects=models.TextField()
