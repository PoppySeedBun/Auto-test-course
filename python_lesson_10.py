from selenium import webdriver
import time
link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

field1 = browser.find_element_by_css_selector("div.first_block .first")
field2 = browser.find_element_by_css_selector("div.first_block .second")
field3 = browser.find_element_by_css_selector("div.first_block .third")

for element in field1,field2,field3:
	element.send_keys("random")

button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(1)
welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text