from bs4 import BeautifulSoup
import requests
import re

html_raw = input("type the url: ")
html_process = requests.get(html_raw)
html_doc = html_process.content
soup = BeautifulSoup(html_doc,'html.parser')
url_set = set()

for link in soup.find_all("a",class_= "btn btn-xs btn-danger"):
    url = link.get('href')
    a = link.parent.parent.parent.parent.parent.find_all("li")
    p = re.compile("^<li>\s|<br/>",)
    t = p.split(str(a[0]))
    r = requests.get(url)
    mp4 = r.content
    correct_t = t[1][1:].replace('</li>','')
    correct_t = correct_t.replace('\n','')
    correct_t = correct_t.replace('/','_')
    correct_t = correct_t.replace(' ','')
    if correct_t in url_set:
        continue
    else:
        url_set.add(correct_t)
        print(correct_t)
        f = open('{}.mp4'.format(correct_t),'wb') #write bytes
        f.write(mp4)
        f.close
