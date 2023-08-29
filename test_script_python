from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Инициализация браузера
driver = webdriver.Chrome()

# Предусловие: Очистить кэш и куки браузера перед началом каждого теста
driver.delete_all_cookies()

# Подготовка: Открытие главной страницы Avito
driver.get("https://www.avito.ru")

# Тестирование добавления объявления в избранное (Сценарий 1)
search_input = driver.find_element_by_name("q")
search_input.send_keys("iPhone")
search_input.send_keys(Keys.RETURN)

time.sleep(3)

first_ad = driver.find_element_by_css_selector(".iva-item-title")
first_ad.click()

favorite_button = driver.find_element_by_css_selector(".item-view-button-favorite")
favorite_button.click()

time.sleep(2)

driver.get("https://www.avito.ru/favorites")

favorite_ads = driver.find_elements_by_css_selector(".favorites-list-item")
if len(favorite_ads) > 0:
    print("Сценарий 1: Объявление успешно добавлено в избранное.")
else:
    print("Сценарий 1: Не удалось добавить объявление в избранное.")

# Тестирование добавления объявления в избранное (Сценарий 2)
driver.get("https://www.avito.ru")

search_input = driver.find_element_by_name("q")
search_input.send_keys("MacBook")
search_input.send_keys(Keys.RETURN)

time.sleep(3)

first_ad = driver.find_element_by_css_selector(".iva-item-title")
first_ad.click()

favorite_button = driver.find_element_by_css_selector(".item-view-button-favorite")
favorite_button.click()

time.sleep(2)

driver.get("https://www.avito.ru/favorites")

favorite_ads = driver.find_elements_by_css_selector(".favorites-list-item")
if len(favorite_ads) > 1:
    print("Сценарий 2: Объявление успешно добавлено в избранное.")
else:
    print("Сценарий 2: Не удалось добавить объявление в избранное.")

# Тестирование удаления объявления из избранного (Сценарий 1)
driver.get("https://www.avito.ru/favorites")

remove_button = driver.find_element_by_css_selector(".favorites-item-delete-button")
remove_button.click()

confirm_remove_button = driver.find_element_by_css_selector(".remove-button-remove")
confirm_remove_button.click()

time.sleep(2)

favorite_ads = driver.find_elements_by_css_selector(".favorites-list-item")
if len(favorite_ads) == 1:
    print("Сценарий 1: Объявление успешно удалено из избранного.")
else:
    print("Сценарий 1: Не удалось удалить объявление из избранного.")

# Тестирование удаления объявления из избранного (Сценарий 2)
driver.get("https://www.avito.ru/favorites")

remove_button = driver.find_element_by_css_selector(".favorites-item-delete-button")
remove_button.click()

confirm_remove_button = driver.find_element_by_css_selector(".remove-button-remove")
confirm_remove_button.click()

time.sleep(2)

favorite_ads = driver.find_elements_by_css_selector(".favorites-list-item")
if len(favorite_ads) == 0:
    print("Сценарий 2: Объявление успешно удалено из избранного.")
else:
    print("Сценарий 2: Не удалось удалить объявление из избранного.")


# Закрытие браузера
driver.quit()
