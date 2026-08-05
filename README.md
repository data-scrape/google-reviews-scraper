# 📝 Google Reviews Scraper

> Scrape Google Maps reviews - ratings, text, author, dates

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/data-scrape/google-reviews-scraper?style=flat-square)](https://github.com/data-scrape/google-reviews-scraper)
[![Forks](https://img.shields.io/github/forks/data-scrape/google-reviews-scraper?style=flat-square)](https://github.com/data-scrape/google-reviews-scraper/forks)

<a href="https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7"><img src="https://img.shields.io/badge/Sponsored%20by-CoreClaw-7B2D8B?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0xMiAyTDIgN2wxMCA1IDEwLTV6TTIgMTdsMTAgNSAxMC01ek0yIDEybDEwIDUgMTAtNXoiLz48L3N2Zz4=" alt="Sponsored by CoreClaw" width="200"></a>

## 📖 Overview

**Google Reviews Scraper** is a free, open-source Python scraper for **Google Reviews**. Extract structured data from google reviews with full pagination support, proxy rotation, and multiple export formats.

google reviews scraper, scrape google reviews, google maps reviews scraper

## ✨ Features

- ✅ Full review text extraction
- ✅ Reviewer name & photo
- ✅ Star rating & date
- ✅ Review responses from business
- ✅ Review count & average rating
- ✅ Pagination support

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/data-scrape/google-reviews-scraper.git
cd google-reviews-scraper
pip install -r requirements.txt
```

### Basic Usage

```bash
python scraper.py "Google reviews for Starbucks 5th Ave NYC"
```

### Advanced Usage

```bash
python scraper.py "Google reviews for Starbucks 5th Ave NYC" \
  --output results \
  --format json \
  --max-results 100 \
  --proxy http://user:pass@host:port
```

## 📊 Data Fields

Extracted data includes the following fields:

`review_id` | `business_name` | `reviewer_name` | `reviewer_photo` | `rating` | `date` | `text` | `owner_response` | `language` | `likes`

## 💡 Use Cases

- Reputation management
- Customer feedback analysis
- Competitor review comparison
- Local SEO improvement
- Sentiment analysis datasets

## 🔧 Configuration

| Option | Default | Description |
|--------|---------|-------------|
| `--output` | `output` | Output file prefix |
| `--format` | `json` | Output format: `json`, `csv`, or `both` |
| `--max-results` | `50` | Maximum results to scrape |
| `--proxy` | None | Proxy URL for IP rotation |
| `--quiet` | False | Suppress info output |

## 📝 Example Output

```json
{
  "url": "https://example.com/result/123",
  "title": "Example Result",
  "data": {
    "rating": 4.5,
    "reviews": 1280,
    "category": "Example Category"
  },
  "scraped_at": "2026-08-05T14:30:00"
}
```

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Users are responsible for complying with the target website's Terms of Service, robots.txt, and applicable laws. The authors of this project are not responsible for any misuse of this tool.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💎 Sponsored by CoreClaw

This project is sponsored by [**CoreClaw**](https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7) — the all-in-one web scraping and data extraction platform.

<a href="https://www.coreclaw.com/?utm_source=github&utm_medium=cpc&utm_campaign=L7&utm_term=&utm_id=L7">🌐 Visit CoreClaw.com</a>

---

⭐ If this project helped you, please give it a star!

<!-- CROSS_LINKS_START -->
<!-- Cross-links will be inserted here -->
<!-- CROSS_LINKS_END -->
