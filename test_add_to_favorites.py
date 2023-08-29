from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Инициализация браузера
driver = webdriver.Chrome()

try:
    # Переход на страницу нужного объявления
    driver.get("URL_ОБЪЯВЛЕНИЯ")
    
    # Нажатие кнопки "Добавить в избранное"
    favorite_button = driver.find_element_by_css_selector(".item-view-button-favorite")
    favorite_button.click()
    
    time.sleep(2)
    
    # Проверка, что объявление добавлено в избранное
    driver.get("https://www.avito.ru/favorites")
    favorite_ads = driver.find_elements_by_css_selector(".favorites-list-item")
    if len(favorite_ads) > 0:
        print("Объявление успешно добавлено в избранное.")
    else:
        print("Не удалось добавить объявление в избранное.")

finally:
    # Закрытие браузера
    driver.quit()
