import requests
import json
from mogujie_db_helper import *

db = get_connection()
cursor = get_cursor(db)


# 取页面HTML
def get_one_page(page):
    url = "https://list.mogujie.com/search?callback=jQuery211021893195395962284_1554919259181&_version=8193&ratio=3%3A4&cKey=15&page=" + str(page) + "&sort=pop&ad=0&fcid=50020&action=trousers&acm=3.mce.1_10_1lbnq.128038.0.2fteOrniiUEaw.pos_2-m_497415-sd_119&ptp=1.n5T00.0.0.Ha7X3KCj&_=1554919259182"
    headers ={
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        return text
    return None


# 解析json数据
def parse_page(html):
    index = html.index('(')
    html = html[index+1:][:-2]
    # print(html)
    json_data = json.loads(html)
    is_end = json_data['result']['wall']['isEnd']
    products = json_data['result']['wall']['docs']
    # print(len(products))
    result_list = []
    for product in products:
        title = product['title']
        url = product['img']
        # save_img(url, title)
        execute_sql2(db, cursor, product)
        # result_list.append(product)
    # return result_list
    return is_end


def save_img(url, title):
    response = requests.get(url)
    file_name = title + '.jpg'
    with open('./images/%s' % file_name, 'wb') as f:
        f.write(response.content)


def main():
    page = 1
    while True:
        html = get_one_page(page)
        print('*' * 20)
        print(page)
        page += 1
        is_end = parse_page(html)
        if is_end:
            print('爬取结束')
            break
    close_connection(db)


if __name__ == '__main__':
    main()
