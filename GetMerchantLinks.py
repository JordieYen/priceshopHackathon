import csv
import sys
import json
import re
import requests
import math

def main():
	args = sys.argv[1:]

	if len(args) == 1:
		rows = []
		with open(args[0], 'r') as file:
			csvreader = csv.reader(file)
			header = next(csvreader)
			for row in csvreader:
				rows.append(row)
		pageNum = 1
		print("Lazada Link")
		for row in rows:
			url = row[0]
			print(row[0])
		# url = "https://www.lazada.com.my/sentriqmy/?q=All-Products&from=wangpu&langFlag=en&pageTypeId=2"
			response = requests.get(url)
			d = json.loads(re.search(r'window.pageData = ({.*})', response.text).group(1))
			num = d['mainInfo']['totalResults']
			num = math.ceil(int(num) / 40) + 1
			# print(num)
			for pageNum in range(1, num):
				link = f"{url}{pageNum}"
				response = requests.get(link)
				# print(response.text)
				# print(json.dumps(d, indent=4))
				# example = f"https://www.lazada.com.my/sentriqmy/?q=All-Products&from=wangpu&langFlag=en&pageTypeId=2&page={pageNum}"
				for stuff in d['mods']['listItems']:
					print("https:" + stuff['itemUrl'] + ",")


if __name__ == '__main__':
    main()