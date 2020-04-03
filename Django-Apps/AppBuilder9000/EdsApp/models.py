from django.db import models


# Animal class
class Animal(models.Model):
    animals = models.Manager()
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    class Meta:
        ordering = ['name']


# Dog class
class Dog(Animal):
    dogs = models.Manager()
    breed = models.CharField(max_length=20)
    HAIR_TYPES = [('short hair', 'short hair'),
                  ('long hair', 'long hair'),
                  ('curly hair', 'curly hair'), ]
    hair = models.CharField(max_length=20, choices=HAIR_TYPES)
    favorite_dog_park = models.CharField(max_length=50)

    def __Str__(self):
        return self.name


# Cat class
class Cat(Animal):
    cats = models.Manager()
    breed = models.CharField(max_length=20)
    HAIR_TYPES = [('short hair', 'short hair'),
                  ('long hair', 'long hair'), ]
    hair = models.CharField(max_length=20, choices=HAIR_TYPES)

    def __Str__(self):
        return self.name


# Dragon class
class Dragon(Animal):
    dragons = models.Manager()
    fire_breathing = models.BooleanField()
    COLOR = {('black', 'black'),
             ('red', 'red'),
             ('green', 'green'),
             ('brown', 'brown'),
             ('yellow', 'yellow'), }

    def __Str__(self):
        return self.name
