from django.db import models

class Airport(models.Model):
    iata_code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=255)
    latitude =models.FloatField()
    longitude =models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.iata_code})"
    