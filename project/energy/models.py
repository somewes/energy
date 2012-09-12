from django.db import models
from django.utils import timezone

#from datetime import datetime
#from django.core.cache import cache
#from django.db.models import Q
#from django.template.defaultfilters import slugify
#from django.template.loader import render_to_string
#from bs4 import BeautifulSoup
#import json
#from django.conf import settings
#from haystack.query import SearchQuerySet
#from django.utils.encoding import force_unicode

class Unit(models.Model):
    
    def __unicode__(self):
        return self.name
    
    name = models.CharField(
        max_length=200,
        db_index = True
    )
    
    latitude = models.DecimalField(
        max_digits=20,
        decimal_places=17,
        db_index = True,
        null = True,
        default = 0,
        blank = True,
    )
    
    longitude = models.DecimalField(
        max_digits=20,
        decimal_places=17,
        db_index = True,
        null = True,
        default = 0,
        blank = True,
    )
    
    zip_code = models.IntegerField(
        db_index = True
    )

class MeterReading(models.Model):
    
    unit = models.ForeignKey('Unit', db_index = True, null=False)
    
    timestamp = models.DateTimeField(
        null=True,
        blank=True,
        default=timezone.now,
        db_index = True
    )
    
    kWh = models.DecimalField(
        max_digits=20,
        decimal_places=10,
        db_index = True
    )

class Circuit(models.Model):
    
    name = models.CharField(
        max_length=200,
        db_index = True
    )
    
    unit = models.ForeignKey('Unit', db_index = True, null=False)
    
    voltage = models.DecimalField(
        max_digits=20,
        decimal_places=10,
        db_index = True
    )
    
class CircuitReading(models.Model):
    
    circuit = models.ForeignKey('Circuit', db_index = True, null=False)
    
    timestamp = models.DateTimeField(
        null=True,
        blank=True,
        default=timezone.now,
        db_index = True
    )
    
    amps = models.DecimalField(
        max_digits=20,
        decimal_places=10,
        db_index = True
    )
    
class Weather(models.Model):
    
    zip_code = models.IntegerField(
        db_index = True
    )
    
    timestamp = models.DateTimeField(
        null=True,
        blank=True,
        default=timezone.now,
        db_index = True
    )
    
    temperature = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        db_index = True
    )
    
class Forecast(models.Model):
    
    zip_code = models.IntegerField(
        db_index = True
    )
    
    timestamp = models.DateTimeField(
        null=True,
        blank=True,
        default=timezone.now,
        db_index = True
    )
    
    temperature = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        db_index = True
    )
    
