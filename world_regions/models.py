from django.db import models
from django_countries.fields import CountryField


class Region(models.Model):
    name = models.CharField(max_length=25)
    code = models.CharField(max_length=3)

    def __unicode__(self):
        return self.name


class RegionCountry(models.Model):
    country = CountryField(unique=True)
    region = models.ForeignKey(Region, related_name="countries")
