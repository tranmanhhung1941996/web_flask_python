# -*- coding: UTF-8 -*-

from __future__ import print_function
from lxml import html
import requests
import re
from pprint import pprint

link = 'https://www.sendo.vn/tim-kiem?q='

def get_post_lazada(lazada_name):
	name = '%2B'.join(lazada_name.lower().split())
	page = requests.get(link + name)
	tree = html.fromstring(page.text)
	posts_pages = get_pages(tree) 
	post_info = get_post_info(posts_pages)
	return post_info

def get_pages(root):
	pprint("get_pages_lazada")
	post_urls = root.xpath('//div[@class="img_product productPreview"]/a/@href')
	trees = []
	for i in range(len(post_urls)):
		if i < 10:
			page = requests.get(post_urls[i])
			tr = html.fromstring(page.text)
			trees.append(tr)
	return trees

def get_post_info(posts_pages):
	post_info = []
	stt = 0
	ship = 10000
	for post in posts_pages:
		tensanpham = post.xpath('//div[@class="block-pro-attr"]/div[@class="box-name item"]/h1/strong/span//text()')
		if not tensanpham:
			pass
		else:
			stt = stt + 1
			price = post.xpath("//div[@class='box-price-wirehouse']/div[@class='box-price']/div[@class='cur-price']//text()")
			if not price:
				price = "Not Found"
			else:
				price = " ".join(price)
			detail = post.xpath("//div[@class='attribute-origin-tech tskt for-desc']/div[@class='attrs']//text()")
			if not detail:
				detail = "Nothing"
			else:
				detail = " ".join(detail)
			post_info.append((stt, tensanpham[0], price, detail,ship))
	return post_info


if __name__ == "__main__":
	lazada_name = raw_input("Event to search for: ")
	results = get_post_lazada(lazada_name)
	for r in results:
		print(r)

