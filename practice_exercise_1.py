from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "email")))

# Inicia sesion
WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, "email"))).send_keys("ketzaypayola@gmail.com")

WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, "password"))).send_keys("Mar241198")

WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".auth-form__button"))).click()

# Agregar una espera explícita para que se cargue la página
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))

# Hacer clic en la foto de perfil
driver.find_element(By.CSS_SELECTOR, ".profile__image").click()

# Insertar el enlace a la foto en el campo Enlace utilizando la variable avatar_url
avatar_url = "https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-7/avatarSelenium.png"
driver.find_element(By.ID, "owner-avatar").send_keys(avatar_url)

# Guardar la nueva foto
driver.find_element(By.XPATH, ".//form[@name='edit-avatar']/button[text()='Guardar']").click()
WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, ".profile__image"),"style",avatar_url))

# Guardar el valor del atributo de estilo para el elemento de foto de perfil en la variable style
style = driver.find_element(By.CSS_SELECTOR, ".profile__image").get_attribute("style")
# Comprobar que style contiene el enlace a la foto de perfil
assert avatar_url in style, f"style={style}"

driver.quit()
