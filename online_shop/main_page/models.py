from django.db import models

# Create your models here.

class Sales(models.Model):
    text = models.CharField(max_length=32)
    phone_number = models.CharField(max_length=9)
    created_at = models.DateTimeField(auto_now_add=False)

def __str__(self):
    return f'{self.text},{self.phone_number}'

