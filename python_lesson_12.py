from selenium import webdriver
import math


def calc(x):
	return  str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

chest = browser.find_element_by_css_selector("img")
x = chest.get_attribute("valuex")
y = calc(x)

checkbox = browser.find_element_by_css_selector("#robotCheckbox")
checkbox.click()
radiobutton = browser.find_element_by_css_selector("#robotsRule")
radiobutton.click()
inputpanel = browser.find_element_by_css_selector("#answer")
inputpanel.send_keys(y)
btn = browser.find_element_by_css_selector(".btn")
btn.click()
