from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('recruiter', 'Recruiter'),
        ('seeker', 'Seeker'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES,null=True)
    display_name = models.CharField(max_length=150,null=True)
    def __str__(self):
        return self.username
    
class RecruiterProfile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="Recruiter_Profile")
    profile_pic=models.ImageField(upload_to="static/Midea/user_profile",null=True)
    bio=models.TextField(max_length=300,null=True)
    contract_number=models.CharField(max_length=13,null=True)
    def __str__(self):
        return f"{self.user.username}"

class SeekerProfile(models.Model):
    chos_skill = [
        ('programing', 'Programing'),
        ('networking', 'Networking'),
        ('hadworking', 'Hadworking'),
        ('acounting', 'Acounting')
    ]
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="Seeker_Profile")
    profile_pic=models.ImageField(upload_to="static/Midea/user_profile",null=True)
    skill=models.CharField(choices=chos_skill,max_length=100,null=True)
    web_site=models.URLField(max_length=300,null=True)
    contract_number=models.CharField(max_length=13,null=True)
    def __str__(self):
        return f"{self.user.username}"
