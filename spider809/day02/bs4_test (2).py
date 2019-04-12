from bs4 import BeautifulSoup
import requests
import re

# 取页面HTML
def get_one_page():
	url = "http://sports.sina.com.cn/nba/"
	headers =  {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre" 
	}
	response = requests.get(url, headers=headers)
	# print(response.status_code)
	if response.status_code == 200:
		text = response.content.decode('utf-8')
		return text
	return None

def	parse_with_bs4(html):
	# html = '<p><div><a></a></div></p>'
	# print(html)
	soup = BeautifulSoup(html, 'lxml')
	
	# 让页面标签整齐的输出
	# print(soup.prettify())
	# head标签里面title的文字内容
	# print(soup.title.string)
	# 取整个指定的标签
	# print(soup.head)
	# print(type(soup.head))
	# print(soup.p)
	# print(soup.p.name)
	# print(soup.img.attrs["src"])
	# print(soup.img.attrs)
	# print(soup.img['src'])
	# print(soup.p)
	# print(soup.p.contents)

	# 取a所有祖先节点
	# b = list(soup.a.parents)
	# print(b[1])
	# print(len(list(soup.a.parents)))
	# print(list(soup.a.parents)[0].attrs['class'])

	# print(soup.head.title.string)

	# result = soup.select('.news-list-b .list .item p a')
	# for item in result:
	# 	print(item.string)
	# 	print(item['href'])

	# result = soup.select('.-live-layout-row.layout_sports_350_650')
	# print(result)

	# l = soup.select('.ct_t_01 a')
	# for item in l:
	# 	print(item.string)
	# 	print(item['href'])
	# print(len(l))
	# item = soup.select('#syncad_1 p')[0]
	# print(item)
	# print(item.contents)
	# print(len(item.contents))
	# item = soup.select('.b_time')[0].string
	# print(item)


def main():
	html = get_one_page()
	# print(html)
	parse_with_bs4(html)

if __name__ == '__main__':
	main()