from django import forms
from .models import Producto, Compra
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre','modelo','unidades','precio','detalles','marca')
        #En este código estamos importando el modelo Producto desde el archivo models.py y definiendo un formulario llamado ProductoForm que hereda de forms.ModelForm.
        #El atributo Meta se utiliza para especificar el modelo asociado al formulario y los campos que se deben incluir en el formulario. En este caso, estamos incluyendo los
        # campos nombre, descripcion, precio y cantidad del modelo Producto.
        #Cabe destacar que con forms.ModelForm no es necesario definir los campos del formulario manualmente, ya que Django genera automáticamente un campo para
        # cada campo del modelo especificado. También se pueden utilizar otros tipos de campos de formularios, como forms.CharField o forms.DecimalField, si se desea tener un mayor control sobre el formato de entrada de los datos.

class BusquedaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, required=True)
    class Meta:
        model = Producto
        fields = ('nombre'),
        #exclude =('modelo','unidades','precio','detalles','marca')

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        #La variable fields de la clase Meta indica que campos del modelo Compra
        #deben ser incluidos en el formulario.
        fields = ['unidades']

#class RegistroForm(UserCreationForm):
 #   email = forms.EmailField()

  #  error_messages = {
   #     'password_mismatch': 'Las contraseñas no coinciden',
    #    'invalid': 'Dirección de correo electrónico inválida',
    #}



class IniciarSesionForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))













#CLEANED_DATA:
#cleaned_data es un diccionario que contiene los datos que se han validado y
# limpiado mediante un formulario en Django. Cuando un formulario es válido,
# Django agrupa los datos que han sido validados y limpiados en el atributo cleaned_data.
#En el código que proporcionaste, form.cleaned_data['nombre'] es
#la forma en que se accede al valor del campo "nombre" después de que
#se ha validado y limpiado en el formulario BusquedaForm. Este valor
#se usa luego en la consulta para buscar productos cuyo nombre contenga ese valor.
#En Django, cuando se envía un formulario a través de un método POST,
# los datos ingresados por el usuario se almacenan en el atributo request.POST.
# Sin embargo, estos datos se almacenan en forma de diccionario y no están validados.
#Para acceder a los datos del formulario de manera validada y en un formato
# utilizable, Django proporciona el método cleaned_data().
# Este método valida los datos y devuelve un diccionario de
# datos limpios que se puede usar para procesar el formulario.


#REQUEST POST:
#request.POST es un diccionario-like object que contiene
# los datos enviados en una petición HTTP con el método POST.
# En Django, cuando se envía un formulario con el método POST,
# los datos enviados se almacenan en este diccionario-like object.
#Por ejemplo, si en un formulario se tiene un campo llamado nombre,
# cuando se envía el formulario, request.POST['nombre'] devolverá
# el valor del campo nombre que se haya ingresado en el formulario.
#Es importante mencionar que request.POST solo estará disponible
# si la petición HTTP que se está procesando tiene el método POST.
# Si la petición tiene otro método (como GET, PUT, DELETE),
# entonces se usará request.GET, request.PUT, request.DELETE, respectivamente.