from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from services.models import Service as Servicio

from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

class CartTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        #PATH_WEB_DRIVER = r'C:\Users\Francisco\Documents\Developer\ProyectosGit\chromeDriver\chromedriver-win64\chromedriver.exe'
        PATH_WEB_DRIVER =r'C:\Users\Francisco\Documents\Developer\ProyectosGit\chromeDriver\msedgedriver.exe'
        cls.service = Service(PATH_WEB_DRIVER)
        # cls.selenium = webdriver.Chrome(service=cls.service)
        cls.selenium = webdriver.Edge(service=cls.service)
        cls.selenium.set_window_size(1100, 1000)

        #Creación del usuario y asignación de privilegios
        user = User.objects.create_user(username='pepito', password='password')
        permissions = Permission.objects.filter(content_type__app_label = 'services',
                                                content_type__model='order',
                                                codename='can_edit_order')
        user.user_permissions.set(permissions)
        user.save()
        # Crear 10 servicios de pruebas para el carrito
        n_services = 10
        for id in range(n_services):
            Servicio.objects.create(
                title = f'Servicio {id}',
                subtitle = f'Subtitulo del servicio {id}',
                content = f'Contenido del servicio {id}',
                image = 'ruta de imagen',
                cost = 100.0
            )
    
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        return super().tearDownClass()
    
    def test_home_title(self):
        browser = self.selenium
        url = self.live_server_url
        browser.get(url + "/")
        time.sleep(1)
        self.assertIn('La Recova', browser.title)                
        time.sleep(3)

    def autentica(self):
        browser = self.selenium
        url = self.live_server_url
        browser.get(url + "/accounts/login/")
        user_name = browser.find_element(By.ID, 'id_username')
        password = browser.find_element(By.ID, 'id_password')
        btn_submit = browser.find_element(By.ID, 'btn_submit')

        user_name.send_keys('pepito')        
        password.send_keys('password')
        btn_submit.click()

    def test_cart(self):        
        self.autentica()    
        browser = self.selenium
        url = self.live_server_url
        browser.get(url + "/services/")
        btn_add_cart = browser.find_element(By.LINK_TEXT , 'Agregar al carrito')
        btn_add_cart.click()
        browser.get(url + "/services/")
        btn_cart = browser.find_element(By.ID , 'cart-badge')
        btn_cart.click()
        #Se verifica el total
        body = browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Total = $100.00', body.text)        
        btn_confirm = browser.find_element(By.LINK_TEXT , 'Confirmar pedido')
        btn_confirm.click()
        # Se llenan los datos del cliente
        name = browser.find_element(By.XPATH , '//*[@id="id_nombre"]')
        address = browser.find_element(By.XPATH , '//*[@id="id_direccion"]')
        email = browser.find_element(By.XPATH , '//*[@id="id_correo"]')
        name.send_keys('Pepito Guzmán')
        address.send_keys('4 Pooniente 987')
        email.send_keys('pepito@gmail.com')        
        form = browser.find_element(By.ID, 'formOrder') 
        time.sleep(2)
        form.submit()        
        body = browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Gracias por su compra', body.text)        
        
