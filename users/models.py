from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    address=models.TextField(max_length=200)
    temperature=models.DecimalField(max_digits=5, decimal_places=2)
    oxygen_saturation=models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
    
