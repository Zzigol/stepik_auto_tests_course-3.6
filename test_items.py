from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_find_button_add_to_basket(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    button = None
    time.sleep(30)
    try:
        button = WebDriverWait(browser, 2) \
            .until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[class="btn btn-lg btn-primary btn-add-to-basket"]')))
    finally:
        assert button, '!!! Can NOT find a button "ADD TO BASKET" on this page !!!'