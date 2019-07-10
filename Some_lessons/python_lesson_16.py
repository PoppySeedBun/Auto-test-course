#Переключение на алерты
from selenium import webdriver
import math
import pyperclip


def count(x):
	return str(math.log(abs(12*math.sin(int(x)))))
	

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector(".btn").click()

alert = browser.switch_to.alert
alert.accept()

x = browser.find_element_by_css_selector("#input_value").text
y = count(x)
browser.find_element_by_css_selector("#answer").send_keys(y)
browser.find_element_by_css_selector(".btn").click()

code = str(browser.switch_to.alert.text)
code = code.split(': ')[-1]

pyperclip.copy(code)