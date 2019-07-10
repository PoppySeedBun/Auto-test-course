import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_AddToBasketButton(browser):
	browser.get(link)
	#time.sleep(7)# Время на проверку текста в кнопке на разных локалях для проверяющего, осталось только разкомментить :)
	browser.find_element_by_css_selector(".btn-add-to-basket") #ищет кнопку добавления в корзину
	assert button.is_displayed(), "The 'Add to basket' button isn't displayed"# Дополнительно проверяет видимость
