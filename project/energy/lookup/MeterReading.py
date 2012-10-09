from redokes.database.Lookup import Lookup
from energy.models import MeterReading as MeterReadingModel
from django.db.models import Q
from datetime import datetime

class MeterReading(Lookup):
    
    def init_defaults(self):
        Lookup.init_defaults(self)
        self.model = MeterReadingModel
        self.fields = fields = [
            'id',
            'date_full',
            'kwh_reading',
            'kwh_usage',
            'unit__id',
            'unit__name',
        ];
        
    def filter_date_full(self, value):
        return Q(date_full=value)
    
    def filter_kwh_usage(self, value):
        return Q(kwh_usage=value)
    
    def filter_unit(self, value):
        return Q(unit__name=value)
