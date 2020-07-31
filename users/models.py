from django.db import models

# Create your models here.

class UserProfile(models.Model):
    Name = models.CharField(max_length=20)
    DOB = models.DateField()
    Address = models.TextField()
    Aadhar = models.BigIntegerField()
    Date = models.DateField()
    Time = models.TimeField()
    Temp = models.DecimalField(max_digits=5, decimal_places=2)
    SpO2 = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['Name']
