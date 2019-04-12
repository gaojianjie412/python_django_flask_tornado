import re

import requests


def get_one_page():
    url = "https://www.mkv99.com/vod-detail-id-16742.html"
    headers ={
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        return text
    return None


def parse_html(html):
    pattern = re.compile('<script>.*?var.*?downurls=".*?\$(.*?)#";', re.S)
    url = re.findall(pattern, html)
    print(url)


def main():
    html = get_one_page()
    parse_html(html)


if __name__ == '__main__':
    main()