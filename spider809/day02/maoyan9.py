import requests
import re
import json
from maoyan_db_helper import *

db = get_connection()
cursor = get_cursor(db)


# 获取网页
def get_page(page):
    url = 'https://maoyan.com/board/4?offset=%d' % (page * 10)
    response = requests.get(url)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None


# 解析网页
def parse_page(html):
    # 取片名
    pattern = re.compile('movieId.*?>.*?<img.*?<img.*?alt="(.*?)" class.*?', re.S)
    movie_names = re.findall(pattern, html)
    # print(movie_names)

    # 取主演
    pattern = re.compile('<p class="star">(.*?)</p>', re.S)
    actors = re.findall(pattern, html)
    actors = [ actor.strip() for actor in actors ]
    # print(actors)

    # 取上映时间
    pattern = re.compile('<p class="releasetime">(.*?)</p>', re.S)
    releasetimes = re.findall(pattern, html)
    # print(releasetimes)

    # 取封面图片url
    pattern = re.compile('movieId.*?>.*?<img.*?<img.*?src="(.*?)" alt.*?', re.S)
    cover_urls = re.findall(pattern, html)
    # print(cover_urls)

    # 取评分
    pattern = re.compile('<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>', re.S)
    scores = re.findall(pattern, html)
    scores = [ ''.join(score) for score in scores ]
    # print(scores)

    # 取排名
    pattern = re.compile('<i class="board-index board-index-.*?">(.*?)</i>', re.S)
    ranks = re.findall(pattern, html)
    # print(ranks)

    # 取详情链接
    pattern = re.compile('<p class="name"><a href="(.*?)" title.*?>', re.S)
    detail_urls = re.findall(pattern, html)
    # print(detail_urls)

    # 获取数据列表
    result_list = []
    for i in range(len(movie_names)):
        item_dict = {}
        item_dict['movie_name'] = movie_names[i]
        item_dict['actor'] = actors[i]
        item_dict['releasetime'] = releasetimes[i]
        item_dict['cover_url'] = cover_urls[i]
        # save_image(item_dict['cover_url'])

        item_dict['score'] = scores[i]
        item_dict['rank'] = ranks[i]
        item_dict['detail_url'] = detail_urls[i]

        # 插入数据库
        execute_sql2(db, cursor, item_dict)
        result_list.append(item_dict)

    return result_list


# 写入json数据文件
def write_json(result_list):
    json_str = json.dumps(result_list, ensure_ascii=False)
    with open('./movies9.json', 'w', encoding='utf-8') as f:
        f.write(json_str)


# 保存图片文件到本地
def save_image(cover_url):
    response = requests.get(cover_url)
    # file_name = re.findall(r'.*?movie/(.*?)@', cover_url)[0]
    # print(file_name)        

    file_name = cover_url.split('/')[-1].split('@')[0]
    print(file_name)
    with open('./images9/%s' % file_name, 'wb') as f:
        f.write(response.content)


def main():
    
    result_list = []
    for page in range(10):
        print(page)
        html = get_page(page)
        # print(html)
        one_page_list = parse_page(html)
        result_list.extend(one_page_list)

    print(result_list)
    print(len(result_list))
    write_json(result_list)

    close_connection(db)


if __name__ == '__main__':
    main()