#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import traceback
import re

def get_html_text(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

def get_stock_list(list, url):
	html = get_html_text(url)
	soup = BeautifulSoup(html, 'html.parser')
	a = soup.find_all('a')
	for i in a:
		try:
			herf = i.attrs['href']
			list.append(re.findall(r"[s][hz]\d{6}", herf)[0])
		except:
			continue

def get_stock_info(list, info_url, fpath): 
	for stock in list:
		count = 0
		url = info_url + stock + '.html'
		html = get_html_text(url)
		try:
			if html == "":
				continue
			info_dic = {}
			soup = BeautifulSoup(html, 'html.parser')
			stock_info = soup.find('div', attrs = 'stock-bets')
			stock_name = soup.find_all(attrs = {'class' : 'bets-name'})[0]
			info_dic.update({'股票名称' : stock_name})
			key_list = stock_info.find_all('dt')
			value_list = stock_info.find_all('dd')
			for i in xrange(len(key_list)):
				key = key_list[i]
				value = value_list[i]
				info_dic[key] = value

			with open(fpath, 'a', encoding='utf-8') as f:
				f.write( str(infoDict) + '\n' )
				count = count + 1
				print("\r当前进度: {:.2f}%".format(count*100/len(list)),end="")

		except:
			count = count + 1
			print("\r当前进度: {:.2f}%".format(count*100/len(list)),end="")

			continue
		



def main(): 
	list_url = 'http://quote.eastmoney.com/stocklist.html'
	info_url = 'https://gupiao.baidu.com/stock/'
	html = get_html_text(list_url)
	stock_list = []
	outfile = 'stock.txt'
	get_stock_list(stock_list, list_url)
	get_stock_info(stock_list, info_url, outfile)

main()
