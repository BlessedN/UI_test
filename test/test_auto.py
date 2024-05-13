import time

from allure_commons.types import LabelType, AttachmentType
from selenium.webdriver.common.by import By
import allure



@allure.id("1")
@allure.title('Тест "Читай город"')
@allure.feature('Мой главный автоматизированный тест')
@allure.tag('UI')
@allure.severity('trivial')
@allure.label(LabelType.FRAMEWORK, "pytest")
def test_run_browser(browser):
    browser.open(url='https://www.chitai-gorod.ru/')

    with allure.step('Поиск книги'):
        browser.send_keys(xpath='//input[@placeholder]',
                          keys='Ремарк Три товарища')
        assert browser.xpath(
            '(//button[@aria-label])[2]'
        ), 'Кнопка "поиск" не найдена'
        browser.find_button_and_click('(//button[@aria-label])[2]')
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG
        )

    with allure.step('Выбор типа переплета книги'):
        browser.scroll_by(limit=1200)
        browser.find_button_and_click(
            '//span[contains(text(), "Твердый переплёт")]/../../div'
        )
        assert browser.active_checkbox(
            '//input[@type="checkbox" and @name="Твердый переплёт"]'
        ), 'Чекбокс "твердый переплет" неактивен'
        time.sleep(3)
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG
           )

    with allure.step('Поиск книги по наименьшей стоимости'):
        books_price_min = browser.get_min_cost_book(
            xpath='//div[contains(@class,"list")]//*[contains(text(), " ₽" ) and contains(@class,"discount")]'
        )
        allure.attach(str(books_price_min), name="Минимальная цена книги",
                      attachment_type=AttachmentType.TEXT)
        time.sleep(3)
        allure.attach(browser.driver.get_screenshot_as_png(), name="Screenshot",
                      attachment_type=AttachmentType.PNG)

    with allure.step('Помещение книги с мин.стоимостью в корзину'):
        browser.scroll_by(limit=300)
        browser.find_button_and_click(
            xpath=f'(//*[contains(text(), "{books_price_min}")])[1]/../../../div[3]//span'
        )
        browser.find_button_and_click(
            xpath='//a[@href="/cart"]'
        )
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG
        )
