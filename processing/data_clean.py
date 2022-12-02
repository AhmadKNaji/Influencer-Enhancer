import re

from nltk.stem.snowball import SnowballStemmer

from twitter import get_stopwords

import contractions


# Create a function to clean the reviews. Remove profanity, unnecessary characters, spaces, and stopwords.

def clean_tweet(tweet):
    
    """
    This function unifies the tweets and stems the words.
    
    params:
    
    review (string) : The string text we want to unify.
    
    return:
    
    r (string) : The unified version of the text input.
    
    """

    # remove urls from tweets

    r = re.sub(r'https?://\S+', "", tweet)

    # This is the compiled regex to remove emojis and other non interpretable characters

    emoj = re.compile("["
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
                    "]+", re.UNICODE)

    r = re.sub(emoj, '', r)

    # Remove tags from tweets

    r = re.sub("@[A-Za-z0-9_]+","", r)

    # Remove hashtag from tweets

    r = re.sub("#[A-Za-z0-9_]+","", r)

    # Remove trailing whitespace

    r = r.strip()

    # Expand contractions (He's -> He is)

    r = contractions.fix(r)
    
    # Make the text all lower case
    
    r = r.lower()

    # Remove characters that are not a number or a letter

    r = re.sub('\W+', ' ', r)
    
    # Split the text into a list containing all the words
    
    r = r.split()
    
    # Create a new list of the words without the stop words
    
    r = [w for w in r if not w in get_stopwords()]
    
    # Create stemmer object
    
    stemmer = SnowballStemmer("english")
    
    # Stem words
    
    sw = [stemmer.stem(w) for w in r]
    
    # Joing stemmed and tokenized words
    
    res = " ".join(sw)
    
    return res
