import requests
from bs4 import BeautifulSoup
import html
import re
from datetime import datetime, timedelta
import multiprocessing
import time

def fetch_and_parse_page(page_start):
    """Fetch and parse a single Google Scholar page."""
    # URL for Google Scholar search with pagination
    url = f"https://scholar.google.com/scholar?start={page_start}&q=agent+based+modeling+finance&hl=en&as_sdt=0,5" # sort based on relevance 
    # url = f"https://scholar.google.com/scholar?start={page_start}&q=agent+based+modeling+finance&hl=en&scisbd=1&as_sdt=0,5" # sort based on the recent publication

    # Headers to mimic a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:141.0) Gecko/20100101 Firefox/141.0",
        "Cookie": "NID=525=hoAfHj3lRKRGvjHBywZ6yYgaHn19iF4t7RiydYN0sFoYVPwa4y4sMBogVtCVzUE0qxGR71DYbXs_WncKuhhY2ZUxYVIrbJazmThEbzDE5Q0w-Yo-YzeOsBzR2IKFFW0CKfHaTKhoHHmYWsjfCuERo4qFQ266EIyjBKUYr9gwsIxef3xqIaGsDy8dMzeKs5NL_w; GSP=LM=1754497981:S=Zmonqy0wzbBe8r8R"
    }

    try:
        # Fetch HTML content
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching page {page_start}: {e}")
        return []

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all result divs with class 'gs_r gs_or gs_scl'
    results = soup.select("div.gs_r.gs_or.gs_scl")

    # Current date for calculating actual dates
    current_date = datetime(2025, 8, 6)

    # List to store results for this page
    page_results = []

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

            # Format the result as requested
            formatted_result = f'"{clean_title}"-["{release_date_str}"]'
            page_results.append(formatted_result)

    return page_results

def write_to_file(results, filename="scholar_results.txt"):
    """Write results to a file in a thread-safe manner."""
    with lock:
        with open(filename, "a", encoding="utf-8") as f:
            for result in results:
                f.write(result + "\n")

def main():
    # Create a lock for thread-safe file writing
    global lock
    lock = multiprocessing.Lock()

    # Clear the output file before starting
    with open("scholar_results.txt", "w", encoding="utf-8") as f:
        f.write("")

    # Create a list of page start indices (0, 10, 20, ..., 990)
    page_starts = list(range(0, 1000, 10))

    # Use a process pool to fetch and process pages concurrently
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map the fetch_and_parse_page function to all page starts
        all_results = pool.map(fetch_and_parse_page, page_starts)

    # Flatten the results and write to file
    for page_results in all_results:
        if page_results:  # Only write non-empty results
            write_to_file(page_results)

    # Print results from the file for verification
    with open("scholar_results.txt", "r", encoding="utf-8") as f:
        print(f.read())

if __name__ == "__main__":
    main()