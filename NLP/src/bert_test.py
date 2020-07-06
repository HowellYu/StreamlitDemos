import numpy, pandas, torch, transformers
from transformers import BertTokenizer, BertModel
from torch import nn

sents = ["I love you. I hate him. You are nice. He is dumb",
         "Like it used to be funny not anymore man. Bro I legit may never see you again. Insane. I'm done",
         "Absolute lack of respect for our talent and experience in this team. I have no idea why I am still here."]

MAX_LEN = 160
class_names = ['negative', 'neutral', 'positive']
PRE_TRAINED_MODEL_NAME = 'bert-base-cased'
tokenizer = BertTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)
model_path = "../model/bert_model_state.bin"

# class def needed for loading the model
class SentimentClassifier(nn.Module):

  def __init__(self, n_classes):
    super(SentimentClassifier, self).__init__()
    self.bert = BertModel.from_pretrained(PRE_TRAINED_MODEL_NAME)
    self.drop = nn.Dropout(p=0.3)
    self.out = nn.Linear(self.bert.config.hidden_size, n_classes)

  def forward(self, input_ids, attention_mask):
    _, pooled_output = self.bert(
      input_ids=input_ids,
      attention_mask=attention_mask
    )
    output = self.drop(pooled_output)
    return self.out(output)


if torch.cuda.is_available():
    print('Using cuda')
    device = torch.device("cuda:0")
else:
    print('Using CPU')
    device = torch.device("cpu")

print("Loading BERT model...")
model = SentimentClassifier(len(class_names))
model.load_state_dict(torch.load(model_path, map_location=device))
print("Model loaded.")

for sent in sents:
    encoded_review = tokenizer.encode_plus(
      sent,
      max_length=MAX_LEN,
      add_special_tokens=True,
      return_token_type_ids=False,
      pad_to_max_length=True,
      return_attention_mask=True,
      return_tensors='pt',
    )

    input_ids = encoded_review['input_ids'].to(device)
    attention_mask = encoded_review['attention_mask'].to(device)

    output = model(input_ids, attention_mask)
    _, prediction = torch.max(output, dim=1)

    print(f'Review text: {sent}')
    print(f'Sentiment  : {class_names[prediction]}')
