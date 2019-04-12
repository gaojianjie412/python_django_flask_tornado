from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from lxml import etree

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 5)


def get_page():
    url = 'https://www.mogujie.com'
    browser.get(url)
    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#top_nav_text')))
    input.clear()
    input.send_keys('睡衣')
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#top_nav_btn')))
    button.click()
    time.sleep(3)

    return browser.page_source


def parse_html(html):
    pass


def main():
    html = get_page()
    # print(html)
    etree_html = etree.HTML(html)
    items = etree_html.xpath('//div[@class="pin-item-wrap"]')
    for item in items:
        titles = item.xpath('.//div[@class="pin-info"]/div[@class="pin-info-title"]/text()')
        title = titles[0].strip()


if __name__ == '__main__':
    main()