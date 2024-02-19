from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

input("")

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.alphacyprus.com.cy/live")

cookies = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cookiescript_accept")))
cookies.click()

#video_element = driver.find_element(By.ID, "rmpPlayer")
video_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "rmpPlayer")))
button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="rmp-fullscreen rmp-button rmp-i rmp-i-resize-full"]')))
#button = driver.find_element(By.CSS_SELECTOR, 'button[class="rmp-fullscreen rmp-button rmp-i rmp-i-resize-full"]')
#button2 = driver.find_element(By.CSS_SELECTOR, 'button[class="rmp-button rmp-volume rmp-i rmp-i-off-volume"]')
button2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[class="rmp-button rmp-volume rmp-i rmp-i-off-volume"]')))

actions = ActionChains(driver)

actions.move_to_element(button2).perform()
time.sleep(1)
volume = driver.find_element(By.CSS_SELECTOR, 'div[class="rmp-volume-indicator rmp-color-bg"]')
volume = re.search(r'\d+', volume.text).group(0)
if int(volume) == 0:
    button2.click()


actions.move_to_element(video_element).perform()
button.click()


time.sleep(100)
input("")
