from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)   # EmailField is a built-in field type in Django for storing email addresses
    phone = models.CharField(max_length=20) 
    course = models.CharField(max_length=100)   # CharField is a built-in field type in Django for storing character strings
    address = models.TextField()                # TextField is a built-in field type in Django for storing large text
    date_created = models.DateTimeField(auto_now_add=True)  # DateTimeField is a built-in field type in Django for storing date and time    
    date_updated = models.DateTimeField(auto_now=True)      # auto_now_add=True automatically set the field to now when the object is first created
    
    def __str__(self):
        return self.name