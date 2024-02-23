from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import pandas as pd
import re
import configparser


config = configparser.ConfigParser()
config.read('config.ini')


# Starting URL
starting_url = config.get('URL', 'starting_url')
base_url = config.get('URL', 'base_url')
root_name = config.get('URL', 'root_name')

# Maximum number of URLs to collect
max_urls = config.getint('URL', 'max_urls')


# Counter variable to keep track of collected URLs
collected_urls = 0

# Function to collect URLs from a webpage
def collect_urls(url):
    bsobj = bs(urlopen(url).read(), 'html.parser')
    content_links = bsobj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    base_url = 'https://en.wikipedia.org'
    url_dict = {}
    for link in content_links:
        if 'href' in link.attrs:
            href = link.attrs['href']
            if href.startswith('/wiki/'):
                full_url = base_url + href
                url_dict[full_url] = link.get_text()
    return url_dict

url_dict = collect_urls(starting_url)

# Collect URLs from linked pages
for url in list(url_dict.keys()):
    if collected_urls >= max_urls:
        break
    
    linked_urls = collect_urls(url)
    for linked_url, title in linked_urls.items():
        if linked_url not in url_dict:
            url_dict[linked_url] = title
            collected_urls += 1
            if collected_urls >= max_urls:
                break

# Print the total number of collected URLs
print("Total number of collected URLs:", len(url_dict))

# Save the collected URLs to a CSV file
url_df = pd.DataFrame(list(url_dict.items()), columns=['URL', 'Title'])

# Save the dataframe to a CSV file
output_file = config.get('DATABASE', 'output_file')
url_df.to_csv(output_file, index=False)
