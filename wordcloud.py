import numpy as np 
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
import unicodedata as ud
#%matplotlib
from os import path
from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS

mpl.rcParams['font.size']=12                #10 
mpl.rcParams['savefig.dpi']=100             #72 
mpl.rcParams['figure.subplot.bottom']=.1 


stopwords = set(STOPWORDS)
d = path.dirname #Eg: c://,d://

data = open(path.join(d, 'filename.txt'), encoding = 'utf-8', errors='ignore').read()

wordcloud = WordCloud(
                          background_color='white',
                          stopwords=stopwords,
                          max_words=200,
                          max_font_size=40, 
                          random_state=42
                         ).generate(data)

print(wordcloud)
fig = plt.figure(1)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
fig.savefig("word.png", dpi=900)

