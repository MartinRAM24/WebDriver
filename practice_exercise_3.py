from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "email")))

# Inicia sesión
WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, "email"))).send_keys("ketzaypayola@gmail.com")

WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, "password"))).send_keys("Mar241198")

WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "auth-form__button"))).click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".places__list")))

# Buscar la tarjeta y desplazarla a la vista
element = driver.find_element(By.CSS_SELECTOR, ".places__item")
driver.execute_script("arguments[0].scrollIntoView();", element)

driver.quit()
