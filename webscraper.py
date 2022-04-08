#TODO:
#OFF BY ONE ERROR...
#do first draft that only gets words from og website
#make second draft that goes to all links website links to that are still at it's domain
#add names of products to data so output can be assigned to real product names?
# add more data about search?
# handle errors w sites

#notes: 46 and bee caused problems?


from ast import Constant
import requests # web scraping library
import re
import sys
import string

#### FUNCTIONS #####

def clean_out_tags(text):
    tag = "<.*>"
    text = re.sub(tag, "", text)
    return text


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
    text = text_object.text
    #text = clean_out_tags(text)
    # matches_keywords = False
    keyword_location = -1
    for word in KEYWORDS:
        keyword_location = text.find(word)
    #TODO: capture location of each keyword appearance?
    print(nextLine.strip(),":", keyword_location);

    #write results to a file
    website_data.write(nextLine.strip()+","+str(keyword_location)+"\n");
    counter4printing += 1
    nextLine = websites.readline()


