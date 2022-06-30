#!/usr/bin/env python3
import csv
import sys
import json
import re
import requests
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def findCallback(list, filter):
    for x in list:
        if filter(x):
            return x
    return False

def main():
	args = sys.argv[1:]

	if len(args) == 1:
		rows = []
		with open(args[0], 'r') as file:
			csvreader = csv.reader(file)
			header = next(csvreader)
			for row in csvreader:
				rows.append(row)
		# count = 0
		c = webdriver.ChromeOptions()
		c.add_argument("--incognito")
		driver = webdriver.Chrome(executable_path=r"/Users/wting/hackathon/priceshop/chromedriver", options=c);
		for row in rows:
			# count += 1
			# if count % 300 == 0:
			# 	time.sleep(30)
			# time.sleep(0.2)
			print(row[0], '\n')
			url = row[0]
			# url = 'https://www.lazada.com.my/products/sandisk-cruzer-glide-cz600-16gb32gb64gb128gb-m30-150mbs-usb-flash-drive-pendrive-originalsandisk-cruzer-blade-16gb-usb-flash-drive-20-electric-pink-original-5-year-warranty-i2870869475.html'
			response = requests.get(url)
			driver.get(url)
			if  "Sorry, we have detected unusual traffic from your network." in driver.find_element("class", "warnning-text"):
				print("fuck urself")
				return
			else:
				d = json.loads(re.search(r'var __moduleData__ = ({.*})', response.text).group(1))
				# print(d)
				del d['data']['root']['fields']['skuInfos']['0']
				skuInfos = d['data']['root']['fields']['skuInfos']
				skuBase = d['data']['root']['fields']['productOption']['skuBase']
				productProperties = skuBase['properties']
				skus = skuBase['skus']
				for skuId in skuInfos:
					pdt_name = d['data']['root']['fields']['skuInfos'][skuId]['dataLayer']['pdt_name']
					pdt_price = d['data']['root']['fields']['skuInfos'][skuId]['dataLayer']['pdt_price']
					pdt_category = d['data']['root']['fields']['skuInfos'][skuId]['dataLayer']['pdt_category'][-1]
					pdt_stock = d['data']['root']['fields']['skuInfos'][skuId]['stock']
					sku = findCallback(skus, lambda x: x['cartSkuId'] == skuId)
					if 'propPath' in sku:
						propPath = sku['propPath']
						properties = propPath.split(";")
						specs = []
						for prop in properties:
							specs.append(prop.split(":")[1])
						a = ""
						for property in productProperties:
							for spec in specs:
								magic = findCallback(property['values'], lambda x: x['vid'] == spec)
								if magic:
									a = a + magic['name'] + " "
								
						print(pdt_name, '|', a, '| stock:', pdt_stock, '| ', pdt_price, '| category:', pdt_category, '\n')
					print(pdt_name, '| stock:', pdt_stock, '| ', pdt_price, '| category:', pdt_category, '\n')
				print('\n\n\n=============================\n\n\n')
	else:
		print("ERROR : input 1 file name")

if __name__ == '__main__':
    main()