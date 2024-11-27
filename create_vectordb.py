from query_helper import clean_doc_text
from langchain_community.document_loaders import DirectoryLoader, BSHTMLLoader
from langchain_text_splitters import HTMLSectionSplitter, RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os, getpass, shutil


CHROMA_PATH = "chroma"

def load_docs():
  loader = DirectoryLoader(
    "data", glob="*.html", 
    loader_cls=BSHTMLLoader, 
    use_multithreading=True,
    silent_errors=True)
  docs = loader.load()

  for doc in docs:
    doc.page_content = clean_doc_text(doc.page_content)
  
  return docs

def split_text(documents: list[Document]):
  headers_to_split_on = [
    ("h2", "Header 2"),  
    ("h3", "Header 3"),
    ("article", "Article"),
    ("ul", "Unordered List"),
    ("p", "Paragraph"),
  ]

  html_splitter = HTMLSectionSplitter(headers_to_split_on)
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    length_function=len,
    add_start_index=True
  )

  html_header_splits = html_splitter.split_documents(documents)
  chunks = text_splitter.split_documents(html_header_splits)

  return chunks

def save_to_db(chunks: list[Document]):

  embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

  if os.path.exists(CHROMA_PATH):
    shutil.rmtree(CHROMA_PATH)

  db = Chroma.from_documents(chunks, embeddings, persist_directory=CHROMA_PATH)
  print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

def generate_data_store():
  docs = load_docs()
  chunks = split_text(docs)
  save_to_db(chunks)

def main():
  generate_data_store()

if __name__ == "__main__":
  main()