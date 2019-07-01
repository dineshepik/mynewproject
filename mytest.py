from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import HtmlTestRunner
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Code to setup browser
print("------------------- Browser Set Up Initiated --------------------")
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
actions = ActionChains(driver)
print("------------------ Browser Set Up Successfully --------------")
print("\n")

# Code to hit the URL
print("---------------Trying to open the URL ----------------")
driver.get("http://34.93.30.19/")
time.sleep(4)
print("--------------- URL opened ----------------")
print("\n")
time.sleep(6)

driver.find_element_by_xpath("//a[contains(@href, '/content/about-us.php')]").click()
time.sleep(2)
actual_text = driver.find_element_by_id("PID-ab2-pg").text
print(driver.find_element_by_id("PID-ab2-pg").text)
expected = "This is about page. Lorem Ipsum Dipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
if actual_text == expected:
    print("Same string")
else:
    print("Failed")


