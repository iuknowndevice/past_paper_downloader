import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote
import os
import time

# Add or remove pages here — ("folder_name", "pmt_url")
PAGES = [
    ("Edexcel_Maths_AS", "https://www.physicsandmathstutor.com/maths-revision/a-level-edexcel/papers-as/"),
    ("Edexcel_Maths_A2", "https://www.physicsandmathstutor.com/maths-revision/a-level-edexcel/papers/"),
]

OUTPUT_DIR = "Past_Papers"
DELAY = 0.5  # seconds between downloads

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def get_pdf_links(page_url):
    response = requests.get(page_url, headers=HEADERS, timeout=15)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    for tag in soup.find_all("a", href=True):
        href = tag["href"]
        # only grab PDFs hosted on PMT, ignores external sites like madasmaths
        if href.lower().endswith(".pdf") and "pmt.physicsandmathstutor.com" in href:
            links.append(urljoin(page_url, href))

    return links


def download_pdf(url, dest_folder):
    filename = unquote(url.split("/")[-1])  # converts %20 to spaces etc.
    filepath = os.path.join(dest_folder, filename)

    if os.path.exists(filepath):
        print(f"  [skip]  {filename}")
        return

    try:
        response = requests.get(url, headers=HEADERS, timeout=30, stream=True)
        response.raise_for_status()
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"  [done]  {filename}")
    except Exception as error:
        print(f"  [error] {filename} — {error}")


def main():
    print("PMT Past Paper Downloader")
    print(f"Saving to: {os.path.abspath(OUTPUT_DIR)}\n")

    for folder_name, page_url in PAGES:
        dest_folder = os.path.join(OUTPUT_DIR, folder_name)
        os.makedirs(dest_folder, exist_ok=True)

        print(f"{'─' * 50}")
        print(f"Subject : {folder_name}")
        print(f"URL     : {page_url}")

        try:
            links = get_pdf_links(page_url)
        except Exception as error:
            print(f"  [error] Could not load page — {error}")
            continue

        print(f"Found {len(links)} PDFs\n")

        for url in links:
            download_pdf(url, dest_folder)
            time.sleep(DELAY)

    print(f"\n{'─' * 50}")
    print("All done!")


if __name__ == "__main__":
    main()