from redokes.controller.Stats import Stats
from energy.models import MeterReading as MeterReadingModel
from energy.lookup.MeterReading import MeterReading as MeterReadingLookup
from django.db.models import Avg
from django.db.models import Count
from django.db.models import Max
from django.forms import model_to_dict

class MeterReadingStats(Stats):
    
    def init_defaults(self):
        Stats.init_defaults(self)
        self.model = MeterReadingModel
        self.date_field = 'timestamp'
        self.aggregate_field = 'kwh_usage'
        
    def index_action(self):
        self.extra = {
            'day': 'DAY(timestamp)',
            'month': 'MONTH(timestamp)',
            'year': 'YEAR(timestamp)',
        }
        
        aggregate_function = 'count'
        if self.aggregate_function == 'avg':
            aggregate_function = 'avg'
#        rows = self.model.objects.extra(self.extra).values(*self.values).order_by(*self.order_by).annotate(value=Count(self.aggregate_field))
        rows = self.model.objects.extra(self.extra).aggregate(Avg('kwh_usage'))
        print rows
        
        rows = self.model.objects.values('unit', 'date_day', 'date_month', 'date_year').annotate(average_kwh_usage=Avg('kwh_usage')).order_by('date_year', 'date_month', 'date_day')
        print rows
        return
        for row in rows:
            dict = model_to_dict(row)
            print dict
            
        
    