
from django.forms import ModelForm, TextInput
from app.models import CitiesModel

class CitiesForm(ModelForm):

    class Meta:
        model = CitiesModel
        fields = '__all__'
