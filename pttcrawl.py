#-*- coding: utf-8 -*-　　 
#-*- coding: cp950 -*-

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re   
import os
import sys

def downloading(articles):
    for art in articles:
        print(art.text,art['href'])
        if not os.path.isdir(os.path.join('crwaler_pitcure', art.text)):
            os.mkdir(os.path.join('crwaler_pitcure',art.text))
            
        res = requests.get('https://www.ptt.cc' + art['href'])
        images = imgur_file.findall(res.text)
        print(images)
        for image in set(images):
            ID = re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))',image).group(1)
            print(ID)
            urlretrieve(image,os.path.join('crwaler_pitcure', art.text, ID))


def pttbeautycrawler(page=3):
    if not os.path.isdir('crwaler_pitcure'):
        os.mkdir('crwaler_pitcure')
    #網頁連結    
    url = 'https://www.ptt.cc/bbs/Beauty/index.html'
    for round in range(page):

        res = requests.get(url)
        #analysis html language
        soup = BeautifulSoup(res.text,'html.parser')
        #title name
        articles=soup.select('div.title a')
        #上一頁連結
        paging = soup.select('div.btn-group-paging a')

        nexturl = 'https://www.ptt.cc' + paging[1]['href']

        downloading(articles)
        
        url = nexturl

        

imgur_file =re.compile('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif)')
#print(sys.argv)
#print(int(sys.argv[1]))
pttbeautycrawler(int(sys.argv[1]))
