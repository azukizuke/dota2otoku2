import urllib.request
import urllib.error
import time
import json

def convertJson(timeout,url):
	headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
	urlreq=urllib.request.Request(url)
	urlreq=urllib.request.Request(url = url, headers=headers)
	num_try=1
	while True:
		try:
			url_reader = urllib.request.urlopen(urlreq)
			print("json load : " + str(url_reader.getcode()))
			if url_reader.getcode() == 200:
				break
		except urllib.error.HTTPError as e:
			print("HTTPError : " + str(url))
			print("HTTPError : " + str(e.reason))
			print("HTTPError : " + str(e.code))
			time.sleep(timeout*num_try)
			print(num_try)
			num_try+=1
		except urllib.error.URLError:
			print("URLError : " + str(url))
			time.sleep(timeout*num_try)
			print(num_try)
			num_try+=1

	root = json.loads(url_reader.read().decode('utf-8'))
	return root
