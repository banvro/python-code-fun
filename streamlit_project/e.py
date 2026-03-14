import re
import requests
from bs4 import BeautifulSoup
from io import BytesIO
import PyPDF2
from urllib.parse import urljoin, urlparse


def get_all_pdf_links(start_url, max_pages=10):
    visited = set()
    to_visit = [start_url]
    pdf_links = []

    domain = urlparse(start_url).netloc

    while to_visit and len(visited) < max_pages:
        url = to_visit.pop(0)

        if url in visited:
            continue

        visited.add(url)

        try:
            print(f"Scanning page: {url}")
            response = requests.get(url, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            for link in soup.find_all("a", href=True):
                href = link["href"]
                full_url = urljoin(url, href)

                # If PDF
                if full_url.lower().endswith(".pdf"):
                    pdf_links.append(full_url)

                # If same domain, add to crawl list
                elif urlparse(full_url).netloc == domain:
                    if full_url not in visited:
                        to_visit.append(full_url)

        except Exception as e:
            print(f"Error scanning {url}: {e}")

    return list(set(pdf_links))


def count_name_in_online_pdfs(pdf_links, name):
    total_count = 0
    file_counts = {}
    pattern = re.compile(rf"\b{re.escape(name)}\b", re.IGNORECASE)

    for url in pdf_links:
        try:
            print(f"Checking PDF: {url}")
            response = requests.get(url, timeout=15)
            pdf_file = BytesIO(response.content)

            reader = PyPDF2.PdfReader(pdf_file)

            count_in_file = 0

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    matches = pattern.findall(text)
                    count_in_file += len(matches)

            file_counts[url] = count_in_file
            total_count += count_in_file

        except Exception as e:
            print(f"Error reading {url}: {e}")

    return total_count, file_counts


# ---------------- MAIN ----------------

if __name__ == "__main__":
    WEBSITE_URL = input("Enter starting website URL: ").strip()
    search_name = input("Enter name to search: ").strip()

    pdf_links = get_all_pdf_links(WEBSITE_URL, max_pages=20)

    print(f"\nFound {len(pdf_links)} PDF files.\n")

    total, breakdown = count_name_in_online_pdfs(pdf_links, search_name)

    print("\n----- RESULTS -----")
    for url, count in breakdown.items():
        print(f"{url} → {count} times")

    print("\n====================")
    print(f"TOTAL occurrences of '{search_name}': {total}")