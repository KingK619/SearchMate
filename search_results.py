# script takes json returned by google search and stores links and meta description 
import json
import re

class my_dictionary(dict):           # class of dictionary
		def __init__(self):  
			self = dict()  
		def add(self, key, value):  
			self[key] = value 

def google_results(formatedJson):
	data = json.loads(formatedJson)
	snip=""
	searchResults = my_dictionary()
    
	for a in data['items']:
		link = a["link"]             # store links
		snip = a["htmlSnippet"]		# store meta description	
		clean = re.compile('<.*?>')
		searchResults.key = link
		searchResults.value = re.sub(clean, '', snip)
		searchResults.add(searchResults.key, searchResults.value)  
	return searchResults
