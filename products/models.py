from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    CATEGORY_CHOICES = (
        ("F", "Food"),
        ("E", "ElectronicProducts"),
        ("C", "Clothing"),
        ("O", "Other"),
    )

    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.ImageField(blank=True)
    content = models.TextField()
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)


    def __str__(self):
        return self.name