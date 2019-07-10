#Поиск в дропдауне
from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

number1 = browser.find_element_by_id("num1").text
number2 = browser.find_element_by_id("num2").text


summ = str(int(number1) + int(number2))

dropdown = Select(browser.find_element_by_id("dropdown"))
dropdown.select_by_value(summ)

button = browser.find_element_by_css_selector(".btn")
button.click()