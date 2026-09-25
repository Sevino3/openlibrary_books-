import requests
import csv

API_URL = "https://openlibrary.org/search.json"

params = {
    "q": "python programming",
    "limit": 100
}

response = requests.get(API_URL, params=params, timeout=30)
response.raise_for_status()

data = response.json()

books = []

for book in data["docs"]:
    year = book.get("first_publish_year")

    if year and year > 2000:
        title = book.get("title", "Unknown")
        authors = ", ".join(book.get("author_name", ["Unknown"]))

        books.append([title, authors, year])

        if len(books) == 50:
            break

with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)

    writer.writerow(["Title", "Authors", "Year"])
    writer.writerows(books)

print(f"{len(books)} books saved to books.csv")
