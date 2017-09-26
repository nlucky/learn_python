#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import traceback
import re
import models



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
	count = 0
	for stock in list:
		url = info_url + stock + '.html'
		html = get_html_text(url)
		try:
			if html == "":
				continue
			info_dic = {}
			soup = BeautifulSoup(html, 'html.parser')
			stock_info = soup.find('div', attrs = {'class':'stock-bets'})
			stock_name = stock_info.find_all(attrs = {'class' : 'bets-name'})[0]
			info_dic.update({'股票名称' : stock_name.text.split()[0]})
			key_list = stock_info.find_all('dt')
			value_list = stock_info.find_all('dd')
			for i in range(len(key_list)):
				key = key_list[i].text
				value = value_list[i].text
				info_dic[key] = value

			stock = Stock(info_dic)

			# with open(fpath, 'a', encoding='utf-8') as f:
			# 	f.write( str(info_dic) + '\n' )
			count = count + 1
			print("\r当前进度: {:.2f}% \n".format(count*100/len(list)),end="")
		except:
			# count = count + 1
			# print("\r当前进度 nil: {:.2f}% \n".format(count*100/len(list)),end="")

			continue
		



def main(): 
	list_url = 'http://quote.eastmoney.com/stocklist.html'
	info_url = 'https://gupiao.baidu.com/stock/'
	html = get_html_text(list_url)
	stock_list = []
	outfile = 'stockinfo.txt'
	get_stock_list(stock_list, list_url)
	get_stock_info(stock_list, info_url, outfile)

main()
