import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
from lxml import etree
from kaisha import *
import threading
from multiprocessing import Process

# 设置浏览器参数
chrome_options = webdriver.ChromeOptions()
# 设置成无头浏览器
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(browser, 5)


def get_page():
    url = 'https://www.xiami.com/chart'
    browser.get(url)
    time.sleep(3)
    html = browser.page_source
    return html


# 多线程保存音乐文件
def save_mp3_with_threads(data_mp3, data_title):
    for i in range(len(data_title)):
        title = data_title[i]
        mp3 = data_mp3[i]
        mp3_url = str2url(mp3)
        print(mp3_url)
        thread = threading.Thread(target=save_mp3, args=(mp3_url, title))
        thread.start()


# 多进程保存音乐文件
def save_mp3_with_process(data_mp3, data_title):
    for i in range(len(data_title)):
        title = data_title[i]
        mp3 = data_mp3[i]
        mp3_url = str2url(mp3)
        print(mp3_url)
        process = Process(target=save_mp3, args=(mp3_url, title))
        process.start()


def parse_page(html):
    etree_html = etree.HTML(html)
    data_mp3 = etree_html.xpath('//tr[@class="songwrapper"]/@data-mp3')
    data_title = etree_html.xpath('//tr[@class="songwrapper"]/@data-title')
    # print(data_mp3)
    save_mp3_with_threads(data_mp3, data_title)
    # for i in range(len(data_mp3)):
    #     title = data_title[i]
    #     mp3 = data_mp3[i]
    #     mp3_url = str2url(mp3)
    #     print(mp3_url)
    #     save_mp3(mp3_url, title)


def save_mp3(mp3_url, title):
    response = requests.get(mp3_url)
    if response.status_code == 200:
        content = response.content
        with open('./mp3/%s.mp3' % title, 'wb') as f:
            f.write(content)


def main():
    html = get_page()
    parse_page(html)


if __name__ == '__main__':
    main()
