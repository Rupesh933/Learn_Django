from django.db import models

# Create your models here.

class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    emial_address = models.EmailField(unique=True)
    designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, blank=True)  # blank means phone number will be optional
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)