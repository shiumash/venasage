from query_helper import fetch_data, parse_xml, fetch_html, fetch_save_html, fetch_and_save_all_links, clean_doc_text
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import BSHTMLLoader


URL = "https://wsearch.nlm.nih.gov/ws/query"
params = {
    "db": "healthTopics",
    "term": "cardiovascular+disease"
  }

def main():
  
  file_path = fetch_data(URL, params)
  urls = parse_xml(file_path)

  html_data = fetch_save_html(urls)

  for i, html_content in enumerate(html_data):
    fetch_and_save_all_links(html_content, urls[i], f"document_{i}")
  
if __name__ == "__main__":
    main()
