import requests
import json
from bs4 import BeautifulSoup


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
        self.search_request_header = {

                "Host"               : "www.amfiindia.com",
                "Connection"         : "keep-alive",
                "Accept"             : "*/*",
                "Origin"             : "https://www.amfiindia.com",
                "X-Requested-With"   : "XMLHttpRequest",
                "User-Agent"         : "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                "Content-Type"       : "application/x-www-form-urlencoded; charset=UTF-8",
                "Referer"            : "https://www.amfiindia.com/net-asset-value/nav-history",
                "Accept-Encoding"    : "gzip, deflate, br",
                "Accept-Language"    : "en-US,en;q=0.8"
#                "Cookie"             : "__utma=57940026.1740075287.1468231823.1469029856.1469703676.6; __utmc=57940026; __utmz=57940026.1469703676.6.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)"
                    
            }
            
        self.search_request_data = {

                "ID"                 : "53",
                    
            }            
            
    def getrequests(self):
        gheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', }
        g=requests.get(self.url,proxies=self.proxyDict, headers=gheaders)
        print "Requested URL           : " + self.url
        print "Request status code     : " + str(g.status_code)
        return g

    def postrequests(self):
#        pheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'X-Requested-With': 'XMLHttpRequest'}
        p=requests.post(self.url, data= self.search_request_data,  headers=self.search_request_header)
        print "Requested URL           : " + self.url
        print "Request status code     : " + str(p.status_code)
        return p

test=BaseCheck(url='https://www.amfiindia.com/modules/NavHistorySchemeNav')
page_root=test.postrequests()
