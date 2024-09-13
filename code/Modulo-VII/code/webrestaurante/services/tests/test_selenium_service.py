from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SeleniumServiceTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        PATH_WEB_DRIVER = r'C:\Users\Francisco\Documents\Developer\ProyectosGit\chromeDriver\chromedriver-win64\chromedriver.exe'
        cls.service = Service(PATH_WEB_DRIVER)
        cls.selenium = webdriver.Chrome(service=cls.service)
        cls.selenium.set_window_size(1100, 1000)
    
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

