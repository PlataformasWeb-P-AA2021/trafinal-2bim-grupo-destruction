from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Persona, Barrio, Casa, Departamento

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = '__all__'

class CasaForm(ModelForm):
    class Meta:
        model = Casa
        fields = '__all__'

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

# class DepartamentoEdificioForm(ModelForm):

#     def __init__(self, edificio, *args, **kwargs):
#         super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
#         self.initial['edificio'] = edificio
#         self.fields["edificio"].widget = forms.widgets.HiddenInput()
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'

#     class Meta:
#         model = Departamento
#         fields = ['nombre_propietario', 'costo', 'num_cuartos', 'edificio']

