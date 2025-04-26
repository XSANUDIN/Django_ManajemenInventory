"""""""""
A11.2022.14795
NUR IKHSANUDIN

"""""""""

from django.db import models

# Create your models here.

# Admin Model

class Admin(models.Model):
    username = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

# Category Model

class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='categories', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Supplier Model

class Supplier(models.Model):
    name = models.CharField(max_length=100, null=False)
    contact_info = models.CharField(max_length=100, blank=True)
    created_by = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='suppliers', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Item Model

class Item(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    quantity = models.IntegerField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items', null=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='items', null=False)
    created_by = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='items', null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
