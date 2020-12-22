import re, nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import FreqDist, word_tokenize
from num2words import num2words

"""
    Function to clean text of websites, email addresess and any punctuation
    We also lower case the text
"""
def clean_text(text):
    text = re.sub("((\S+)?(http(s)?)(\S+))|((\S+)?(www)(\S+))|((\S+)?(\@)(\S+)?)", " ", text)
    symbols = "!\"#$%&()*+-./:;<=>?@[\]^_`{|}~',\n"
    for i in symbols:
        text = text.replace(i, ' ')    
    return text.lower()

    """
    Function that removes all stopwords from text
    """
def remove_stop_words(text):
    stop_words = stopwords.words('english')
    words = word_tokenize(str(text))
    new_text=""
    for word in words:
        if word not in stop_words:
            new_text = new_text + " " + word
    return new_text

def single_character(text):
    new_text = ""
    words = word_tokenize(str(text))
    for w in words:
        if len(w) > 1:
            new_text = new_text + " " + w
    return new_text   

"""
    Function to stem words, so plural and singular are treated the same
    """
def stem_words(text):
    stemmer= PorterStemmer()
    tokens = word_tokenize(str(text))
    new_text = ""
    for w in tokens:
        new_text = new_text + " " + stemmer.stem(w)
    return new_text


def convert_numbers(text):
    tokens = word_tokenize(str(text))
    new_text = ""
    for w in tokens:
        try:
            w = num2words(int(w))
        except:
            pass
        new_text = new_text + " " + w
    new_text = new_text.replace("-", " ")
    return new_text


def apply_all_preprocessing(text):
    text = clean_text(text)
    text = single_character(text)
    text = remove_stop_words(text)
    text = convert_numbers(text)
    text = stem_words(text)
    text = convert_numbers(text)
    text = stem_words(text)
    text = clean_text(text)
    text = remove_stop_words(text)
    return text
    
