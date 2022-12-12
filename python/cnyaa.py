#!/usr/bin/env python3

import json, extract as em
from termcolor import colored, cprint

vSeedDescUrl = "https://nyaa.si/?s=seeders&o=desc"

vWantedList = [
'Chainsaw Man',
'Spy x Family'
]

def writeResult(pJson, filename):
	with open("{}.json".format(filename), "w") as output:
		json.dump(pJson, output, indent=1)
