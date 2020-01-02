from bs4 import BeautifulSoup
import requests
import pandas as pd



#print(html_content)
BOOK_LOCATOR = "li.col-xs-6"
TITLE_LOCATOR = "h3 a"
RATING_LOCATOR = "p.star-rating"
PRICE_LOCATOR = "p.price_color"
LINK_LOCATOR = "h3 a"
title =[]
rating = []
price = []
link = []

def get_number_pages():
    URL = "http://books.toscrape.com/catalogue/page-1.html"
    html_content = requests.get(URL).content
    parser = BeautifulSoup(html_content,'html.parser')
    #print((parser.select_one("li.current").string).split("Page"))[3]
    return 50


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
    for i in range(int(get_number_pages())):
        URL = "http://books.toscrape.com/catalogue/page-"+str(i)+".html"
        html_content = requests.get(URL).content
        parser = BeautifulSoup(html_content,'html.parser')
        a = parser.select(BOOK_LOCATOR)
        for i in a:
            title.append(find_title(i))
            rating.append(find_rating(i))
            price.append(find_price(i))
            link.append(find_link(i)) 
    mainlist=pd.DataFrame({'Title':title,'Rating':rating,'Price':price,'Link':link})
    print(mainlist)



