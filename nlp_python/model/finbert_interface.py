import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

# Import your scraper function
from nlp_python.scrapper.news_scrapper import scrape_company_news

# FINBERT SETUP 

MODEL_NAME = "ProsusAI/finbert"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

labels = ["negative", "neutral", "positive"]

#  ANALYSIS FUNCTION 

def analyze_news(company_name: str):
    """
    1. Scrapes company-related headlines
    2. Runs FinBERT sentiment analysis
    3. Returns aggregated sentiment result
    """

    # Step 1: Scrape headlines dynamically
    df = scrape_company_news(company_name)

    if df.empty or "headline" not in df.columns:
        raise ValueError("No headlines available for sentiment analysis")

    scores = {
        "positive": 0,
        "neutral": 0,
        "negative": 0
    }

    # Step 2: Run FinBERT
    for text in df["headline"].dropna().head(70):

        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=512
        )

        with torch.no_grad():
            outputs = model(**inputs)

        prediction = torch.argmax(outputs.logits).item()
        scores[labels[prediction]] += 1

    # Step 3: Compute overall trend
    total = sum(scores.values())
    sentiment_score = (scores["positive"] - scores["negative"]) / max(total, 1)

    if sentiment_score > 0.3:
        trend = "Positive Outlook"
    elif sentiment_score < -0.3:
        trend = "Negative Outlook"
    else:
        trend = "Stable Outlook"

    # Step 4: Return JSON-compatible result
    return {
        "positive": scores["positive"],
        "neutral": scores["neutral"],
        "negative": scores["negative"],
        "overall_trend": trend
    }
