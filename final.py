# Imports
import requests    
import csv       
import time       

# Configuration
API_KEY = "DhDN5SyqF2WdP6clEelwsi3oRY9mkA4R"
BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
OUTPUT_FILE = "nyt_ai_full.csv"
WAIT_SECONDS = 10

# Define keywords, years and months
KEYWORDS = ["AI ethics", "artificial intelligence"]
YEARS = [2020, 2024]
MONTHS = range(1, 13)  
MAX_PAGES = 5 # Max 5 pages

# Fetches article headlines for a given month/year/keyword across multiple pages
def fetch_articles(year, month, keyword):
    all_titles = []

    for page in range(MAX_PAGES):
        start = f"{year}{month:02d}01"
        end = f"{year + 1}0101" if month == 12 else f"{year}{month + 1:02d}01"

        params = {
            "q": keyword,
            "begin_date": start,
            "end_date": end,
            "api-key": API_KEY,
            "page": page
        }

        response = requests.get(BASE_URL, params=params)

        data = response.json()
        docs = data.get("response", {}).get("docs", [])
        if not docs:
            break

        titles = [doc["headline"]["main"] for doc in docs]
        all_titles.extend(titles)
        time.sleep(WAIT_SECONDS)

    return len(all_titles), all_titles

# Goes through each keyword and month collects article data and writes it to a CSV
def save_articles():
    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "keyword", "title", "monthly_count"])

        for keyword in KEYWORDS:
            for year in YEARS:
                for month in MONTHS:
                    print(f" Searching '{keyword}' — {year}-{month:02d}")
                    count, titles = fetch_articles(year, month, keyword)
                    date_str = f"{year}-{month:02d}"
                    count_label = f" Articles found this month: {count}"

                    if not titles:
                        writer.writerow([date_str, keyword, "No articles found", count_label])
                    else:
                        for title in titles:
                            writer.writerow([date_str, keyword, title, count_label])

    print(f"\n Results saved to '{OUTPUT_FILE}'")

# Start the process of collecting and saving articles
save_articles()
