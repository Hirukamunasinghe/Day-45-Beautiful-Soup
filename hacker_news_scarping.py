from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,"html.parser")
#print(soup.title)

#Get the values in order - All the texts,links and the upvotes
articles = soup.find_all(name="a", class_="titlelink")
article_texts =[]
article_links =[]
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]

#Getting the highest amount of article upvotes
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

print(article_texts)
print(article_links)
print(article_upvotes)


