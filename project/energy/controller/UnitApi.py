from redokes.controller.Crud import Crud
from energy.models import Unit as UnitModel
from energy.lookup.Unit import Unit as UnitLookup
from energy.form.Unit import Unit as UnitForm

class UnitApi(Crud):
    
    def init_defaults(self):
        Crud.init_defaults(self)
        self.access = None
        self.model_class = UnitModel
        self.lookup_class = UnitLookup
        self.form_class = UnitForm
        self.access_module = None
        self.access_model = None
    
    