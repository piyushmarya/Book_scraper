from bs4 import BeautifulSoup
import requests

URL = "http://books.toscrape.com/"

html_content = requests.get(URL).content
#print(html_content)

parser = BeautifulSoup(html_content,'html.parser')


def find_price(a):
    price = a.select_one(price_locator)
    print(price.string)
    

def find_rating(a):
    rating_data = a.select_one(rating_locator)
    rating = rating_data.attrs.get('class')
    print([i for i in rating if i not in "star-rating"])
    
#    print(rating)

def find_title(a):
    title_data = a.select_one(title_locator)
    print(title_data)
    title = title_data.attrs.get('title')
    print(title)

if __name__ == "__main__":
    book_locator = "li.col-xs-6"
    title_locator = "a"
    rating_locator = "p.star-rating"
    price_locator = "p.price_color"
    a = parser.select(book_locator)
    for i in a:
#        find_price(i)
#        find_rating(i)
         find_title(i)


