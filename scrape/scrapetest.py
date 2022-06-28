from bs4 import BeautifulSoup
import json,re,requests

url = 'https://www.lazada.com.my/products/honor-magicbook-x15-i3-2021-space-grey-8gb-ram-256gb-original-1-year-warranty-by-honor-malaysia-i2608649455-s11730638464.html?mp=1&freeshipping=1'
response = requests.get(url)

d = json.loads(re.search(r'var __moduleData__ = ({.*})', response.text).group(1))
print(json.dumps(d['data']['root']['fields']['skuInfos'], indent=4))