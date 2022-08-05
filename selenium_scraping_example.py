#Librerias
from selenium import webdriver 
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import by
import time
import pandas as pandas

# Opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver_path = '/home/elias/Público/Descargas/Programa/chromedriver'
driver = webdriver.Chrome(driver_path,chrome_options=options)

# Iniciaria en la pantalla 2
driver.set_window_position(2000,0)
driver.maximize_window()
time.sleep(1)

# Inicializamos el navegador 
driver.get('https://www.meteored.com.ar')


