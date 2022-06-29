#!/usr/bin/env python3
import csv
import sys
import json
import re
import requests

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
		# for row in rows:
			# print(row[0])
			url = 'https://www.lazada.com.my/products/apple-ipad-102-inch-9th-gen-wi-fi-i2477575777-s10832263173.html'
			# url = row[0]
			response = requests.get(url)
			# print(response.text)
			d = json.loads(re.search(r'var __moduleData__ = ({.*})', response.text).group(1))
			del d['data']['root']['fields']['skuInfos']['0']
			skuInfos = d['data']['root']['fields']['skuInfos']
			skuBase = d['data']['root']['fields']['productOption']['skuBase']
			productProperties = skuBase['properties']
			skus = skuBase['skus']

			for skuId in skuInfos:
				pdt_name = d['data']['root']['fields']['skuInfos'][skuId]['dataLayer']['pdt_name']
				pdt_price = d['data']['root']['fields']['skuInfos'][skuId]['dataLayer']['pdt_price']
				# print(skuId, ': ', pdt_name, pdt_price, '\n')
				sku = findCallback(skus, lambda x: x['cartSkuId'] == skuId)
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
				print(pdt_name, '|' , pdt_price, '|' , a, '\n')

				# print(skuInfos[skuId]['price']['salePrice']['text'], '\n')
			# print('\n\n\n=============================\n\n\n')




			# for item in skuInfos:
			# 	for stuff in d['data']['root']['fields']['skuInfos'][item]:
			# 		print(stuff)
					# if stuff == 'price':
					# 	print(json.dumps(d['data']['root']['fields']['skuInfos'][item][stuff], indent = 4))
					# if stuff == 'quantity':
					# 	print(json.dumps(d['data']['root']['fields']['skuInfos'][item][stuff], indent = 4))
					# if stuff == 'dataLayer':
					# 	print(json.dumps(d['data']['root']['fields']['skuInfos'][item][stuff], indent = 4))

			# print(json.dumps(skuInfos, indent = 4))
			# print(json.dumps(d['data']['root']['fields']['skuInfos'][temp], indent = 4))
	else:
		print("ERROR : input file name")

if __name__ == '__main__':
    main()