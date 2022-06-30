#!/usr/bin/env python3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv
import sys
import json
import re
import requests

def remove_consec_dash(s):
    new_s = ""
    prev = ""
    for c in s:
        if c == prev and c == '-':
            continue
        else:
            new_s += c
            prev = c
    return new_s

args = sys.argv[1:]
query = 'iPad 10.2-inch 9th Gen Wi-Fi + Cellular (2021)'
if len(args) == 1:
	rows = []
	
	with open (args[0], 'r') as file :
		csvreader = csv.reader(file)
		header = next(csvreader)

		for row in csvreader:
			rows.append(row)

		column = []
		for row in rows:
			res = row[1]
			splitres = res.split(",")
			column.append(splitres)

		items = []
		for item in column:
			items.append(item[0])

		splitquery = query.split(" ")
		i = 0
		for q in splitquery:

			highest = 0
			for row in rows:
				res = row[1]
				splitres = res.split(",")
				score = fuzz.partial_ratio(splitres[0].lower().replace(" ", ""), q.lower().replace(" ", ""))
				if (score > highest):
					highest = score

			higharray = []
			for row in rows:
				res = row[1]
				splitres = res.split(",")
				score = fuzz.partial_ratio(splitres[0].lower().replace(" ", ""), q.lower().replace(" ", ""))
				if (score > highest - 20):
					higharray.append(row)

			rows = higharray

		for item in rows:
			print(item)

		str = 'HUAWEI MateBook D15 (2021), 15.6"",  i5-1135G7, 8GB/512GB (Intel Iris XE)'
		str2 = 'huawei-matebook-d15-2021-156-i5-1135g7-8gb512gb-intel-iris-xe'
		str = str.replace(' ', "zzz").replace('-', "zzz")
		str = re.sub('[\W\ ]+', '', str)
		str = str.replace('zzz', "-").lower()
		str = remove_consec_dash(str)
		# print(str)
		# print(str2)