import requests
import time
from bs4 import BeautifulSoup

def createLink(input):
    split = input.split(" ")
    website = "https://www.quodb.com/search/"
    for x in split:
        website = website + x + "%20"
    website = website[:-3]
    return website

def QuoteToMovie(quote):
    from selenium import webdriver
    url = createLink(quote)
    webdriver = webdriver.Chrome()
    webdriver.get(url)
    time.sleep(0.002)

    html = BeautifulSoup(webdriver.page_source,'html.parser')
    webdriver.close()
    results = html.find(id="results_table")

    if html == None or results == None:
        return []

    times = html.findAll(class_="editable editable-click editable-empty editable-open time")
    rows = results.findAll(lambda tag: tag.name=='tr')

    arr = []
    for i in range(0, int(len(rows)/2)):
        arr.append([rows[i*2]['data-title'], times[i].getText()])

    return arr







