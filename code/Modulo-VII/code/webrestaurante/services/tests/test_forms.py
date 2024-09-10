from django.test import TestCase
from services.forms import OrderForm

class OrderFormTest(TestCase):
    def test_title_label(self):
        form = OrderForm()
        self.assertTrue(form.fields['nombre'].label == 'Nombre')
        
    def test_complete_fields(self):
        data = {
            'nombre':'Francisco Vázquez',
            'direccion':'4 Pte 765',
            'total':234.23, 
            'correo':'fran@gmail.com'
        }
        form = OrderForm(data)
        self.assertTrue(form.is_valid())

    def test_incomplete_fields(self):
        data = {
            # nombre debe ser obligatorio
            'direccion':'4 Pte 765',
            'total':234.23, 
            'correo':'fran@gmail.com'
        }
        form = OrderForm(data)
        self.assertFalse(form.is_valid())