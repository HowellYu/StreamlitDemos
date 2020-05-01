import streamlit as st
import os


# NLP Pkgs
from textblob import TextBlob
import spacy
from gensim.summarization import summarize
import nltk

# Sumy Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import json

LANGUAGE = "english"
SENTENCES_COUNT = 10

# Sumy Summarization
def sumy_summarizer(docx):
    parser = PlaintextParser.from_string(docx, Tokenizer(LANGUAGE))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, 3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

# Function For Analysing Tokens and Lemma
@st.cache
def text_analyzer(my_text):
    nlp = spacy.load('en')
    docx = nlp(my_text)
    # tokens = [ token.text for token in docx]
    allData = [('"Token":{},\n"Lemma":{}'.format(token.text,token.lemma_))for token in docx ]
    return allData

# Function For Extracting Entities
@st.cache
def entity_analyzer(my_text):
    nlp = spacy.load('en')
    docx = nlp(my_text)
    tokens = [token.text for token in docx]
    entities = [(entity.text,entity.label_)for entity in docx.ents]
    allData = ['"Token":{},\n"Entities":{}'.format(tokens,entities)]
    return allData

# currently streamlit does not have a download method, there is a workaround to generate a download link
def get_download_link(text, file_name):
    import base64
    b64 = base64.b64encode(text.encode('ascii')).decode()  # some strings <-> bytes conversions necessary here
    print('result:', b64)
    return f'<a href="data:file/txt;base64,{b64}" download="{file_name}.txt">Download Result</a>'


def main():
    """ NLP Based App with Streamlit """

    # show balloons
    # st.balloons()

    # Title
    st.title("Streamlit App Demo")
    st.subheader("Common NLP Tasks")

    # Tokenization
    if st.checkbox("Show Tokens and Lemma"):
        st.subheader("Tokenize Your Text")

        message_token_text = st.text_area("Enter Text")
        message_token_file = st.file_uploader("Upload a file", type=("txt"))
        if st.button("Tokenzie"):

            message_token = None

            if message_token_text:
                message_token = message_token_text
            elif message_token_file:
                message_token = message_token_file.read()
            else:
                st.warning('Please make sure to enter text or upload a file and make sure the input is not empty!')

            if message_token:
                nlp_result = text_analyzer(message_token)
                st.json(nlp_result)
                file_name = 'token_lemma'
                st.markdown(get_download_link(json.dumps(nlp_result), file_name), unsafe_allow_html=True)

    # Entity Extraction
    if st.checkbox("Show Named Entities"):
        st.subheader("Analyze Your Text")

        message_NER_text = st.text_area("Enter Text")
        message_NER_file = st.file_uploader("Upload a file", type=("txt"))
        if st.button("Extract"):

            message_NER = None

            if message_NER_text:
                message_NER = message_NER_text
            elif message_NER_file:
                message_NER = message_NER_file.read()
            else:
                st.warning('Please make sure to enter text or upload a file and make sure the input is not empty!')

            if message_NER:
                entity_result = entity_analyzer(message_NER)
                st.json(entity_result)
                file_name = 'ner'
                st.markdown(get_download_link(json.dumps(entity_result), file_name), unsafe_allow_html=True)

    # Sentiment Analysis
    if st.checkbox("Show Sentiment Analysis"):
        st.subheader("Analyse Your Text")

        message_sent_text = st.text_area("Enter Text")
        message_sent_file = st.file_uploader("Upload a file", type=("txt"))

        if st.button("Analyze"):

            message_sent = None

            if message_sent_text:
                message_sent = message_sent_text
            elif message_sent_file:
                message_sent = message_sent_file.read()
            else:
                st.warning('Please make sure to enter text or upload a file and make sure the input is not empty!')
            if message_sent:
                blob = TextBlob(message_sent)
                result_sentiment = blob.sentiment
                st.success(result_sentiment)

    # Summarization
    if st.checkbox("Show Text Summarization"):
        st.subheader("Summarize Your Text")

        message_from_text = st.text_area("Enter Text")
        message_from_file = st.file_uploader("Upload a file", type=("txt"))

        summary_options = st.selectbox("Choose Summarizer",['sumy','gensim'])
        if st.button("Summarize"):

            message_summ = None

            if message_from_text:
                message_summ = message_from_text
            elif message_from_file:
                message_summ = message_from_file.read()
            else:
                st.warning('Please make sure to enter text or upload a file and make sure the input is not empty!')

            if message_summ:
                if summary_options == 'sumy':
                    st.text("Using Sumy Summarizer ..")
                    print("Using Sumy Summarizer ..")
                    summary_result = sumy_summarizer(message_summ)
                if summary_options == 'gensim':
                    st.text("Using Gensim Summarizer ..")
                    summary_result = summarize(message_summ)
                    print("Using Gensim Summarizer ..")

                st.success(summary_result)
                file_name = 'machine_translation' + '-' + summary_options
                st.markdown(get_download_link(summary_result, file_name), unsafe_allow_html=True)


    st.sidebar.subheader("About App")
    st.sidebar.text("NLP Tasks Demo with Streamlit")

    st.sidebar.subheader("By")
    st.sidebar.text("Modified by Howell Yu")
    st.sidebar.text("Created by Jesse E.Agbe(JCharis)")



if __name__ == '__main__':
    main()
