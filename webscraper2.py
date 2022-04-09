#TODO:
#do first draft that only gets words from og website
#make second draft that goes to all links website links to that are still at it's domain
#add names of products to data so output can be assigned to real product names?
# handle errors w sites
# how to walk through all without getting caught in an infinite loop or using too much memory?

#notes: 46 and bee caused problems?


from ast import Constant
from pickle import TRUE
from idna import check_label
import requests # web scraping library
import re
import sys
import string

#### FUNCTIONS #####

def is_in_list(element2find, list):
    for element in list:
        if element == element2find:
            return True
    return False

def clean_out_tags(text):
    tag = "<.*>"
    text = re.sub(tag, "", text)
    return text

def keywords_exist(url):
    KEYWORDS = {"disability", "accessibility", "special education"}
    text_object = requests.get(url)
    text = text_object.text.lower()
    for word in KEYWORDS:
        keyword_location = text.find(word)
        if keyword_location != -1:
            return True
    return False

def find_all_links(url):
    links = []
    #if amazon quit
    if url.find("amazon.com") != -1:
        return links

    #find domain
    domain = re.findall("^.*(.com)|(.org)|(.edu)|(.net)|(.technology)", url)[0]


    text_object = requests.get(url)
    text = text_object.text.lower()
    # how should i make this only find single links
    matches = re.findall("<a.*/a>", text)
    for match in matches:
        href = re.search('href=""', match)
        # href should never equal none
        if href == None: continue
        string_start, string_end = href.span()
        link = re.sub('"', "", re.findall('".*"', match[string_start:string_end])[0])
        #if not in domain quit
        if link.find(domain) == -1:
            continue
        else:
            links.append(link)
    return links


def check_all_pages(url, visited_pages, file2write2):
    #base case
    if(is_in_list(url, visited_pages)):
        return
    #not base case
    visited_pages.append(url)
    if keywords_exist(url):
        file2write2.write(url.strip()+","+"True"+"\n")
    links = find_all_links(url)
    for link in links:
        check_all_pages(link)
    




#def search_a_website()


##### END FUNCTIONS ####


# open websites list to read
websites = open("websites2search.txt", "r")
# open txt file to write data to
website_data = open("websitedata.txt", "w")

# save first url
nextLine = websites.readline()
# start scraper loop
counter4printing = 1;
while nextLine != "":
    website_data.write("\n\n"+nextLine.strip()+"\n")
    print("-------------", counter4printing, "WHILE LOOP-------------")
    check_all_pages(nextLine, [], website_data)
    print(nextLine.strip(),"done")

    #final statements
    counter4printing += 1
    nextLine = websites.readline()