all:
	Python3 printCSV.py csv/LazadaLinks.csv csv/Dataformatching.csv > csv/Output.csv
merchant:
	Python3 GetMerchantLinks.py csv/Merchantlinks.csv > csv/Links.csv
test:
	Python3 printCSV.py csv/test.csv csv/Dataformatching.csv > csv/long.csv
