from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')

sents = ["I love you. I hate him. You are nice. He is dumb",
         "Like it used to be funny not anymore man. Bro I legit may never see you again. This is madness!. I am so so so tired"]

for sent in sents:
    print('Analyzing - ', sent, '...')
    res = nlp.annotate(sent,
                       properties={
                           'annotators': 'sentiment',
                           'outputFormat': 'json'
                       })
    for s in res["sentences"]:
        print "%d: '%s': %s %s" % (
            s["index"],
            " ".join([t["word"] for t in s["tokens"]]),
            s["sentimentValue"], s["sentiment"])
