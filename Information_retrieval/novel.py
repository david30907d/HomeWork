import requests, json, pyprind, sys
from bs4 import BeautifulSoup

# novel = 'https://tw.ixdzs.com/read/0/864/'
novel = sys.argv[1]
web = requests.get(novel)
web.encoding = web.apparent_encoding
web = BeautifulSoup(web.text, "lxml")
result = {}
for i in pyprind.prog_bar(web.select('.chapter')):
	chapter = requests.get(novel + i.select('a')[0]['href'])
	chapter.encoding = chapter.apparent_encoding
	chapter = BeautifulSoup(chapter.text, "lxml")
	result[chapter.select('h1')[0].text] = chapter.select('.content')[0].text

json.dump(result, open(web.select('h1')[0].text + '.json', 'w', encoding='utf-8'))