import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url=input("Enter - ")
hmtl = urllib.request.urlopen(url).read()
soup = BeautifulSoup(hmtl, "html.parser")

tags = soup('span')
spans=[]
for tag in tags:
    tag=tag.contents[0]
    tag=int(tag.text)
    spans.append(tag)
print(sum(spans))