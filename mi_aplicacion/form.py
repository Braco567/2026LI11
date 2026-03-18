from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Row, Column

from mi_aplicacion.models import Alumno, Escuela, Maestro

class EscuelaForm(ModelForm):
    class Meta:
        model = Escuela
        fields = ["nombre", "siglas"]

class MaestroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        action_type = kwargs.pop('action_type', 'Alta')
        super(MaestroForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        if action_type == 'Eliminar':
            submit_text = 'Eliminar'
        elif action_type == 'Editar':
            submit_text = 'Actualizar'
        else:  # Alta
            submit_text = 'Guardar'
        
        self.helper.layout = Layout(
            Row(
                Column(Field('nombre'), css_class='from-group col-md-4 mb-0'),
                Column(Field('sexo'), css_class='from-group col-md-4 mb-0'),
                Column(Field('fecha_nacimiento'), css_class='from-group col-md-4 mb-0'),
                css_class='from-row'
            ),
            Row(
                
                
                Column(Field('escuela'), css_class='from-group col-md-12 mb-0'),
                css_class='from-row'
            ),
            Submit('submit', submit_text)
        )
    class Meta:
        model = Maestro
        fields = ["nombre", "escuela", "sexo", "fecha_nacimiento"]
        labels = {
            'nombre': 'Nombre del Maestro',
            'escuela': 'Escuela a la que pertenece',
            'sexo': 'sexo del maestro',
            'fecha_nacimiento': 'fecha de nacimiento del maestro'
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        }
class AlumnoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        action_type = kwargs.pop('action_type', 'Alta')
        super(AlumnoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        if action_type == 'Eliminar':
            submit_text = 'Eliminar'
        elif action_type == 'Editar':
            submit_text = 'Actualizar'
        else:  # Alta
            submit_text = 'Guardar'
        
        self.helper.layout = Layout(
            Row(
                Column(Field('nombre'), css_class='from-group col-md-4 mb-0'),
                Column(Field('sexo'), css_class='from-group col-md-4 mb-0'),
                Column(Field('fecha_nacimiento'), css_class='from-group col-md-4 mb-0'),
                css_class='from-row'
            ),
            Row(
                Column(Field('escuela'), css_class='from-group col-md-6 mb-0'),
                Column(Field('maestro'), css_class='from-group col-md-6 mb-0'),
                css_class='from-row'
            ),
            Submit('submit', submit_text)
        )
    class Meta: 
        model = Alumno
        fields = ["nombre", "escuela", "maestro", "sexo", "fecha_nacimiento"]
        labels = {
            'nombre': 'Nombre del Alumno',
            'escuela': 'Escuela a la que pertenece',
            'maestro': 'Maestro asignado',
            'sexo': 'sexo del alumno',
            'fecha_nacimiento': 'fecha de nacimiento del alumno'
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        }