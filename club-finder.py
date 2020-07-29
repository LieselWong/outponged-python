import requests
from bs4 import BeautifulSoup

clubs = requests.get('https://usatt.simplycompete.com/c/d/?max=1000')
clubSoup = BeautifulSoup(clubs.text, 'html.parser')

data = clubSoup.find_all('script')

clubList = []

def findIn(thing, data):
	for i in data:
		for content in i.contents:
			if thing in content:
				return content


found = findIn('window.markerData', data).replace('window.markerData =', '').replace('{', '[').replace('}',']').replace('\n','').replace('      ','').replace('],','').split('[')

for i in found:
	indList = []
	i = i.split(',')
	for element in i:
		if ('markerName' in element) or ('addressLine1' in element) or ('addressCityState' in element):
			indList.append(element)
	clubList.append(indList)

for i in clubList:
	print(i)
	print('\n\n')

print(len(clubList))
