import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://books.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    book_names = []
    prices = []
    ratings = []
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        name = book.h3.a["title"]
        price = (
            book.find("p", class_="price_color")
            .text
            .strip()
            .replace("Â£", "")
        )
        rating = book.p["class"][1]

        book_names.append(name)
        prices.append(price)
        ratings.append(rating)

    data = pd.DataFrame({
        "Book Name": book_names,
        "Price": prices,
        "Rating": ratings
    })
    data.to_csv("books_data.csv", index=False)
    print("\nData Scraped Successfully!\n")
    print(data.head())

else:
    print("Failed to fetch website")