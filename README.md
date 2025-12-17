# 📰 Google News Scraper (Day 14)

A Python automated bot that scrapes latest news headlines for any given topic and saves them into a structured CSV file. It uses `BeautifulSoup` to parse HTML content effectively.

**Part of the "15 Days, 15 Projects" Challenge.**

## 🚀 Features

* **Custom Search:** User can input any topic (e.g., "Bitcoin", "SpaceX", "Climate Change").
* **Smart Extraction:** Pulls the Headline text and the clickable Link.
* **Data Export:** Saves results immediately to `headlines.csv` for easy viewing in Excel.
* **Bot Protection:** Uses "Headers" to mimic a real browser so Google doesn't block the script.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Requesting:** `requests` (To fetch the webpage).
* **Parsing:** `BeautifulSoup4` (bs4) (To find the data in the HTML jungle).

## ⚙️ Installation

### 1. Install Dependencies
```bash
pip install requests beautifulsoup4
python main.py