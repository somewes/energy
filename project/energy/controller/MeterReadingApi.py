from redokes.controller.Crud import Crud
from energy.models import MeterReading as MeterReadingModel
from energy.lookup.MeterReading import MeterReading as MeterReadingLookup

class MeterReadingApi(Crud):
    
    def init_defaults(self):
        Crud.init_defaults(self)
        self.access = None
        self.model_class = MeterReadingModel
        self.lookup_class = MeterReadingLookup
        self.form_class = None
        self.access_module = None
        self.access_model = None
		# test this commit
    