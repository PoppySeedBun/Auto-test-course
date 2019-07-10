from selenium import webdriver
import math

def calc(x):
	return  str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

rbt_chckbx = browser.find_element_by_css_selector("#robotCheckbox")
rbt_radio = browser.find_element_by_css_selector("#robotsRule")
xvalue = browser.find_element_by_css_selector("#input_value")
input_answer = browser.find_element_by_css_selector("#answer")
submit = browser.find_element_by_css_selector(".btn")

rbt_chckbx.click()
rbt_radio.click()
x = xvalue.text
y = calc(x)
input_answer.send_keys(y)
submit.click()



