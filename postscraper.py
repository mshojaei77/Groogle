import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

class AdvancedWebScraper:
    def __init__(self):
        self.results = {}

    def extract_data(self, url):
        response = requests.get(url, allow_redirects=True, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            paragraphs = [paragraph.text.strip() for paragraph in soup.find_all("p")]
            return ''.join(paragraphs)

if __name__ == "__main__":
    scraper = AdvancedWebScraper()
    urls = ['http://example.com', 'http://example.org']
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(scraper.extract_data, url): url for url in urls}
        for future in as_completed(futures):
            url = futures[future] # Get the URL associated with the future
            data = future.result() # Get the result of the future
            scraper.results[url] = data # Store the result in the results dictionary

    # Print the results
    for url, data in scraper.results.items():
        print(f" {url}: {data}")
