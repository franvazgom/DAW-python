from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class SeleniumTest(StaticLiveServerTestCase):
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
    
    def test_google(self):
        browser = self.selenium
        browser.get("http://google.com")
        time.sleep(1)
        self.assertIn('Google', browser.title)
        cajita = browser.find_element(By.ID, 'APjFqb')
        cajita.send_keys("PERROS GIGANTES")
        time.sleep(1)
        cajita.submit()
        time.sleep(2)

