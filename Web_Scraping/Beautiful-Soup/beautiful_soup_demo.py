from bs4 import BeautifulSoup

with open("website.html") as file:
    site = file.read()

soup = BeautifulSoup(site, "html.parser")

print(soup.title)
print(soup.prettify())