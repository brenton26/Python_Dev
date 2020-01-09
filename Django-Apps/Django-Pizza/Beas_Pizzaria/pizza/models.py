from django.db import models

# Create your models here.
class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self, test):
        return self.title

class Pizza(models.Model):
    topping1 = 

