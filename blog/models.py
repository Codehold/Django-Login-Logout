from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save




class Profile(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE,related_name="salman",null=True )
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone_No = models.CharField(max_length=20)
    cnic = models.CharField(max_length=20)
    plot_No = models.CharField(max_length=100 , blank=True,null=True)
    total_price = models.IntegerField()
    created_date = models.DateTimeField()

    class Meta:
        ordering = ['-created_date']


    def __str__(self):
        return self.name




class Installament(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    installament_fees = models.IntegerField()
    date = models.DateTimeField() 


    class Meta:
        ordering = ['-date']


    def __str__(self):
        return str(self.user)
