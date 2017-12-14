#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from lxml import html
import requests
import re
from pprint import pprint

head = 'https://www.thegioididong.com'
mid = '/tim-kiem?key='

def get_post_thegioididong(thegioididong_name):
	name = '+'.join(thegioididong_name.lower().split())
	page = requests.get(head + mid + name)
	tree = html.fromstring(page.text)
	posts_pages = get_pages(tree) 
	post_info = get_post_info(posts_pages)
	return post_info

def get_pages(root):
	pprint("get_pages_thegioididong")
	post_urls = root.xpath('//li/a/@href')
	trees = []
	for i in range(len(post_urls)):
		if i < 10:
			page = requests.get(head + post_urls[i])
			tr = html.fromstring(page.text)
			trees.append(tr)
	return trees

def get_post_info(posts_pages):
	post_info = []
	stt = 0
	for post in posts_pages:
		tensanpham = post.xpath('//div[@class="rowtop"]/h1//text()')
		if not tensanpham:
			pass
		else:
			stt = stt + 1
			price = post.xpath("//aside[@class='price_sale']/div[@class='area_price']/strong//text()")
			if not price:
				price = post.xpath("//aside[@class='price_sale']/div[@class='boxshock']/div[@class='boxshockheader']/label/strong//text()")
				if not price:
					price = "Not Found"
			if price != "Not Found":
				price = price[0]
			detail = post.xpath("//ul[@class='policy']/li//text()")
			if not detail:
				detail = post.xpath("//ul[@class='policy ']/li//text()")
				if not detail:
					detail = "Nothing"
			if detail != "Nothing":
				detail = " ".join(detail)
			rate = post.xpath("//div[@class='ratingresult']/span[@class='star']")
			if not rate:
				rate = "None"
			else:
				rate = str(len(rate)*2) + "/10"
			post_info.append((stt, tensanpham[0], price, detail, rate))
	return post_info


if __name__ == "__main__":
	thegioididong_name = raw_input("Event to search for: ")
	results = get_post_thegioididong(thegioididong_name)
	for r in results:
		print(r)

