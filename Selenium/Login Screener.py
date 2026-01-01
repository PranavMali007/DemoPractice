import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://www.screener.in/")
# driver.find_element(By.XPATH,"//a[@class='button account']").click()
# driver.find_element(By.NAME,"username").send_keys("pranavmali0007@gmail.com")
# driver.find_element(By.NAME,"password").send_keys("Pranav@16091999")
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
# input("PLEASE ENTER TO CLOSE BROWSER")
########################################################################################
driver = webdriver.Chrome()
driver.get("https://www.screener.in/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@class='button account']").click()
driver.find_element(By.NAME,"username").send_keys("pranavmali0007@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Pranav@16091999")
driver.find_element(By.NAME,"password").submit()
# input("PLEASE ENTER TO CLOSE BROWSER")
driver.quit()