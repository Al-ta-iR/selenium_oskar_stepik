
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_find_add_to_card_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
    ).is_displayed(), \
        'Кнопка добавления товара в корзину отсутсвует'