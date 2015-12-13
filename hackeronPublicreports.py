import requests
from bs4 import BeautifulSoup
import json
dictbugs = {}



def find_latest_id(url):
	try:
		latest_reportid = 0
		req = requests.get(url)
		html_doc = req.content
		soup = BeautifulSoup(html_doc)
		for tag in soup.find_all('a'):
			if "report" in tag.get('href'):
				reportid = tag.get('href').split("/")[2]
				dictbugs[reportid] = tag.text
			else:
				pass
	except:
		pass

for x in xrange(1,171):
	url = "https://hackerone.com/hacktivity?page=" + str(x)
	find_latest_id(url)
	print "Checking on" + url

#print dictbugs

f = open("reports.csv", 'w')
for key in dictbugs:
	text = "https://hackerone.com/reports/" +key + "," + dictbugs[key] + "\n"
	f.write(text)


		

#for x in xrange(1,):
#	req = requests.get("https://hackerone.com/reports/104028")
