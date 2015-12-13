import requests
from bs4 import BeautifulSoup
import json
import csv
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
				reportjson = "https://hackerone.com/reports/" + reportid + ".json"
				req1 = requests.get(reportjson)
				data = json.loads(req1.content)
				print data['url']
				if 'formatted_bounty' in data.keys():
					cellwriter.writerow([data['id'], data['url'], data['title'].encode('utf-8').strip(), data['formatted_bounty'], data['reporter']['username'].encode('utf-8').strip(),data['team']['handle'].encode('utf-8').strip(),data['created_at'], data['disclosed_at']])
				else:
					cellwriter.writerow([data['id'], data['url'], data['title'].encode('utf-8').strip(), "Bounty Info Not sure", "No Reporter Information FOund",data['team']['handle'].encode('utf-8').strip(),data['created_at'], data['disclosed_at']])
			else:
				pass
	except:
		pass

cellwriter = csv.writer(open('eggs.csv', 'w'))
for x in xrange(1,171):
	url = "https://hackerone.com/hacktivity?page=" + str(x)
	find_latest_id(url)
	print "Checking on " + url
