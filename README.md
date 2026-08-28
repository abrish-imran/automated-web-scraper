# Automated Multi-Page Web & Lead Scraper

A production-ready Python web scraping pipeline designed to extract, structure, and export multi-page web directory data to clean CSV formats. Built with defensive error handling, network fault tolerance, and rate limiting.

## 📌 Project Overview
- **Target Site:** `books.toscrape.com`
- **Output:** `lead.csv` containing extracted records across multiple paginated pages.
- **Tech Stack:** Python 3, BeautifulSoup4, Requests, CSV module.

## ✨ Key Features
- **Dynamic Multi-Page Scraping:** Automatically navigates through paginated pages using dynamic URL formatting.
- **Defensive Error Handling:** Implements `try-except` blocks to handle missing HTML attributes (`AttributeError`) gracefully without script termination.
- **Network Resilience & Rate Limiting:** Utilizes HTTP request timeouts (`timeout=10`), status validation (`raise_for_status()`), and polite request delays (`time.sleep`) to prevent IP flagging.
- **Structured Data Export:** Outputs parsed records to UTF-8 encoded CSV files using `csv.DictWriter`.

## 🛠️ Project Structure
```text
├── scraper.py          # Main automated extraction script
├── requirements.txt    # Project dependencies
├── lead.csv            # Sample extracted dataset (60 items across 3 pages)
├── .gitignore          # Git exclusion rules
└── README.md           # Project documentation
