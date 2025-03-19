from django.db import models

# Create your models here.

options = [

    ('action', 'action'),
    ('cartoon', 'cartoon'),
]

class MovieData(models.Model):


    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(choices=options, max_length=20)

    def __str__(self):
        return self.name
