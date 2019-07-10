from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

fields = browser.find_elements_by_xpath('//div[@class="first_block"]//input')

for element in fields:
	element.send_keys('random')

button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(1)
welcome_text_elt = browser.find_element_by_tag_name('h1')
welcome_text = welcome_text_elt.text
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text