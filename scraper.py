import csv
import os
import time
import requests
from bs4 import BeautifulSoup

# ==========================================
# SETUP DIRECTORIES & RELATIVE PATHS
# ==========================================
# Determines the folder where scraper.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Defines a relative path to save lead.csv in the exact same directory as scraper.py
CSV_FILENAME = os.path.join(BASE_DIR, "lead.csv")

all_leads = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# ==========================================
# MULTI-PAGE EXTRACTION & DEFENSIVE SCRAPING
# ==========================================
for page in range(1, 4):
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    print(f"Scraping page {page}...")

    # 1. Safe HTTP Request & Network Defense
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Check for 4xx or 5xx HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Warning: Failed to fetch page {page}. Error: {e}")
        continue  # Skip gracefully to the next page

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    # 2. Extract Data for Each Book Safely
    for book in books:
        # Safe Title Extraction
        try:
            title = book.find("h3").find("a")["title"]
        except (AttributeError, TypeError, KeyError):
            title = "N/A"

        # Safe Price Extraction
        try:
            price = book.find("p", class_="price_color").text.strip()
        except AttributeError:
            price = "N/A"

        # Safe Availability Extraction
        try:
            availability = book.find("p", class_="instock availability").text.strip()
        except AttributeError:
            availability = "N/A"

        # Structuring data into dictionary card
        lead_card = {
            "Title": title,
            "Price": price,
            "Availability": availability
        }

        all_leads.append(lead_card)

    # Polite delay between page requests
    time.sleep(1)

print(f"\nSuccessfully collected {len(all_leads)} items across pages!\n")

# ==========================================
# EXPORT TO CSV USING RELATIVE PATH
# ==========================================
with open(CSV_FILENAME, mode="w", newline="", encoding="utf-8") as file:
    fieldnames = ["Title", "Price", "Availability"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(all_leads)

print(f"Done! All data saved securely to relative path: '{CSV_FILENAME}'.")
