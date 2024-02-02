from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
driver = webdriver.Remote("http://selenium:4444/wd/hub", options=options)
driver.get('https://www.youtube.com/@raily')

reject_button = driver.find_element(By.XPATH, "//button[span[text()='Reject all']]")
reject_button.click()

channel_username = driver.find_element(By.ID, 'text').text

# driver.get('https://www.youtube.com/@adorplayer')


