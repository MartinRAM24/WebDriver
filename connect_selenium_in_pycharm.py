from selenium import webdriver
import time

# Inicializar el controlador
driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

# Agregar una espera
time.sleep(5)

# Cerrar el navegador
driver.quit()
