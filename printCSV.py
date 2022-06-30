#!/usr/bin/env python3
import csv
import sys
import json
import re
import requests
from time import sleep
from selenium import webdriver
from random import random, randint

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

		count = 0
		print("link,Product Name,Variant,Stock Availability,Pricing,Category")
		for row in rows:
			url = row[0]

			count += 1
			if count % 2 == 0:
				sleep(random())
			if count % 200 == 0:
				sleep(randint(30, 45))
			if count % 500 == 0:
				sleep(randint(60, 90))
				
			response = requests.get(url)
			d = json.loads(re.search(r'var __moduleData__ = ({.*})', response.text).group(1))
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
				
				a = ""
				if 'propPath' in sku:
					propPath = sku['propPath']
					properties = propPath.split(";")
					specs = []

					for prop in properties:
						specs.append(prop.split(":")[1])

					for property in productProperties:
						for spec in specs:
							magic = findCallback(property['values'], lambda x: x['vid'] == spec)
							if magic:
								a = a + magic['name'] + " "

				print(url + ',' + pdt_name.replace(",", '') + ',' + a + ',' + str(pdt_stock) + ',' + pdt_price.replace(",", '') + ',' + pdt_category)
			# print('\n\n\n=============================\n\n\n')
	else:
		print("ERROR : input 1 file name")

if __name__ == '__main__':
    main()