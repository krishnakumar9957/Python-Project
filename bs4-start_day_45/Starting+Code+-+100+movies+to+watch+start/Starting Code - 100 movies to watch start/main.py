import requests
from bs4 import BeautifulSoup
from requests import Response

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html parser")
print(tittle)




