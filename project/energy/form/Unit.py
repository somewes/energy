from django.forms import ModelForm
from energy.models import Unit as UnitModel

class Unit(ModelForm):
    post = None
    class Meta:
        model = UnitModel
#        exclude = (
#            'id',
#            'slug',
#            'description',
#            'color',
#            'feature_template',
#            'story_template',
#            'created_at',
#        )