import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

# Adding headers
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Sending request
response = requests.get(url, headers=headers)

# Check request status
if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    book_names = []
    prices = []
    ratings = []

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        # Book name
        name = book.h3.a["title"]

        # Price
        price = book.find("p", class_="price_color").text

        # Rating
        rating = book.p["class"][1]

        # Store data
        book_names.append(name)
        prices.append(price)
        ratings.append(rating)

    # Create DataFrame
    data = pd.DataFrame({
        "Book Name": book_names,
        "Price": prices,
        "Rating": ratings
    })

    # Save CSV
    data.to_csv("books_data.csv", index=False)

    print("Data saved successfully!")
    print(data.head())

else:
    print("Failed to fetch website")