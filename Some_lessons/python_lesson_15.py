#Загрузка файлов
from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_name("firstname").send_keys("Jojo")
browser.find_element_by_name("lastname").send_keys("Jaja")
browser.find_element_by_name("email").send_keys("Jojo-jaja@email.com")

filedir = os.path.abspath(os.path.dirname(__file__))
filedir = os.path.join(filedir, "Test.txt")

browser.find_element_by_id("file").send_keys(filedir)
browser.find_element_by_css_selector(".btn").click()
