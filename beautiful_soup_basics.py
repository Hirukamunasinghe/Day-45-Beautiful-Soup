from bs4 import BeautifulSoup
#import lxml

with open("website.html","r",encoding="utf8") as webpage:
     contents = webpage.read()

soup = BeautifulSoup(contents,"html.parser")

#Getting the title
print(soup.title)
# #Title name (Name of title tag)
print(soup.title.name)
# #String in the title tag
print(soup.title.string)
#Entire html/soup object with indentation
print(soup.prettify())
#Get the link/anchor tag
print(soup.a)
#Get the first list
print(soup.li)
#Get the first paragraph
print(soup.p)

#GET ALL anchor tags
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

#GET ONLY THE TEXT IN ANCHOR TAG
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1",id="name")
print(heading)

section_heading = soup.find(name="h3",class_ ="heading")
print(section_heading)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(selector=".heading")
print(headings)