#TODO:
#do first draft that only gets words from og website
#make second draft that goes to all links website links to that are still at it's domain
#add names of products to data so output can be assigned to real product names?
# handle errors w sites
# how to walk through all without getting caught in an infinite loop or using too much memory?

#notes: 46 and bee caused problems?


from ast import Constant
from pickle import TRUE
import requests # web scraping library
import re
import sys
import string

#### FUNCTIONS #####

def clean_out_tags(text):
    tag = ".*</head>"
    text = re.sub(tag, "", text)
    # print(text[:1000])
    return text

#def search_a_website()


##### END FUNCTIONS ####

KEYWORDS = {"disability", "accessibility", "special education"}

# open websites list to read
websites = open("websites2search.txt", "r")
# open txt file to write data to
website_data = open("websitedata.txt", "w")

# save first url
nextLine = websites.readline()
# start scraper loop
counter4printing = 1;
while nextLine != "":
    print("-------------", counter4printing, "WHILE LOOP-------------")
    text_object = requests.get(nextLine)
    text = text_object.text.lower()
    text = clean_out_tags(text)
    # matches_keywords = False
    keyword_locations = {}
    i=0;
    for word in KEYWORDS:
        keyword_locations[i] = text.find(word)
        i += 1
    #TODO: capture location of each keyword appearance?
    print(nextLine.strip(),":", keyword_locations);

    #write results to a file
    website_contains_word = False
    for number in keyword_locations:
        if number != 0:
            website_contains_word = True
    website_data.write("----------------"+nextLine.strip()+","+str(website_contains_word)+"\n"+"----------------");
    counter4printing += 1
    nextLine = websites.readline()


