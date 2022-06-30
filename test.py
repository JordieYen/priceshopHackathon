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
		# 	print(row[0], '\n')
		# 	url = row[0]
			url = 'https://www.lazada.com.my/products/apple-ipad-102-inch-9th-gen-wi-fi-i2477575777-s10832263173.html'
			response = requests.get(url)
			d = json.loads(re.search(r'var __moduleData__ = ({.*})', response.text).group(1))
			del d['data']['root']['fields']['skuInfos']['0']
			for skuId in d['data']['root']['fields']['skuInfos']:
				pdt_name = d['data']['root']['fields']['skuInfos'][skuId]['dataLayer']['pdt_name']
				# result = ''
				# result = pdt_name.lower
				print(pdt_name)
	else:
		print("ERROR : input 1 file name")

if __name__ == '__main__':
    main()