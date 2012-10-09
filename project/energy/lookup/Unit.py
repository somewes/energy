from redokes.database.Lookup import Lookup
from energy.models import Unit as UnitModel
from energy.lookup.MeterReading import MeterReading as MeterReadingLookup

from django.db.models import Q
from datetime import datetime

class Unit(Lookup):
    
    def init_defaults(self):
        Lookup.init_defaults(self)
        self.model = UnitModel
        self.fields = fields = [
            "id",
            "name",
            "zip_code",
        ];
        
        self.add_mapped_lookup('meter_readings', MeterReadingLookup, 'unit__id')
        
    def filter_name(self, value):
        return Q(name=value)
    
    def filter_zip_code(self, value):
        return Q(zip_code=value)
    
