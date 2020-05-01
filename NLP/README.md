### Streamlit for Natural Language Processing Tasks

> Author: Qianhao Howell Yu        
> Source: https://blog.jcharistech.com/2019/10/22/building-a-natural-language-processing-app-with-streamlitspacy-and-python/    


#### NLP Tasks
1. Tokenizer
  - [Spacy](https://spacy.io/api/doc)
2. Entity Extraction
  - [Spacy](https://spacy.io/api/doc)
3. Sentiment Analysis
  - [TextBlob](https://textblob.readthedocs.io/en/dev/)
4. Text Summarization
  - [Sumy](https://pypi.org/project/sumy/)
  - [Gensim](https://pypi.org/project/gensim/)

#### Setup
Execute the following command to install all the necessary dependencies, preferably in a Python virtual environment.
```shell
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt')"
python -m spacy download en
```

Execute the following command to launch the app. By default, the app will launch at http://localhost:8501/.
```shell
streamlit run app.py
```

### StreamLit Capabilities
- Text area, checkbox, multiple selection, slider, date.
- File upload, download, result display, markdown.
- Dataframe (pandas).
- Error handling.
- Header, sub-header, sidebar.
