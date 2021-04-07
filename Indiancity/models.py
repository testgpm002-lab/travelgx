from django.db import models
import jsonfield


# Create your models here.
class CityList(models.Model):
    CityName = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Rating = models.FloatField()
    url = models.URLField(max_length=200, null=True, blank=True)
    recommendation = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.CityName