# import pytest
# import os
# import sys
# import inspect

# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir) 

# from routes import show_histogram

# def test_1():
#     pass

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


PATH = "C://Users//Apprenant//Documents//chromedriver_win32//chromedriver.exe"
# binary = FirefoxBinary('C:\Users\Apprenant\Documents\geckodriver\geckodriver.exe')
# driver = webdriver.Firefox(firefox_binary=binary)

driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:5000/list_without_alternance")

# assert "list_without_alternance" in driver.title
# elem = driver.find_elements_by_class_name("form-control")
# elem = driver.find_element_by_name("form-control")
# elem.clear()
# elem.send_keys("Chua")
# elem.send_keys(Keys.RETURN)

# a = driver.find_elements_by_tag_name("td")

# assert len(a) ==  4

# driver.close()
