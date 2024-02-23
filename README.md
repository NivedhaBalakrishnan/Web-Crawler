# Webcrawler

## Overview
Webcrawler is a Python script that recursively crawls web pages to extract URLs. It starts from a source page, collects URLs from that page, then visits each URL to collect more URLs. This process continues until a specified limit is reached, in this case, ~5000 URLs.

## Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/NivedhaBalakrishnan/Web-Crawler.git
   ```

2. **Update the configuration in the `config.ini` file:**

    - Set the `starting_url` to the URL of the initial page to start crawling from.
        - **Starting URL Page:** [https://en.wikipedia.org/wiki/Ancient_Egypt](https://en.wikipedia.org/wiki/Ancient_Egypt)
    - Adjust the `max_urls` parameter to specify the maximum number of URLs to collect.
        - **Maximum URLs:** 5000

3. **Run the webcrawler script to collect URLs:**

    ```sh
    python3 web_crawler.py
    ```

4. **Run the embedding script to extract embeddings from the collected titles and save them to the CSV:**

    ```sh
    python3 embed.py
    ```

5. **Use the search script to perform a cosine similarity search based on a query:**

    ```sh
    python3 search.py 'Ancient Greece'
    ```
    Replace `'Ancient Greece'` with your desired query.

## Output
### Number of URLs
- **Total Links in Starting Page:** 1568
- **Total URLs Collected:** 6230

### Output for Query 'Ancient Greece'
Title: Ancient Greek, URL: https://en.wikipedia.org/wiki/Ancient_Greek_language

Title: ancient Greeks, URL: https://en.wikipedia.org/wiki/Ancient_Greeks

Title: Greece, URL: https://en.wikipedia.org/wiki/Economy_of_ancient_Greece#Trade

Title: Greece, URL: https://en.wikipedia.org/wiki/Ancient_Greece

Title: Greece, URL: https://en.wikipedia.org/wiki/Greek_city-states


## Configuration

You can customize the behavior of the web crawler by modifying the parameters in the `config.ini` file. Here are some key parameters you may want to adjust:

- `starting_url`: The URL of the initial page to start crawling from.
- `max_urls`: The maximum number of URLs to collect.


