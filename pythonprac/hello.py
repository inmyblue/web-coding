import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20220125',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

for tr in trs:
    a_tag = tr.select_one('td.title > div > a') #타이틀가져오기
    if a_tag is not None:
        title = a_tag.text
        rank = tr.select_one('td:nth-child(1) > img')['alt']  # 순위가져오기
        point = tr.select_one('td.point').text  # 평점가져오기

        doc = {
            'title' : title,
            'rank' : rank,
            'point' : point
        }

        db.movies.insert_one(doc)



