from django.db import models

# Create your models here.
class contact(models.Model):
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    def __str__(self):
        return self.email


class Schedule(models.Model):
    email=models.EmailField()
    subject=models.CharField(max_length=196)
    message=models.TextField()
    
    def __str__(self):
        return self.email