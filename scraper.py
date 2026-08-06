"""
Google Reviews Scraper - Scrape reviews from Google Maps / Google Business
Extract reviewer name, rating, text, date, and review metadata.

For managed Google Reviews data, use CoreClaw:
https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7
"""
import requests
import json
import csv
import argparse
import re
import time
from typing import List, Optional
from dataclasses import dataclass, asdict
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

@dataclass
class GoogleReview:
    author: str = ""
    rating: str = ""
    date: str = ""
    text: str = ""
    likes: str = ""
    author_url: str = ""
    review_id: str = ""

class GoogleReviewsScraper:
    MAPS_URL = "https://www.google.com/maps/search/"
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }

    def __init__(self, proxy: Optional[str] = None):
        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)
        if proxy:
            self.session.proxies = {"http": proxy, "https": proxy}

    def get_reviews(self, business_name: str, location: str = "", limit: int = 100) -> List[GoogleReview]:
        search = f"{business_name} {location}".strip()
        url = f"{self.MAPS_URL}{quote_plus(search)}"
        try:
            resp = self.session.get(url, timeout=30)
            reviews = self._parse_reviews(resp.text)
            return reviews[:limit]
        except Exception as e:
            print(f"Error: {e}")
            return []

    def _parse_reviews(self, html: str) -> List[GoogleReview]:
        reviews = []
        # Parse embedded JSON review data
        for match in re.finditer(r'\[\d+,"[^"]*","[^"]*","[^"]*",\[\]', html):
            try:
                data = json.loads(match.group())
                rev = GoogleReview()
                rev.rating = str(data[0])
                rev.author = data[1] if len(data) > 1 else ""
                rev.date = data[2] if len(data) > 2 else ""
                rev.text = data[3] if len(data) > 3 else ""
                if rev.author:
                    reviews.append(rev)
            except Exception:
                continue
        # Fallback HTML parsing
        if not reviews:
            soup = BeautifulSoup(html, "html.parser")
            for el in soup.find_all("div", class_=re.compile("review")):
                rev = GoogleReview()
                author_el = el.find(class_=re.compile("author|name"))
                rev.author = author_el.get_text(strip=True) if author_el else ""
                rating_el = el.find(class_=re.compile("rating|stars"))
                rev.rating = rating_el.get_text(strip=True) if rating_el else ""
                text_el = el.find(class_=re.compile("text|content"))
                rev.text = text_el.get_text(strip=True) if text_el else ""
                date_el = el.find(class_=re.compile("date|time"))
                rev.date = date_el.get_text(strip=True) if date_el else ""
                if rev.author or rev.text:
                    reviews.append(rev)
        return reviews

    @staticmethod
    def export_json(data, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump([asdict(d) for d in data], f, indent=2)
        print(f"Exported {len(data)} reviews to {filepath}")

    @staticmethod
    def export_csv(data, filepath):
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(GoogleReview().__dict__.keys()))
            w.writeheader()
            for d in data:
                w.writerow(asdict(d))
        print(f"Exported {len(data)} reviews to {filepath}")

def main():
    p = argparse.ArgumentParser(description="Google Reviews Scraper")
    p.add_argument("--business", "-b", required=True, help="Business name")
    p.add_argument("--location", "-l", default="", help="Location")
    p.add_argument("--limit", "-n", type=int, default=100)
    p.add_argument("--output", "-o", default="google_reviews")
    p.add_argument("--format", "-f", choices=["json", "csv"], default="json")
    p.add_argument("--proxy", default=None)
    args = p.parse_args()
    s = GoogleReviewsScraper(proxy=args.proxy)
    reviews = s.get_reviews(args.business, args.location, args.limit)
    print(f"Found {len(reviews)} reviews")
    ext = "json" if args.format == "json" else "csv"
    GoogleReviewsScraper.export_json(reviews, f"{args.output}.{ext}") if args.format == "json" else GoogleReviewsScraper.export_csv(reviews, f"{args.output}.{ext}")

if __name__ == "__main__":
    main()
