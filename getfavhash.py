#!/usr/bin/python3
import mmh3
import requests
import codecs
import sys

def gethash(url):
	response = requests.get(url)
	if response.status_code != 200 :
		print(f"error: status code is {response.status_code} and is not 200! ")
	else:
		if response.headers["Content-Type"] != "text/html":   
			favicon = codecs.encode(response.content,"base64")
			hash = mmh3.hash(favicon)
			print(hash)
		else:
			print("error: content-type not for a icon!")

	# response = requests.get(url)
	# favicon = codecs.encode(response.content,"base64")
	# hash = mmh3.hash(favicon)

if len(sys.argv) != 2:
	print("error: i need an url!")
	sys.exit()
if not "https://" in sys.argv[1] or "http://" in sys.argv[1]:
    print("error: url must contains scheme (like http or https) !")
else:
	if "favicon.ico" in sys.argv[1]:
		gethash(sys.argv[1])
	else:
		if sys.argv[1][len(sys.argv[1])-1:] == "/":
			gethash(sys.argv[1]+"favicon.ico")
		else:
			gethash(sys.argv[1]+"/favicon.ico")

