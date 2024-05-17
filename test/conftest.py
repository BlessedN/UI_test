import pytest
import time
from selenium import webdriver
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
            received_element = self.driver.find_element(
                by=By.XPATH, value=f'{locator}'
            )
            return True, received_element
        except NoSuchElementException:
            return False, None

    def active_checkbox(self, locator) -> bool:
        received_element = self.xpath(locator)[1]
        if received_element is None:
            return False
        return received_element.is_selected()

    def open(self, url):
        self.driver.get(url)

    def send_keys(self, locator, keys):
        search_field = self.xpath(locator)[1]
        if search_field is not None:
            search_field.send_keys(keys)

    def find_button_and_click(self, locator):
        time.sleep(2)
        received_element = self.xpath(locator)[1]
        if received_element is None:
            return False
        received_element.click()
        time.sleep(6)

    def scroll_by(self, limit):
        time.sleep(1)
        self.driver.execute_script(
            f"window. scrollBy(0, {limit})"
        )
        time.sleep(1)

    def get_min_cost_book(self, locator):
        all_book_web_elem = self.driver.find_elements(
            by=By.XPATH, value=f'{locator}'
        )
        books_price = [i.text for i in all_book_web_elem]
        books_price_min = min(
            [int("".join(i.split(" ₽")[0].split(" "))) for i in books_price])
        return books_price_min







