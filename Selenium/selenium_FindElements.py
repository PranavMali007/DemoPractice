import os
from fileinput import filename
from time import sleep

from attr import attributes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://omayo.blogspot.com/')
# time.sleep(3)
# driver.find_element(By.ID,"ta1").send_keys("Hello World")
# time.sleep(3)
# driver.find_element(By.NAME,"q").send_keys("PRANAV MALI")
# time.sleep(3)
# driver.find_element(By.CLASS_NAME,'combobox').click()
# time.sleep(3)
# driver.find_element(By.LINK_TEXT,"compendiumdev").click()
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR,"input[value='Cancel']").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input[value='Cancel']").click()
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input[value='Cancel']").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"//input[@value='Login']").click()
# time.sleep(3)
# for i in range(5):
#     driver.find_element(By.CSS_SELECTOR,"#ta1").send_keys("<PRANAV>\n<MALI>")
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR,"#ta1").clear()

# text = driver.find_element(By.XPATH,"//div[@id='HTML45']//button[1]").text
# print(text)

# title = driver.title
# print(title)
# current_url = driver.current_url
# print(current_url)
# # driver.find_element(By.LINK_TEXT,"theautomatedtester")
# driver.find_element(By.PARTIAL_LINK_TEXT,"theautomatedtester").click()
# current_url = driver.current_url
# print(current_url)

# attributes = driver.find_element(By.ID,"sa").get_attribute("value")
# print(attributes)
####################################################################* is_displayed()
# if driver.find_element(By.ID,'hbutton').is_displayed():
#     print("HIDDEN BUTTON AVAILABLE")
# else:
#     print("HIDDEN BUTTON NOT AVAILABLE")
####################################################################* is_enabled()
# if driver.find_element(By.ID,"but2").is_enabled():
#     print('Button 2 Enabled')
# else:
#     print('Button 2 Disabled')
#
# if driver.find_element(By.ID,"but1").is_enabled():
#     print('Button 1 Enabled')
# else:
#     print('Button 1 Disabled')
#####################################################################* is_selected()
# for i in range(5):
#     if driver.find_element(By.NAME,'color').is_selected():
#         print('Check box already enabled')
#     else:
#         print('Check box Enabling NoW.....')
#         driver.find_element(By.NAME,'color').click()
#     sleep(2)
#     driver.find_element(By.NAME, 'color').click()
##########################################################*driver.forward() * driver.back()
# driver.find_element(By.LINK_TEXT,'onlytestingblog').click()
# driver.back()
# # sleep(2)
# driver.forward()
# # sleep(2)
# driver.back()
##########################################################*driver.refresh()
# driver.refresh()
# driver.refresh()
##########################################################*driver.page_source
# html_code = driver.page_source
# with open("html_file.html",'w') as e:
#     e.write(html_code)
##########################################################*driver.fullscreen()
# driver.fullscreen_window()
# sleep(5)
##########################################################*driver.set_window_
# driver.set_window_size(1920, 1080)
# driver.set_window_position(7.9,90)
# driver.set_window_rect(50,50,50,50)
# sleep(2)
##########################################################*driver.driver.save_screenshot
# driver.save_screenshot('save_screenshot.png')
# driver.save_screenshot('save_screenshot')
# driver.get_screenshot_as_file('get_screenshot_as_file')
# s= driver.get_screenshot_as_base64()
# print(s)
##########################################################*driver.size
# size = driver.find_element(By.XPATH,"//textarea[@id='ta1']").size
# print(type(size))
# print(size)
# print(size.items())
# print(size.values())
# print(size.keys())

##########################################################drop down
# dropdowne = driver.find_element(By.ID,"multiselect1")
dropdowne = driver.find_element(By.ID,"drop1")
select = Select(dropdowne)

# select.select_by_visible_text('doc 2')
#or
# select.select_by_index(2)
#or
# select.select_by_value("ghi")
# or
# print(select.is_multiple) #It will print True If multi select option available else false

################
for option in select.options:
    print(option.text)

driver.close()