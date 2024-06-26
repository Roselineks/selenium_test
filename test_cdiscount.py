
# test pour chercher un input (barre de recherche  television hd..)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome ()

driver.get("https://www.cdiscount.com")

time.sleep(10)

# Attendre que le pop-up de consentement apparaisse et accepter les cookies
try:
    # Ajustez le sélecteur en fonction de la structure HTML du site
    accept_cookies_button = driver.find_element(By.ID, "footer_tc_privacy_button_3")  # Exemple d'ID, à ajuster
    accept_cookies_button.click()
    print("Cookies accepted.")
except Exception as e:
    print(f"Cookies pop-up not found or another error occurred: {e}")

#time.sleep(20)

input = driver.find_element(By.NAME, "search")
input.clear()
input.send_keys("television hd")
input.send_keys(Keys.ENTER)
# Preuve que mon test a bien fonctionné
driver.get_screenshot_as_file("input4.png")



#recuperer le prix d'un element

prix_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id=\"lpBloc\"]/li[1]/div[2]/div[3]/div[1]/div/div[2]/span"))
  )
prix = prix_element.text
print(prix)

time.sleep(25)

# Fermer le navigateur
driver.quit()