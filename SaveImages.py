#!/usr/bin/env python
from bs4 import BeautifulSoup as bs
import urlparse
from urllib2 import urlopen
from urllib import urlretrieve
import os
import sys
from threading import Thread

def download_parellel(function,images,output):
    for i in images:
        Thread(target=function,args=(i,output,)).start()
    

def download(image,output):
    print image["src"]
    filename = image["src"].split("/")[-1]
    outpath = os.path.join(output, filename)   
    urlretrieve(image["src"], outpath)
       

def main(url,output):
    soup = bs(urlopen(url)) 
    parsed = list(urlparse.urlparse(url))    
    images = list(soup.findAll("img"))
    download_parellel(download,images,output)
    
if __name__ == "__main__":
    url = sys.argv[-1]
    output = "/Users/rkarth/"
    main(url, output)

    
