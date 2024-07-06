from bs4 import BeautifulSoup

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
print(all_movies)