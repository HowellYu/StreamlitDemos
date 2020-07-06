import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
sents = ["I love you. I hate him. You are nice. He is dumb",
         "Like it used to be funny not anymore man. Bro I legit may never see you again. Insane. I'm done",
         "Absolute lack of respect for our talent and experience in this team. I have no idea why I am still here."]
for sent in sents:
    print(sent)
    print(sid.polarity_scores(sent))
