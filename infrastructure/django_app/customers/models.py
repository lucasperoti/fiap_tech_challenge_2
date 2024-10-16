from django.db import models


class Customer(models.Model):
    cpf = models.CharField(max_length=14, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name or "Cliente Anônimo"