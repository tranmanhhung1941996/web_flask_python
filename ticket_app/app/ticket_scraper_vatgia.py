# -*- coding: UTF-8 -*-

from __future__ import print_function
from lxml import html
import requests
import re
from pprint import pprint

head = 'http://vatgia.com'
mid = "/home/"
tail = ".spvg"

def get_post_vatgia(vatgia_name):
	name = '+'.join(vatgia_name.lower().split())
	page = requests.get(head + mid + name + tail)
	tree = html.fromstring(page.text)
	posts_pages = get_pages(tree) 
	post_info = get_post_info(posts_pages)
	return post_info

def get_pages(root):
	pprint("get_pages_vatgia")
	post_urls = root.xpath("//div[@class='picture_main']/div[@class='more_content']/a/@href")
	trees = []
	for i in range(len(post_urls)):	 
		if i < 10:
			page = requests.get(head+post_urls[i])
			tr = html.fromstring(page.text)
			trees.append(tr)
	return trees

def get_post_info(posts_pages):
	post_info = []
	stt = 0
	for post in posts_pages:
		product_name = post.xpath("//div[@id='detail_product_exclusive_information']/div[@class='detail_product_exclusive_information']/h1//text()")
		if not product_name :
			pass
		else :
			price = post.xpath("//td[@class='value_product_price']/b[@class='product_price']//text()")
			if not price:
				price = "Not Found"
			rate = post.xpath("//div[@class='rate_estore_review']/div[@class='start_review']//text()")
			if not rate:
				rate = "None"
			else:
				if rate[0] == "0":
					rate = "Not yet"
				else:
					rate = rate[0] + '/5'
	
			stt = stt + 1
			post_info.append((stt, product_name[0], price[0], rate))
	return post_info


if __name__ == "__main__":
	vatgia_name = raw_input("Event to search for: ")
	location = raw_input("Location of event: ")
	results = get_post_vatgia(vatgia_name)
	for r in results:
		print(r)

