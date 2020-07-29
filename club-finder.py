import requests
from bs4 import BeautifulSoup

clubs = requests.get('https://usatt.simplycompete.com/c/d')
clubSoup = BeautifulSoup(clubs.text, 'html.parser')

data = clubSoup.find_all('script')

def findIn(thing, data):
	for i in data:
		for content in i.contents:
			if thing in content:
				return content


found = findIn('window.markerData', data).replace('window.markerData =', '')
print(found)
