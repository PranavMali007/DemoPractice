'''TO run parallel TC pip install pytest-xdist
    use: pytest -n 2 in console to execute
'''

from time import sleep

from selenium import webdriver

def test_open_omayo():
    driver = webdriver.Chrome()
    driver.get('https://omayo.blogspot.com/')
    sleep(5)
    driver.quit()


def test_open_selenium_143():
    driver = webdriver.Chrome()
    driver.get('https://selenium143.blogspot.com/')
    sleep(5)
    driver.quit()

def test_open_blogger():
    driver = webdriver.Chrome()
    driver.get('https://www.blogger.com/about/?bpli=1&pli=1')
    sleep(5)
    driver.quit()