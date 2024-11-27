import os, re, requests
import xml.etree.ElementTree as ET
import numpy as np
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def fetch_data(url, params):
    response = requests.get(url, params=params)
    content = response.content.decode("utf-8")
    file_path = "article_list.xml"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fetched data and wrote to {file_path}")
    return file_path

def parse_xml(file_path):
  try:
    xml_data = ET.parse(file_path)
    root = xml_data.getroot()
    urls = [document.attrib['url'] for document in root.findall(".//document")]
    print(f"Parsed URLs: {urls}")
    return urls
  except ET.ParseError as e:
    print(f"XML parsing error: {e}")
  except FileNotFoundError as e:
    print(f"File not found: {e}")

def ensure_data_directory():
    if not os.path.exists("data"):
        os.makedirs("data")
        print("Created 'data' directory")

def fetch_save_html(urls):
  html_data = []
  ensure_data_directory()
  for i, url in enumerate(urls):
    try:
      res = requests.get(url)
      if res.status_code == 200 and 'text/html' in res.headers['Content-Type']:
        html_content = res.text
        html_data.append(html_content)
        file_path = os.path.join("data", f"document_{i}.html")
        with open(file_path, "w", encoding="utf-8") as f:
          f.write(html_content)
        print(f"Saved HTML content to {file_path}")
      else:
        print(f"Failed to fetch {url} with status code {res.status_code}")
    except requests.exceptions.RequestException as e:
      print(f"Request failed for {url}: {e}")
  return np.array(html_data)
    
def fetch_and_save_all_links(html_content, base_url, file_prefix):
    allowed_domains = [
        "www.medlineplus.gov",
        "www.ncbi.nlm.nih.gov",
        "www.mayoclinic.org",
        "www.aao.org",
        "www.kidshealth.org",
        "www.radiologyinfo.org",
        "www.cdc.gov",
        "www.hopkinsmedicine.org"
    ]
    
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=True)
    ensure_data_directory()
    
    crawled_links = 0
    for i, link in enumerate(links):
        if crawled_links >= 200:
            break
        
        href = link['href']
        parsed_url = urlparse(href)
        domain = parsed_url.netloc
        
        if domain in allowed_domains:
            if not href.startswith('http'):
                href = base_url + href
            try:
                res = requests.get(href)
                if res.status_code == 200 and 'text/html' in res.headers['Content-Type']:
                    html_content = res.text
                    file_path = os.path.join("data", f"{file_prefix}_link_{i}.html")
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(html_content)
                    print(f"Saved HTML content of link {href} to {file_path}")
                    crawled_links += 1
                else:
                    print(f"Failed to fetch {href} with status code {res.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Request failed for {href}: {e}")

def clean_doc_text(text):
    # Remove tabs, newlines, and extra spaces
    text = re.sub(r'\t', ' ', text)  # Replace tabs with a space
    text = re.sub(r'\n', ' ', text)  # Replace newlines with a space
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text.strip()  # Remove leading and trailing spaces

def fetch_html(urls):
    html_data = []
    for url in urls:
        try:
            res = requests.get(url)
            if res.status_code == 200:
                html_data.append(res.text)
            else:
                print(f"Failed to fetch {url} with status code {res.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed for {url}: {e}")
    print(f"Fetched HTML data for URLs: {urls}")
    return np.array(html_data)