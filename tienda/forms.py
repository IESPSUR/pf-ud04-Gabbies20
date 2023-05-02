from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre','modelo','unidades','precio','detalles','marca')


        """
        En este código estamos importando el modelo Producto desde el archivo models.py y definiendo un formulario llamado ProductoForm que hereda de forms.ModelForm.

El atributo Meta se utiliza para especificar el modelo asociado al formulario y los campos que se deben incluir en el formulario. En este caso, estamos incluyendo los campos nombre, descripcion, precio y cantidad del modelo Producto.

Cabe destacar que con forms.ModelForm no es necesario definir los campos del formulario manualmente, ya que Django genera automáticamente un campo para cada campo del modelo especificado. También se pueden utilizar otros tipos de campos de formularios, como forms.CharField o forms.DecimalField, si se desea tener un mayor control sobre el formato de entrada de los datos.
        """