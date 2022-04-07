#TODO:
#do first draft that only gets words from og website
#make second draft that goes to all links website links to that are still at it's domain
#add names of products to data so output can be assigned to real product names?
# add more data about search?


from ast import Constant
import requests # web scraping library
import re
import sys
import string

#### FUNCTIONS #####

def clean_out_tags(text):
    tag = "<.*>"
    re.sub(tag, "", text)
    return text


##### END FUNCTIONS ####

KEYWORDS = {"disability", "accessibility", "special education"}

# open websites list to read
websites = open("websites2search.txt", "r")
# create dict to store if websites match
websites_data = {}

# save first website
nextLine = websites.readline()
# start scraper loop
counter4printing = 1;
while nextLine != None:
    print(counter4printing, "WHILE LOOP--------------------------")
    text_object = requests.get(nextLine)
    text = text_object.text
    sys.stdout.flush()
    text = clean_out_tags(text)
    # matches_keywords = False
    keyword_location = -1
    for word in KEYWORDS:
        keyword_location = text.find(word)
    websites_data[nextLine] = keyword_location;
    print(nextLine,":", keyword_location);
    counter4printing += 1
    nextLine = websites.readline()
    #write results to a file
    #TODO: error on 46

