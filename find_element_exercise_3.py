from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

time.sleep(5)

# Buscar elementos
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")

# Probar el atributo placeholder para cada elemento
assert email.get_attribute('placeholder') == "Correo electrónico", f"Expected 'Correo electrónico', but got: '{email.get_attribute('placeholder')}'"
assert password.get_attribute('placeholder') == "Contraseña", f"Expected 'Contraseña' but got: '{password.get_attribute('placeholder')}'"

print("pruebas exitosas!")
# Cerrar el navegador
driver.quit()
