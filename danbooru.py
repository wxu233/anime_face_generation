import requests 
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    }
s = requests.Session()


# score:>80 -animated 1girl rating:safe  solo -from_behind -realistic
pa = {'tags':'looking_at_viewer score:>90',#tag
    'page':'1'} #I used my own account to search with more tags, but I cannot provide it here :( 
for p in range(0,72): #pages in Danbooru
    pa['page'] = str(p)
    response = s.get("https://danbooru.donmai.us/posts",params = pa,headers = headers)
    soup = BeautifulSoup(response.content, features='lxml')
    fst = soup.find('div', {"class": "user-disable-cropped-false"})
    snd = fst.find_all('article')
    print(p)
    for e in snd:
        imgurl = e['data-large-file-url']
        imgname =  imgurl.split('/')[-1]
        t = s.get(imgurl, stream=True)
        print(imgurl)
        with open('img1/'+imgname, 'wb') as f:
            f.write(t.content)

while True:
    a = 1