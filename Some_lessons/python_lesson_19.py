from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

#price = browser.find_element_by_id("price")

wait = WebDriverWait(browser,12)

wait.until(EC.text_to_be_present_in_element((By.ID,"price"),"10000"))
browser.find_element_by_id("book").click()


x = browser.find_element_by_css_selector("#input_value").text
y = calc(x)

browser.find_element_by_css_selector("#answer").send_keys(y)
browser.find_element_by_id("solve").click()
