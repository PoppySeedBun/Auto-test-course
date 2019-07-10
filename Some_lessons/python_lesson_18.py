from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

link ="http://suninjuly.github.io/wait1.html"
link2 = "http://suninjuly.github.io/wait2.html"
browser = webdriver.Chrome()
browser.get(link2)

#browser.implicitly_wait(5)

#browser.find_element_by_id("check").click()

button = WebDriverWait(browser, 5).until(
		EC.element_to_be_clickable((By.ID, "check"))
	)


button.click()



button2 = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element(By.ID("123123"),"123123"))

message = browser.find_element_by_id("check_message").text

assert "успешно" in message



