# -*- coding: utf-8 -*-
import requests
import time
class BaseCheck():
    def __init__(self, url):
        self.http_proxy  = "http://703069247:Apr*2016@182.94.234.152:3120"
        self.https_proxy = "http://703069247:Apr*2016@182.94.234.152:3120"
        self.ftp_proxy   = "http://703069247:Apr*2016@182.94.234.152:3120"

        self.proxyDict = {
                      "http"  : self.http_proxy,
                      "https" : self.https_proxy,
                      "ftp"   : self.ftp_proxy
                    }
        self.url = url
        def makearr(tsteps):
            global stemps
            global steps
            stemps = {}
            for step in tsteps:
                stemps[step] = { 'start': 0, 'end': 0 }
            steps = tsteps
        makearr(['init','check'])
        def starttime(typ = ""):
            for stemp in stemps:
                if typ == "":
                    stemps[stemp]['start'] = time.time()
                else:
                    stemps[stemp][typ] = time.time()
        starttime()
    def __str__(self):
        return str(self.url)
        
    def getrequests(self):
        #headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
        g=requests.get(self.url,proxies=self.proxyDict, headers={'Referer' : 'https://www.mutualfundindia.com/MF/return/TopFunds?'})
        print "Requested URL           : " + self.url
        print "Request status code     : " + str(g.status_code)
        #print g.content

        stemps['init']['end'] = time.time()
        #print stemps['init']['end'] - stemps['init']['start']
        x= stemps['init']['end'] - stemps['init']['start']
        print "Request Fetch Time      : " + str(x)
        return g


#test=BaseCheck(url='http://google.com')
#test=BaseCheck(url='https://www.amfiindia.com/')

#from lxml import html
#import requests

import xml.etree.ElementTree as ET

test=BaseCheck(url='https://www.mutualfundindia.com/MF/return/TopFundDetails?page=7')
page_root=test.getrequests()

sample = page_root.content
#tree=ET.fromstring(sample.decode('UTF-8'))

#tree = ET.parse(page_root.content)
#root = tree.getroot()

#sample_try1 = sample.replace('–','')

from lxml import etree
htmlpage = etree.HTML(page_root.content)

#for element in htmlpage.iter():
#    print("%s"% (element.attrib))
    
#for element in htmlpage.iter():
#    print("%s - %s"% (element.tag, element.text))

from BeautifulSoup import BeautifulSoup
soup = BeautifulSoup(page_root.content)
import re


comment = soup.findAll(text=re.compile("tr"))

for link in soup.findAll('a'):
    print(link.get('href'))


# to enable pip set the proxy environmental variable : https_proxy=http://703069247:Apr*2016@182.94.234.152:3120


### Web Links for Reference

#https://github.com/search?utf8=%E2%9C%93&q=mutual+funds+india
#https://github.com/krod16/mfIndia
#https://github.com/krod16/mfIndia/blob/master/mfIndia.py
#https://www.reliancemutual.com/InvestorServices/FactsheetsDocuments/Factsheet-January2015.pdf
#https://www.fundsupermart.co.in/main/fundinfo/listManager.tpl
#http://economictimes.indiatimes.com/rshares-banking-etf/mffundinfo/schemeid-7803.cms               <--- Site for scraping details --- Need to check the HTML layout


#http://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
#http://stackoverflow.com/questions/16310803/python-lxml-web-scraping-dealing-with-blank-entries
#http://stackoverflow.com/questions/11804497/python-3-web-scraping-and-javascript-oh-my


#https://www.mutualfundindia.com/MF/return/TopFunds?
#https://www.mutualfundindia.com/MF/Factsheet/Details?id=23431                                     <--- Site for scraping details
#http://stackoverflow.com/questions/28366780/scraping-data-through-paginated-table-using-python
#http://stackoverflow.com/questions/37144370/scraping-pagination-web-with-beautifulsoap-python
#http://stackoverflow.com/questions/28597041/scraping-multiple-paginated-links-with-beautifulsoup-and-requests


#http://toddhayton.com/2015/05/04/scraping-aspnet-pages-with-ajax-pagination/
#http://chrisalbon.com/python/beautiful_soup_html_basics.html
#http://stackoverflow.com/questions/29006848/scrape-data-from-paginated-contents
#http://stackoverflow.com/questions/27678485/scrape-with-beautifulsoup-from-site-that-uses-ajax-pagination-using-python
#https://www.linkedin.com/pulse/python-web-scraping-part-2-how-scrap-embedded-module-igor-onyshchenko



#https://github.com/abhinavsood/mutual-fund-analysis                                            <--- Site for scraping details
#https://github.com/abhinavsood/mutual-fund-analysis/blob/master/00_moneycontrol.py             <--- Site for scraping details
#https://github.com/abhinavsood/mutual-fund-analysis/blob/master/01_amfiindia.py                <--- Site for scraping details


#http://stackoverflow.com/questions/12847965/scrapy-parsing-items-that-are-paginated
#http://stackoverflow.com/questions/28013624/how-to-get-contents-of-hidden-divs-within-an-accordion-block-with-python



#https://www.valueresearchonline.com/funds/fundanalysis.asp?schemecode=15981                    <--- Site for scraping details

    
#http://www.relakhs.com/mutual-fund-manager-top-fund-manager-india/    <--- Site for Advice


#http://www.bloomberg.com/research/stocks/private/snapshot.asp?privcapId=112010116              <--- Site for scraping details
#https://www.linkedin.com/in/krishandaga                                                        <--- Fund Manager Details in Linkedin  


#http://portal.amfiindia.com/spages/NAV0.txt                                                    <--- NAV Details
#https://www.google.co.in/search?q=INF846K01WP8&oq=INF846K01WP8&aqs=chrome..69i57&sourceid=chrome&ie=UTF-8      <--- Google Search for a Fund Index
#https://www.edelweiss.in/mutual-funds/scheme-snapshot/axis-children-s-gift-fund--lock-in--dir-(d)/31647.html        <--- Possible site to scrape --- Review HTML Layout


#https://www.amfiindia.com/research-information/other-data/scheme-details                       <--- Site for scraping details
#https://www.amfiindia.com/downloads                                                            <--- NAV and Scheme Data Downloads


#http://www.moneycontrol.com/mutual-funds/amc-assets-monitor
#http://www.moneycontrol.com/india/mutualfunds/mfinfo/investment_info/MHD1171
#http://www.moneycontrol.com/mf/mfipo/otherschemes.php?manager=Krishan%20Kumar%20Daga     
