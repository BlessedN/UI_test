import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1540, 1024)
    driver.set_window_position(0, 0)
    yield BasePage(driver)
    driver.close()


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def xpath(self, locator):
        try:
            self.driver.find_element(
                by=By.XPATH, value=f'{locator}'
            )
            return True
        except NoSuchElementException:
            return False

    def active_checkbox(self, locator) -> bool:
        checkbox_is_selected = self.driver.find_element(
            by=By.XPATH, value=f'{locator}'
        ).is_selected()
        return checkbox_is_selected

    def open(self, url):
        self.driver.get(url)

    def send_keys(self, xpath, keys):
        search_field = self.driver.find_element(
            by=By.XPATH, value=f'{xpath}'
        )
        search_field.send_keys(keys)

    def find_button_and_click(self, xpath):
        time.sleep(2)
        click_button = self.driver.find_element(
            by=By.XPATH, value=f'{xpath}'
        )
        click_button.click()
        time.sleep(6)

    def scroll_by(self, limit):
        time.sleep(1)
        self.driver.execute_script(
            f"window. scrollBy(0, {limit})"
        )
        time.sleep(1)

    def get_min_cost_book(self, xpath):
        all_book_webelem = self.driver.find_elements(
            by=By.XPATH, value=f'{xpath}'
        )
        books_price = [i.text for i in all_book_webelem]
        books_price_min = min(
            [int("".join(i.split(" ₽")[0].split(" "))) for i in books_price])
        return books_price_min







