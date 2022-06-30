import requests


def send_request(session, proxy):
   try:
       response = session.get('http://httpbin.org/ip', proxies={'http': f"http://{proxy}"})
       print(response.json())
   except:
       pass


if __name__ == "__main__":
	with open('Free_Proxy_List.txt', 'r') as file:
		proxies = file.readlines()
		print(proxies)

	with requests.Session() as session:
		for proxy in proxies:
			send_request(session, proxy)