from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# html tag locators to find the values inside the specified tags
BOOK_LOCATOR = "li.col-xs-6"
TITLE_LOCATOR = "h3 a"
RATING_LOCATOR = "p.star-rating"
PRICE_LOCATOR = "p.price_color"
LINK_LOCATOR = "h3 a"
PAGE_LOCATOR = "li.current"

# list initialization to store the values found
title = []
rating = []
price = []
link = []


def get_number_pages():
    """
    Returns the total number of pages on the specified website
    """
    url = "http://books.toscrape.com/catalogue/page-1.html"
    html_content = requests.get(url).content
    parser = BeautifulSoup(html_content, "html.parser")
    content = parser.select_one(PAGE_LOCATOR).string
    pattern = "Page [0-9]+ of ([0-9]+)"
    matcher = re.search(pattern, content)
    pages = int(matcher.group(1))
    return pages


def find_price(book_data):
    """
    Returns the price of the specified book
    """
    price_of_book = book_data.select_one(PRICE_LOCATOR)
    return price_of_book.string


def find_rating(book_data):
    """
    Returns the rating of the specified book
    """
    rating_data = book_data.select_one(RATING_LOCATOR)
    rating_of_book = rating_data.attrs.get("class")
    return ([i for i in rating_of_book if i not in "star-rating"])[0]


def find_title(book_data):
    """
    Returns the title of the specified book
    """
    title_data = book_data.select_one(TITLE_LOCATOR)
    title_of_book = title_data.attrs["title"]
    return title_of_book


def find_link(book_data):
    """
    Returns the link of the specified book
    """
    link_data = book_data.select_one(LINK_LOCATOR)
    link_to_book = link_data.attrs["href"]
    return link_to_book


if __name__ == "__main__":
    for page in range(1, get_number_pages() + 1):
        URL = "http://books.toscrape.com/catalogue/page-" + str(page) + ".html"

        # gathering the html content in var html_content for each page
        html_content = requests.get(URL).content
        parser = BeautifulSoup(html_content, "html.parser")

        # var book_data consists of all the books on the i'th page
        all_book_data = parser.select(BOOK_LOCATOR)

        # iterating over every book and finding title,rating,price,link
        for book in all_book_data:
            title.append(find_title(book))
            rating.append(find_rating(book))
            price.append(find_price(book))
            link.append(find_link(book))

    # creating a dataframe of all the data scraped from the website
    main_list = pd.DataFrame(
        {"Title": title, "Rating": rating, "Price": price, "Link": link}
    )
    print(main_list)
