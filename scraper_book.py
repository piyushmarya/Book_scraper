from bs4 import BeautifulSoup
import requests

URL = "http://books.toscrape.com/"

html_content = requests.get(URL).content
#print(html_content)
BOOK_LOCATOR = "li.col-xs-6"
TITLE_LOCATOR = "h3 a"
RATING_LOCATOR = "p.star-rating"
PRICE_LOCATOR = "p.price_color"
LINK_LOCATOR = "h3 a"
parser = BeautifulSoup(html_content,'html.parser')


def find_price(a):
    price = a.select_one(PRICE_LOCATOR)
    return price.string
    

def find_rating(a):
    rating_data = a.select_one(RATING_LOCATOR)
    rating = rating_data.attrs.get('class')
    return ([i for i in rating if i not in "star-rating"])[0]
    
#    print(rating)

def find_title(a):
    title_data = a.select_one(TITLE_LOCATOR)
    title = title_data.attrs['title']
    return title

def find_link(a):
    link_data = a.select_one(LINK_LOCATOR)
    link = link_data.attrs['href']
    return link

if __name__ == "__main__":
    a = parser.select(BOOK_LOCATOR)
    for i in a:
        print(find_price(i) + " " +
        find_rating(i) + " " +
        find_title(i) + " " +
        find_link(i)) 



