from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2,max_digits=10)

    def __str__(self):
        return self.title