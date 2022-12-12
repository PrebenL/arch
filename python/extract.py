import re, requests
from bs4 import BeautifulSoup
from termcolor import colored, cprint

def extractCall(pBaseUrl):
	return BeautifulSoup(requests.get(pBaseUrl).text, 'lxml')

def extractFirstPage(pCall):
	for item in pCall.find_all('td', {'colspan': '2'}):
		for x in item.find_all('a', href=True):
			vTitle = re.sub(r'\[.+?\]', '', x.get('title', 'No title attribute'))
			if "comment" not in vTitle:
				if "1080p" in vTitle:
					#Yellow for 1080p.
					cprint(colored(vTitle, 'yellow', attrs=["bold", "underline"]))
				else:
					#Blue for 720p or less.
					cprint(colored(vTitle, 'blue'))

def extractTitleFromHtml(pHtml):
	vStartTag = pHtml.find('td', {'colspan': '2'})
	for x in vStartTag.find_all('a', href=True):
		if "comment" not in x['title']:
			vMatch = x.get('title', 'No title attribute')
			vMarkup = re.sub(r'\[.+?\]', '', vMatch).split(' - ')
			extractedTitle = '{0} - {1}'.format(vMarkup[0].strip(), vMarkup[1].replace(' ', ''))
	return extractedTitle

def extractMagnetLinkFromHtml(pHtml):
	vStartTag = pHtml.find('td', {'class': 'text-center'})
	for x in vStartTag.find_all('a', href=True):
		if "download" not in x:
			extractedLink = x['href']	
	return extractedLink

def extractWantedAnimeMagnetLinks(pLimit, pCall, pWantedList):
	vResult = {}
	vFind_TBody = pCall.find('tbody')
	for x in vFind_TBody.find_all('tr', {'class': 'success'}, limit=pLimit):
		vTitle = extractTitleFromHtml(x)
		vLink = extractMagnetLinkFromHtml(x)
		for i in range(len(pWantedList)):
			if pWantedList[i] in vTitle:
				vResult[vTitle] = vLink
	return vResult

def extractAnimeMpInfo(pBaseUrl, pPages):
	vEpisodeLib = {}
	for page in range(1, int(pPages)):
		vMainSet = BeautifulSoup(requests.get(pBaseUrl + str(page)).text,'lxml').find(
			'ul', {'class': 'items'})
		for x in vMainSet.find_all("li"):
			vEpisodeLib[x.find("p", class_='name').a['title']] = x.find("p", class_='episode').get_text()
		return vEpisodeLib

def extractSpecificMagnetLinks(pName, pQualityFilter, pLimit, pFilename):
	vUrl = 'https://nyaa.si/?q={}&f=0&c=0_0&s=seeders&o=desc'.format(pName.replace(' ', '+'))
	vFind_TBody = extractCall(vUrl).find('tbody')
	f = open(pFilename, 'a')
	for x in vFind_TBody.find_all('tr', {'class': 'success'}, limit=pLimit):
		if pQualityFilter in extractTitleFromHtml(x) and pName in extractTitleFromHtml(x):
			f.write(extractMagnetLinkFromHtml(x) + ',\n')
	f.close()
