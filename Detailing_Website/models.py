from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=100)

    email=models.EmailField()

    phone=models.CharField(max_length=15)

    service=models.CharField(max_length=100)

    message=models.TextField()

    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Booking(models.Model):

    VEHICLE_CHOICES = [
        ('car','car'),
        ('Bike','Bike'),
    ]

    SERVICE_CHOICES = [
        ('Car Detailing','Car Detailing'),
        ('Bike Detailing', 'Bike Detailing'),
        ('Wheel & Tyres', 'Wheel & Tyres'),
        ('Custom Wraps & Graphics', 'Custom Wraps & Graphics'),
        ('Custom Builds', 'Custom Builds'),
        ('Performance Upgrades', 'Performance Upgrades'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    vehicle = models.CharField(
        max_length=10,
        choices=VEHICLE_CHOICES
    )

    service = models.CharField(
        max_length=100,
        choices=SERVICE_CHOICES
    )

    date = models.DateField()
    time = models.CharField(max_length=20)

    message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.service}"