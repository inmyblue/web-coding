import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

song_list = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for s_list in song_list:
    rank = s_list.select_one('td.number').get_text()
    rank = rank[0:2].strip()

    title = s_list.select_one('td.info > a.title.ellipsis').get_text().strip()
    artist = s_list.select_one('td.info > a.artist.ellipsis').get_text().strip()

    print(rank, title, artist)