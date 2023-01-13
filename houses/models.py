from django.db import models

# Create your models here.
class House(models.Model):
    """House model"""
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(
        verbose_name='Price per night',
        help_text='Price per night in USD'
    )
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        default=True,
        help_text='Check if pets are allowed',
        verbose_name='Pets allowed'
        ) 

    def __str__(self):
        return self.name