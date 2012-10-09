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
    
    def __unicode__(self):
        return '{0} - {1} {2}'.format(self.unit, self.date_full, self.kwh_usage)
    
    unit = models.ForeignKey('Unit', db_index = True, null=False)
    
    date_full = models.DateTimeField(
        null=True,
        blank=True,
        default=timezone.now,
        db_index = True
    )
    
    date_month = models.IntegerField(
        db_index = True,
        blank = True,
    )
    
    date_day = models.IntegerField(
        db_index = True,
        blank = True,
    )
    
    date_year = models.IntegerField(
        db_index = True,
        blank = True,
    )
    
    date_hour = models.IntegerField(
        db_index = True,
        blank = True,
    )
    
    date_minute = models.IntegerField(
        db_index = True,
        blank = True,
    )
    
    date_second = models.IntegerField(
        db_index = True,
        blank = True,
    )
    
    kwh_reading = models.DecimalField(
        max_digits=20,
        decimal_places=10,
        db_index = True
    )
    
    kwh_usage = models.DecimalField(
        max_digits=20,
        decimal_places=10,
        db_index = True,
        blank = True,
    )
    
    #overwrite the save method to do extra processing
    def save(self, *args, **kwargs):
        self.date_month = self.date_full.month
        self.date_day = self.date_full.day
        self.date_year = self.date_full.year
        self.date_hour = self.date_full.hour
        self.date_minute = self.date_full.minute
        self.date_second = self.date_full.second
        
        # get the usage of the previous reading
        records = MeterReading.objects.filter(unit=self.unit, date_full__lt=self.date_full).order_by('-date_full')
        if records.count():
            previous_record = records[0]
            self.kwh_usage = self.kwh_reading - previous_record.kwh_reading
        else:
            self.kwh_usage = 0
        
        super(MeterReading, self).save(*args, **kwargs)
        
        # update next record if it exist
        records = MeterReading.objects.filter(unit=self.unit, date_full__gt=self.date_full).order_by('date_full')
        if records.count():
            next_record = records[0]
            next_record.save()

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
    
