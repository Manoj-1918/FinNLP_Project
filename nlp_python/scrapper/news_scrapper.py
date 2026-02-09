import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

HEADLINES_FILE = "data/raw_headlines.csv"
HEADERS = {"User-Agent": "Mozilla/5.0"}



def scrape_company_site(company):
    headlines = []

    if company.lower() == "tcs":
        url = "https://www.tcs.com/newsroom"
        soup = BeautifulSoup(requests.get(url, headers=HEADERS).text, "html.parser")

        for h in soup.find_all("h3"):
            text = h.get_text(strip=True)
            if len(text) > 25:
                headlines.append(text)

    return headlines




def scrape_economic_times(company):
    headlines = []
    url = f"https://economictimes.indiatimes.com/topic/{company}"
    soup = BeautifulSoup(requests.get(url, headers=HEADERS).text, "html.parser")

    for h in soup.find_all("a"):
        text = h.get_text(strip=True)
        if company.lower() in text.lower() and len(text) > 25:
            headlines.append(text)

    return headlines




def scrape_moneycontrol(company):
    headlines = []
    url = f"https://www.moneycontrol.com/news/tags/{company.lower()}.html"
    soup = BeautifulSoup(requests.get(url, headers=HEADERS).text, "html.parser")

    for h in soup.find_all("h2"):
        text = h.get_text(strip=True)
        if company.lower() in text.lower() and len(text) > 25:
            headlines.append(text)

    return headlines




def scrape_business_standard(company):
    headlines = []
    url = f"https://www.business-standard.com/search?type=news&q={company}"
    soup = BeautifulSoup(requests.get(url, headers=HEADERS).text, "html.parser")

    for h in soup.find_all("h2"):
        text = h.get_text(strip=True)
        if company.lower() in text.lower() and len(text) > 25:
            headlines.append(text)

    return headlines




def scrape_company_news(company_name):
    all_headlines = []

    all_headlines += scrape_company_site(company_name)
    all_headlines += scrape_economic_times(company_name)
    all_headlines += scrape_moneycontrol(company_name)
    all_headlines += scrape_business_standard(company_name)

    # Clean + Deduplicate
    all_headlines = list(set(all_headlines))

    if not all_headlines:
        raise ValueError("No headlines scraped for this company")

    df = pd.DataFrame({"headline": all_headlines})

    os.makedirs(os.path.dirname(HEADLINES_FILE), exist_ok=True)
    df.to_csv(HEADLINES_FILE, index=False, encoding="utf-8")

    return df

#scrape_company_news("TCS")
