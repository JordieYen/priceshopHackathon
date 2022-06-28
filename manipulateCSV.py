import csv
import sys

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()		Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

def testarrays():
	array = []
	test = ["hello za", "warudo da zee"]

	array.append("apple");
	array.append("bottom");
	array.append("jeans");
	array.append(test);
	for x in array:
  		print(x)

def main():
	header = ['name', 'area', 'country_code2', 'country_code3']
	data = [
		['Albania', 28748, 'AL', 'ALB'],
		['Algeria', 2381741, 'DZ', 'DZA'],
		['American Samoa', 199, 'AS', 'ASM'],
		['Andorra', 468, 'AD', 'AND'],
		['Angola', 1246700, 'AO', 'AGO']
	]
	test = ["Za Warudo", 3242, "ZW", "43"]
	data.append(test)
	with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(data)

if __name__ == '__main__':
    main()