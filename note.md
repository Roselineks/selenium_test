
# test pour chercher un input (barre de recherche ..)

# from selenium import webdriver
#from selenium.webdriver.common.by import By
import time

#driver = webdriver.Chrome()
#driver.get("https://www.cdiscount.com")
#time.sleep(30)
#input = driver.find_element(By.NAME, "search")
#input.clear()
#input.send_keys("television hd")

#preuve que mon test a bien fonctionné

#driver.get_screenshot_as_file("input.png")

#correction+++

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configuration du WebDriver
#options = Options()
#options.add_argument("--start-maximized")  # Pour maximiser la fenêtre du navigateur
#service = Service('path/to/chromedriver')  # Remplacez par le chemin de votre chromedriver

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

time.sleep(20)

input = driver.find_element(By.NAME, "search")
input.clear()
input.send_keys("television hd")

# Preuve que mon test a bien fonctionné
driver.get_screenshot_as_file("input.png")

# Fermer le navigateur
driver.quit()


# ce qui fonctionne ok
# test pour chercher un input (barre de recherche  television hd..)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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

# Preuve que mon test a bien fonctionné
driver.get_screenshot_as_file("input3.png")

# Fermer le navigateur
driver.quit()




