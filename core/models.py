from django.db import models

# Create your models here.

class Sections(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=700,null=True, blank= True)
    
    def __str__(self):
        return self.name
    
    
    
    
from django.db import models

class PatientRequest(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=15)
    GENDER_CHOICES = [
        ('male', 'ذكر'),
        ('female', 'أنثى'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    symptoms = models.TextField()

    def __str__(self):
        return self.name

