import pandas as pd
import re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from stopwords import clean_stemmed

from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
###run it only for first time###
# nltk.download('punkt')
# nltk.download('wordnet')
################################
wordnet_lemmatizer = WordNetLemmatizer()
porter_stemmer = PorterStemmer()

def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def clean(d):
  d = str(d)
  chars = re.findall("""[\w\s"'#]+\w+""",d)
  d = ''.join([c for c in chars if c])
  return d

def stem_and_lemma(msg):
  msg = msg.replace(':D','')
  nltk_tokens = tknzr.tokenize(msg)
  message_tokenized = []
  for w in nltk_tokens:
    if w not in clean_stemmed:
      w = w.strip(' ').strip('\'').strip('\`').strip('\"')
      # w = porter_stemmer.stem(w)
      w = wordnet_lemmatizer.lemmatize(w)
      message_tokenized.append(w)
  msg = ' '.join(message_tokenized)
  msg = msg.strip('"').strip("'").strip('!')
  return msg

# df = pd.read_csv("chatlogs.csv")
df = pd.read_excel("chatlogs_excel.xlsx", sheet_name='Chat Logs')
# df = df.head(100)
# df['message'] = df['message'].apply(clean)
df['message'] = df['message'].apply(lambda x: remove_emoji(str(x)))
df['message'] = df['message'].apply(stem_and_lemma)
df.to_csv('chatlogs_cleaned.csv')