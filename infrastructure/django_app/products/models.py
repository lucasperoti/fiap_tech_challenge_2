from django.db import models

from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('Lanche', 'Lanche'),
        ('Acompanhamento', 'Acompanhamento'),
        ('Bebida', 'Bebida'),
        ('Sobremesa', 'Sobremesa'),
    ]
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name