# script to strip given text from HTML tags
# usecase: Content from webpages recovered may have stray HTML tags, like <b> or <i>

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from signalepy import Signale
logger = Signale() 

def linkparser(link):
	url = link
	try:
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		html = urlopen(req).read()
		soup = BeautifulSoup(html, features="lxml")

		for script in soup(["script", "style", "head", "a", "footer"]):
		    script.decompose()

		text = soup.get_text()

		lines = (line.strip() for line in text.splitlines())
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		text = '\n'.join(chunk for chunk in chunks if chunk)
		return text

	except Exception as err :
		print("\n")
		logger.debug(link, err)
