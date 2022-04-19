from django.db import models

# Create your models here.

class Inquiry(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    comments = models.TextField()

def __str__(self):
        return self.email