'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below! 
tweettext = []
tweetstring = ""
for tweet in tweetData:
    tweetstring += tweet['text']

for tweet in tweetData:
    tweettext.append(tweet['text'])
first = tweettext[10]
print(type(first))

print(tweetstring)
blob_polarity = []
for blob in tweettext:
    b = TextBlob(blob)
    blob_polarity.append(b.polarity)
avg = sum(blob_polarity)/len(blob_polarity)

blob_subjectivity = []
for blob in tweettext:
    blob_subjectivity.append(blob_subjectivity)
worddict = {}

tweetBlob = TextBlob(tweetstring)
word_dict = {}
for word in tweetBlob.words:
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]
print(word_dict)
# Textblob sample:
tb = TextBlob("You are a brilliant computer scientist.")
print(tb.sentiment)


plt.hist(blob_polarity, bins=[-1, -0.5, 0.0, 0.5, 1])
plt.xlabel('Values')
plt.ylabel('Number of Items')
plt.title('Histogram of Numbers')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()