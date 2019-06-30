#Скролл страницы
from selenium import webdriver
import math

def calc(x):
	return  str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element_by_id("input_value").text
y = calc(x)

scroller = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", scroller)
scroller.send_keys(y)
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()


button = browser.find_element_by_tag_name("button")
button.click()
#assert True