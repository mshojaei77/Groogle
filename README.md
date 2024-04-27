# Groogle
Groq + Google 
# Groogle : Groq + Google

Groogle is a Python application that combines the capabilities of the Groq API and the Google search engine to provide a comprehensive solution for information retrieval and processing. The application uses the Groq API for chat completions and the Google search engine to find relevant web results. It then uses a web scraper to extract data from these results and uses the Groq API again to generate a response based on the prompt and the extracted data.

## Features

- **Groq API Integration**: Utilizes the Groq API for chat completions to generate queries and answers.
- **Google Search**: Performs Google searches to find relevant web results.
- **Web Scraping**: Extracts data from the web results using a web scraper.
- **Concurrent Processing**: Uses concurrent processing to speed up the web scraping process.
- **Environment Variables**: Loads API keys from environment variables for secure access.

## Usage

1. Install the required packages by running `pip install -r requirements.txt`.
2. Set your Groq API key in your environment variables as `GROQ_API_KEY`.
3. Run the script and input your prompt when prompted.
4. The script will generate a Google search query, perform the search, scrape the results, and use the Groq API to generate an answer based on the prompt and the extracted data.

## Note

- The script requires an active internet connection to perform Google searches and scrape web results.
- The script uses the `googlesearch` package, which may not be the most efficient or reliable for large-scale scraping.
- The script uses the `postscraper.py` for web scraping, which may not be the most efficient or reliable for all websites.
- The script uses the `concurrent.futures` module for concurrent processing, which may not be the most efficient or reliable for all use cases.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the [MIT License](LICENSE).
