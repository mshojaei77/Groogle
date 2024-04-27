from groq import Groq
import os
from dotenv import load_dotenv
from googlesearch import search
from postscraper import AdvancedWebScraper
from concurrent.futures import ThreadPoolExecutor, as_completed

load_dotenv()
API_KEY = os.getenv('groq_api_key')

prompt = input("ask me anything: ")
client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

query_generator = client.chat.completions.create(messages=[{"role": "user","content": f"generate only 1 google search query for this prompt ({prompt}) to get help, put it inside quotes",}],model="llama3-8b-8192",)

query = ' '.join(query_generator.choices[0].message.content.split('"')[1::2])

print(query)

scraper = AdvancedWebScraper()

urls = list(search(query,num_results=5))
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(scraper.extract_data, url): url for url in urls}
    for future in as_completed(futures):
        url = futures[future] # Get the URL associated with the future
        data = future.result() # Get the result of the future
        scraper.results[url] = data # Store the result in the results dictionary

for url, data in scraper.results.items():
        print(f" \n {url}: \n ```{data}``` ")

chat_completion = client.chat.completions.create(messages=[{"role": "user","content": f"answer this prompt '{prompt}' using following web results: \n {scraper.results}" }],model="llama3-70b-8192",)
answer = chat_completion.choices[0].message.content
print(answer)
