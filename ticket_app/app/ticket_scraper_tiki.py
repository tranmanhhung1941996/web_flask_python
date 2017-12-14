# -*- coding: UTF-8 -*-

from __future__ import print_function
from lxml import html
import requests
import re
from pprint import pprint

def get_post_tiki(tiki_name):
	name = '+'.join(tiki_name.lower().split())
	page = requests.get("https://tiki.vn/search?q=" + name)
	tree = html.fromstring(page.text)
	posts_pages = get_pages(tree) 
	post_info = get_post_info(posts_pages)
	return post_info

def get_pages(root):
	pprint("get_pages_tiki")
	post_urls = root.xpath("//div[@class='product-box-list']/div[@class='product-item    search-div-product-item']/a/@href")
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
	for post in posts_pages:
		title = post.xpath("//div[@class='item-box']/h1//text()")
		if not title :
			pass
		else :
			price = post.xpath("//p[@class='special-price-item']/span[@id='span-price']//text()")
			
			if not price:
				price = "Not Found"
			detail = post.xpath("//div[@class='top-feature-item bullet-wrap']/p//text()")
			if not detail:
				detail = "Nothing"
			else:
				detail = ". ".join(detail)
			rate = post.xpath("//div[@class='item-rating']/p[@class='rating']/span[@class='rating-box']/span/@style")
			if not rate:
				rate = "None"
			else:
				rate = rate[0].split(':')
				rate = rate[1].split('%')
				rate = rate[0] + '/100'
			stt = stt + 1
			post_info.append((stt, title[0], price[0], detail, rate))
	return post_info


if __name__ == "__main__":
	tiki_name = raw_input("Event to search for: ")
	results = get_post_tiki(tiki_name)
	for r in results:
		print(r)

