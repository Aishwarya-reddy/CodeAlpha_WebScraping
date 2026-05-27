import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Request headers
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Send HTTP request
response = requests.get(url, headers=headers)

# Check if request is successful
if response.status_code == 200:

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Lists to store data
    book_names = []
    prices = []
    ratings = []

    # Find all book containers
    books = soup.find_all("article", class_="product_pod")

    # Extract data from each book
    for book in books:

        # Book title
        name = book.h3.a["title"]

        # Book price
        price = book.find("p", class_="price_color").text.strip()

        # Book rating
        rating = book.p["class"][1]

        # Append data to lists
        book_names.append(name)
        prices.append(price)
        ratings.append(rating)

    # Create DataFrame
    data = pd.DataFrame({
        "Book Name": book_names,
        "Price": prices,
        "Rating": ratings
    })

    # Save data to CSV file
    data.to_csv("books_data.csv", index=False)

    # Display first 5 rows
    print("\nData Scraped Successfully!\n")
    print(data.head())

else:
    print("Failed to fetch website")