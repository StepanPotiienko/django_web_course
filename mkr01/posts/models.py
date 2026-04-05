from django.db import models


class Post(models.Model):
    text = models.TextField()
    date = models.DateField(null=True, blank=True)
    precipitation_probability = models.FloatField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.text[:50]
