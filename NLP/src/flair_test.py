import flair
flair_sentiment = flair.models.TextClassifier.load('en-sentiment')
sents = ["I love you. I hate him. You are nice. He is dumb",
         "Like it used to be funny not anymore man. Bro I legit may never see you again. Insane. I'm done",
         "Absolute lack of respect for our talent and experience in this team. I have no idea why I am still here."]
for sent in sents:
    print(sent)
    s = flair.data.Sentence(sent)
    flair_sentiment.predict(s)
    total_sentiment = s.labels
    print(total_sentiment)
