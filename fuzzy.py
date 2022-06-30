#!/usr/bin/env python3
from unittest import skip
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import csv
import sys
import json
import re
import requests

# args = sys.argv[1:]
# args1 = sys.argv[2:]

brand = ["honor", "huawei", "infinix", "nokia", "oppo", "realme", "samsung", "vivo", "xiaomi", "apple"]


def fuzzysussy(pdt_name, data_for_matching ):

		rows = data_for_matching
		
		topsearch = []
		toptopsearch = []
		filter3 = []
		highest = 0; 
		splitquery = (str.split((pdt_name).lower().replace("("," ").replace(")"," ").replace("/"," ").replace("[", " ").replace("]", " ").replace("-"," ").replace(".","-"),' '))

		for row in rows:
			for word in splitquery:
				if splitquery[0] in (row[2].lower()):
					topsearch.append(row)
					break
		
		for row in topsearch:
			for word in splitquery:
				if splitquery[1] in row[2].lower():
					toptopsearch.append(row)
					break

		if (len(toptopsearch)) == 0:
			return (False)

		if (len(toptopsearch) > 3):	
			for row in toptopsearch:
				for word in splitquery:
					if splitquery[2] in row[2].lower():
						filter3.append(row)
						break
		if (len(filter3) == 0):
			topsearch = toptopsearch;
		elif (len(filter3) >= 0):
			topsearch = filter3;

		# Fuzzy Partial ratio through Product Key
		for row in topsearch:
			score = fuzz.partial_ratio(pdt_name, row[2])
			if (score > highest):
				highest = score
				highestrow = row

		# Low Score will run Fuzzy Partial ratio through product name
		if (score < 25):
			for row in topsearch:
				score = fuzz.partial_ratio(pdt_name, row[1])
				if (score > highest):
					highest = score
					highestrow = row

		# Output
		array = []
		array.append(highestrow[1])
		array.append(highestrow[2])
		return(array)