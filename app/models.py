from django.db import models

# Create your models here.
class Signup(models.Model):
    first_name = models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    email = models.EmailField(max_length=70)
    username= models.CharField(max_length=500)
    address=models.CharField(max_length=2000)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=300)
    pincode= models.CharField(max_length=200)
    profile_pic=models.ImageField(null=True,blank=True,upload_to='static/images')
    signup_as=models.CharField(max_length=100)
    password1=models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)



    def __str__(self):
        return self.email
