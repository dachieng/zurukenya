from django.db import models
from django.utils import timezone


class Trips(models.Model):
    image = models.ImageField(upload_to="pics")
    title = models.CharField(max_length=100)
    startDate = models.DateTimeField(default=timezone.now)
    destination1 = models.CharField(max_length=100)
    destination2 = models.CharField(max_length=100)
    destination3 = models.CharField(max_length=100)
    destination4 = models.CharField(max_length=100, null=True)
    destination5 = models.CharField(max_length=100, null=True)
    duration = models.IntegerField()
    amount = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.title
