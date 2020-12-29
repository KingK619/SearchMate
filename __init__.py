from dotenv import load_dotenv
from calculateTfidf import *
from preprocessing import *
from googleapi import *
from search_results import *
from extractDocx import *
import random
import htmlstrip
from modules import *

logger = Signale() 


def ranks(sample):
    """
    Return the ranks of each element in an integer sample.
    """
    indices = sorted(range(len(sample)), key=lambda i: sample[i])
    return sorted(indices, key=lambda i: indices[i])

def sample_with_minimum_distance(n=40, k=4, d=10):
    """
    Sample of k elements from range(n), with a minimum distance d.
    """
    random.seed(79)
    sample = random.sample(range(n-(k-1)*(d-1)), k)
    if n<=0:
    	return [0]
    else:
    	return [s + (d-1)*r for s, r in zip(sample, ranks(sample))]

# Fucntion to make calls to other functions
def initiating(query):
	load_dotenv()
	logger.info("Finding Please hold tight!!!")
	my_api_key = os.environ.get("API_KEY")
	my_cse_id = os.environ.get("CSE_ID")

	sentenceEnders = re.compile('[.!?]')
	sentenceList = sentenceEnders.split(query)
	linkstoquery=my_dictionary()
	logger.watch("Searching Initiated...\n")
	randomsentence=sample_with_minimum_distance(len(sentenceList)-5,int(len(sentenceList)/5),4)
	for s in randomsentence:
		if s == len(sentenceList):
			continue
		separator = ' '
		end=min(len(sentenceList),s+4)
		search_term=separator.join(sentenceList[s:end])
		x = re.compile(r'\W+', re.UNICODE).split(search_term)
		x = [ele for ele in x if ele != '']
		search_term=''
		search_term=separator.join(x)
		if len(search_term) !=0:
			formatedJson = google_search(search_term, my_api_key, my_cse_id)
			searchResults = my_dictionary() 
			searchResults = google_results(formatedJson)
			for links in searchResults.keys():
				if links in linkstoquery:
					linkstoquery[links]+=1
				else:
					linkstoquery[links]=1
	logger.complete("Searching Completed...\n")
	logger.watch("Calculating Match Score...\n")
	sorted_links = dict( sorted(linkstoquery.items(), key=operator.itemgetter(1),reverse=True))
	count = 0
	results = {}
	logger.watch("Getting Results...")
	spinner = Halo(text='Loading', text_color = "yellow", spinner='dots', animation = 'bounce')
	spinner.start()
	for link in sorted_links.keys():
		count+=1
		if count<15:
			try:
				source = htmlstrip.linkparser(link)
				bowB = word_tokenize(apply_all_preprocessing(source))
			except Exception as err :
				print(err)
				continue

			bowA = word_tokenize(apply_all_preprocessing(query))

			wordSet = set(bowA).union(set(bowB))

			wordDictB = dict.fromkeys(wordSet, 0)
			wordDictA = dict.fromkeys(wordSet, 0)

			wordFreqA(bowA, wordDictA) 
			wordFreqB(bowB, wordDictB) 

			tfBowA = computeTF(wordDictA, bowA)
			tfBowB = computeTF(wordDictB, bowB)
			idfs = computeIDF([wordDictA, wordDictB])
			tfidfBowA = computeTFIDF(tfBowA, idfs)
			tfidfBowB = computeTFIDF(tfBowB, idfs)
			sim = similarity(tfBowA, tfBowB, bowA, bowB) *100
			if sim >= 30:
				results[link] = sim  
		else:
			break
	spinner.stop()
	sorted_results = dict(sorted(results.items(), key=operator.itemgetter(1),reverse=True))
	print("\n\n\n")
	logger.important("\033[1;32;40m FINAL RESULTS ====>")
	for link,score in sorted_results.items():
		logger.important(link,"Url: ")
		logger.info(score," Find Score: ")
	
	print("\n\n")
	logger.success("Run Complete")
	print("\n")
	return sorted_results