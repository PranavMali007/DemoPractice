from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests



@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/")
    driver.implicitly_wait(5)
    # request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == 'call' and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            file_name = f"screenshot_{item.name}.png"
            driver.save_screenshot(file_name)
            print(f"\nScreenshot captured as {file_name}")

def test_demo1(driver):
    Test_Verification = driver.find_element(By.LINK_TEXT,'A/B Testing').click()
    print(f'Test_Verification ={Test_Verification}')    #None will return
    driver.implicitly_wait(5)
    assert 'The Internet' in driver.title
    assert 'Test_Verification' is not None


def test_demo2(driver):
    Add_Remove = driver.find_element(By.LINK_TEXT,'Add/Remove Elements').click()
    driver.implicitly_wait(5)
    add_button = driver.find_element(By.XPATH,"//button[@onclick='addElement()']")
    print(f'delete_buttons = {add_button}')
    for i in range(50):
        add_button.click()
    delete_buttons = driver.find_elements(By.XPATH, "//button[@class='added-manually']")
    print(f'delete_buttons = {delete_buttons}')
    print(f"Total 'Add Element' clicks (Delete buttons present): {len(delete_buttons)}")
    for i in delete_buttons:
        i.click()

def test_broken_images(driver):
    Broken_img = driver.find_element(By.LINK_TEXT,'Broken Images').click()
    images = driver.find_elements(By.TAG_NAME, "img")
    broken_images = []
    for img in images:
        src = img.get_attribute('src')
        print(f'img ==== {img}')
        print(f'src ==== {src}')
        try:
            response = requests.get(src, stream=True)
            print(f'response ==== {response}')
            print(f'response.status_code ==== {response.status_code}')
            if response.status_code != 200:
                broken_images.append(src)
        except Exception as e:
            broken_images.append(src)
    # print(f"Total images: {len(images)}")
    # print(f"Broken images ({len(broken_images)}): {broken_images}")
    assert len(broken_images) == 0, f'Broken images found: {broken_images}'