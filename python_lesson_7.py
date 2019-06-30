from selenium import  webdriver

browser = webdriver.Chrome()
browser.get("Http://suninjuly.github.io/huge_form.html")
elements = browser.find_elements_by_tag_name("input")

for element in elements:
	element.send_keys("Kappa")
	

button = browser.find_element_by_tag_name("button")
button.click()
