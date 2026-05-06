from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title if self.title else "Untitled"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

class Measurement(models.Model):
    text = models.TextField()
    date = models.DateField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    precipitation_probability = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.text[:50]

    def get_absolute_url(self):
        return reverse("measurement_detail", kwargs={"pk": self.pk})
