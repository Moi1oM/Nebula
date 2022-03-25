import requests
from bs4 import BeautifulSoup
from function import extract_info
import csv

file=open('webtoon.csv',mode="w",newline='')

writer=csv.writer(file)
writer.writerow(["title","artist","stars"])

web_URL=f"https://comic.naver.com/webtoon/weekdayList?week=wed"
web_html=requests.get(web_URL)
web_soup=BeautifulSoup(web_html.text,"html.parser")

web_list_box=web_soup.find("ul",{"class","img_list"}).find_all("li")
d=[]
d=extract_info(web_list_box)

for i in d:
    row=[]
    row.append(i['title'])
    row.append(i['artist'])
    row.append(i['stars'])
    print(row)
    writer.writerow(row)
