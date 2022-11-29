import requests
import json
import extractModule as em
from bs4 import BeautifulSoup
from termcolor import colored, cprint

vSeedDescUrl = "https://nyaa.si/?s=seeders&o=desc"

vWantedList = [
'Chainsaw Man',
'Spy x Family'
]

def returnFirstPage():
	for item in vSoupCall.find_all('td', {'colspan': '2'}):
		for x in item.find_all('a', href=True):
			vTitle = x.get('title', 'No title attribute')
			vTitle = re.sub(r'\[.+?\]', '', vTitle)
			if "comment" not in vTitle:
				if "1080p" in vTitle:
					cprint(colored(vTitle, 'yellow', attrs=["bold", "underline"]))
				else:
					cprint(colored(vTitle, 'blue'))

def writeResult(pJson, filename):
	with open("{}.json".format(filename), "w") as output:
		json.dump(pJson, output, indent=1)

writeResult(em.extractWantedAnimeMagnetLinks(5, BeautifulSoup(requests.get(vSeedDescUrl).text, 'lxml'), vWantedList), "test_002")