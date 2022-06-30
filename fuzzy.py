#!/usr/bin/env python3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv
import sys
import json
import re
import requests

args = sys.argv[1:]
query = 'XIAOMI 11T/11T PRO (8/12GB+128GB/256GB) ORIGINAL XIAOMI MALAYSIA'
if len(args) == 1:
	rows = []
	
	with open (args[0], 'r') as file :
		csvreader = csv.reader(file)
		header = next(csvreader)
		for row in csvreader:
			rows.append(row)
		column = []
		cooolumn = []
		for row in rows:
			res = row[1]
			splitres = res.split(",")
			cooolumn.append(splitres)
			column.append(res)
		items = []
		for item in cooolumn:
			items.append(item[0])
		splitquery = query.split(" ")
		i = 0
		for q in splitquery:
			highest = 0
			for item in items:
				# print(item.lower())
				# print(query.lower())
				score = fuzz.partial_ratio(item.lower().replace(" ", ""), q.lower().replace(" ", ""))
				if (score > highest):
					highest = score
					# highesti = item
			# print(highesti)
			higharray = []
			for item in items:
				score = fuzz.partial_ratio(item.lower().replace(" ", ""), q.lower().replace(" ", ""))
				if (score > highest - 20):
					higharray.append(item)
			items = higharray
		for item in items:
			# score = fuzz.partial_ratio(item.lower().replace(" ", ""), query.lower().replace(" ", ""))
			# if (score > highest):
			# 	highest = score
			# 	highesti = item
		# print(highesti)
			print(item)