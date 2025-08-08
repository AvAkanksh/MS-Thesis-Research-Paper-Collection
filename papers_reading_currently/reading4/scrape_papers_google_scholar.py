import requests
from bs4 import BeautifulSoup
import html
import re
from datetime import datetime, timedelta
for i in range(100):
    
    # URL for Google Scholar search
    url = f"https://scholar.google.com/scholar?start={i*10}&q=agent+based+modeling+finance&hl=en&scisbd=1&as_sdt=0,5"

    # Headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0",
        "Cookie": "NID=525=hoAfHj3lRKRGvjHBywZ6yYgaHn19iF4t7RiydYN0sFoYVPwa4y4sMBogVtCVzUE0qxGR71DYbXs_WncKuhhY2ZUxYVIrbJazmThEbzDE5Q0w-Yo-YzeOsBzR2IKFFW0CKfHaTKhoHHmYWsjfCuERo4qFQ266EIyjBKUYr9gwsIxef3xqIaGsDy8dMzeKs5NL_w; GSP=LM=1754497981:S=Zmonqy0wzbBe8r8R"
    }

    # Fetch HTML content
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error for bad responses

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all result divs with class 'gs_r gs_or gs_scl'
    results = soup.select("div.gs_r.gs_or.gs_scl")

    # Current date for calculating actual dates
    current_date = datetime(2025, 8, 6)

    # Process each result to extract title and date
    for result in results:
        # Extract title from h3.gs_rt a
        title_tag = result.select_one("h3.gs_rt a")
        if title_tag:
            # Get text with a space separator, decode HTML entities, and normalize whitespace
            raw_title = title_tag.get_text(separator=" ", strip=True)
            clean_title = html.unescape(raw_title).strip()
            clean_title = " ".join(clean_title.split())

            # Extract relative date from span.gs_age
            date_tag = result.select_one("span.gs_age")
            if date_tag:
                # Extract number of days from text like "4 days ago"
                date_text = date_tag.get_text(strip=True)
                match = re.match(r"(\d+)\s+days\s+ago", date_text)
                if match:
                    days_ago = int(match.group(1))
                    # Calculate actual date
                    release_date = current_date - timedelta(days=days_ago)
                    release_date_str = release_date.strftime("%Y-%m-%d")
                else:
                    release_date_str = "Unknown"
            else:
                release_date_str = "Unknown"

            # Print title and release date
            print(f"Title: {clean_title}")
            print(f"Release Date: {release_date_str}\n")