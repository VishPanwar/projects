#script to count the frequency of words in a given url page
import requests
from bs4 import BeautifulSoup
import operator

def world_lists(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code,"lxml")
    for p_text in soup.findAll('a',{'class','result-title hdrlnk'}):
        content = p_text.string
        if content is not None:
            words = content.lower().split()
        for each_words in words:
            word_list.append(each_words)
    clean_up_list(word_list)

def clean_up_list(words_list):
    clean_up_list = []
    for word in words_list:
        symbols = "!@#$%^&*()_+<>:\"{}[].,;-'•/"
        for i in range(len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_up_list.append(word)
    create_Map(clean_up_list)

def create_Map(clean_up_list):
    word_count = {}
    for word in clean_up_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for k,v in sorted(word_count.items(),key= operator.itemgetter(1)):
        print(k,v)



world_lists("https://cincinnati.craigslist.org/d/rooms-shares/search/roo")
