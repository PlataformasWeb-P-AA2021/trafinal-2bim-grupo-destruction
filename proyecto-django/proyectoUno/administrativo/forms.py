from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Persona, Barrio, Casa, Departamento

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

    # Agregar clases de Bootstrap en el formulario.
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = '__all__'

    # Agregar clases de Bootstrap en el formulario.
    def __init__(self, *args, **kwargs):
        super(BarrioForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CasaForm(ModelForm):
    class Meta:
        model = Casa
        fields = '__all__'
        labels = {
            'num_cuartos': _('Número de cuartos'),
            'num_pisos': _('Número de pisos'),
            'valor': _('Valor de bien'),
            'color': _('Color de inmueble'),
        }

    # Agregar clases de Bootstrap en el formulario.
    def __init__(self, *args, **kwargs):
        super(CasaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'
        labels = {
            'num_cuartos': _('Número de cuartos'),
            'valor': _('Valor de bien'),
        }

    # Agregar clases de Bootstrap en el formulario.
    def __init__(self, *args, **kwargs):
        super(DepartamentoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
