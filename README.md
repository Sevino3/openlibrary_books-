OpenLibrary Books

A Python project that collects book information from the OpenLibrary API, filters books published after 2000, and saves the results in a CSV file.

Features

- Gets book data from the OpenLibrary API
- Filters books published after 2000
- Saves 50 books in CSV format
- Includes book title, authors, and publication year

Requirements

- Python 3
- requests library

How to Run

Install the required library:

pip install requests

Then run:

python main.py

The program creates a file named "books.csv".

Output

The CSV file contains these columns:

- Title
- Authors
- Year

API

Data is collected from the OpenLibrary Search API.
