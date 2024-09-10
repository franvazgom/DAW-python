from django.test import TestCase
from services.models import Order

class OrderModelTest(TestCase):
    
    def test_not_empty(self):
        order = Order(
            nombre = 'Francisco Vázquez', 
            direccion = '4 Pte 345', 
        	total = 2341.67, 
            correo = 'franvazgom@gmail.com' 
        )
        Order.save(order)
        orders = Order.objects.all()
        self.assertIs(len(orders) > 0, True)
        self.assertEqual(orders[0].nombre, 'Francisco Vázquez')

