# test pour chercher un input (barre de recherche exp : roseline ..)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

input = driver.find_element(By.NAME, "no_type")
input.clear()
input.send_keys("Roseline")

time.sleep(30)

#preuve que mon test a bien fonctionné

driver.get_screenshot_as_file("input.png")
