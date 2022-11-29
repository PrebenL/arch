import re

def extractTitleFromHtml(pHtml):
	vStartTag = pHtml.find('td', {'colspan': '2'})
	for x in vStartTag.find_all('a', href=True):
		if "comment" not in x['title']:
			vMatch = x.get('title', 'No title attribute')
			vMarkup = re.sub(r'\[.+?\]', '', vMatch).split(' - ')
			extractedTitle = '{0} - {1}'.format(vMarkup[0].strip(), vMarkup[1].replace(' ', ''))
			#extractedTitle = vMarkup

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
	#5 items
	for x in vFind_TBody.find_all('tr', {'class': 'success'}, limit=pLimit):
		vTitle = extractTitleFromHtml(x)
		vLink = extractMagnetLinkFromHtml(x)
		for i in range(len(pWantedList)):
			if pWantedList[i] in vTitle:
				vResult[vTitle] = vLink
	
	return vResult