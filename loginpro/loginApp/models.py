from django.db import models

# Create your models here.
class covid_data(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    carona_status = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    def __str__(self):
        return self.name