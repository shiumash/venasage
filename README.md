# venasage 🫀

## overview
venasage is an ai chatbot that provides clear, reliable answers to cardiovascular health questions. it combines trusted medical sources with smart retrieval technology, helping users make informed decisions with accurate, up-to-date information.

> fun fact: the name comes from *vena* the latin word for 'vein' + *sage*, wise one'. nifty huh?

## 🚀 key features
- **intelligent medical information retrieval**: sophisticated retrieval-augmented generation (rag) model for precise, context-aware responses
- **semantic search optimization**: leveraging advanced embedding technologies for accurate, relevant information extraction
- **reduced hallucination**: rigorous approach to minimizing ai-generated misinformation

## 💡 inspiration & approach
i was inspired callum macleod's medium article ["implementing rag in langchain with chroma: a step-by-step guide"](https://medium.com/@callumjmac/implementing-rag-in-langchain-with-chroma-a-step-by-step-guide-16fc21815339). my take will be tailored specifically to cardiovascular health information retrieval. drawing from the foundational rag concepts, our approach diverges by:
- specializing in cardiovascular domain-specific knowledge
- implementing custom preprocessing for medical text
- developing with updated langchain v0.3 modules.
- incorporating more open-source tools.

## 🛠 tech stack
### embedding & semantic search
- **embedding model**: [hugging face `all-minilm-l6-v2`](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- **vector database**: [chromadb](https://python.langchain.com/docs/integrations/vectorstores/chroma/) for efficient semantic retrieval
- **language model**: fine-tuned [llama 3.2](https://www.llama.com/)

### data processing capabilities
- **html/xml parsing**: developed robust web scraping and parsing techniques
- **text preprocessing**: advanced preprocessing and crawling scripts for medical text corpus

## 🧠 technical architecture
venasage represents a sophisticated approach to medical information retrieval, integrating:
- semantic embedding techniques
- vector database optimization
- advanced machine learning models

## 📦 installation
```bash
# clone the repository
git clone https://github.com/yourusername/venasage.git
# highly recommend using a virtual environment 😉
# install dependencies
pip install -r requirements.txt
```
## 🚦 quick start
```python
coming soon 🤭
```
---
**disclaimer**: venasage is an ai assistant and should not replace professional medical advice. always consult healthcare professionals for personalized medical guidance. please don't sue me 🙏
