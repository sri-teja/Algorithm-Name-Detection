#sampleComment
import slate
import nltk
from nltk.tag import PerceptronTagger
from nltk.data import find
#nltk.download()
#from nltk.tag.stanford import NERTagger
#nltk.download()
#nltk.download('all')
import nltk.corpus
from nltk import pos_tag, word_tokenize
import nltk.tag.perceptron
from nltk.corpus import stopwords
from nltk import PorterStemmer
import re

with open('a.pdf') as f:
    doc = slate.PDF(f)
print doc
stopword={}
stemmed_words=[]
words_before_stemming=[]
words = stopwords.words('english')
for i in words:
    stopword[i]=1
#regex = re.compile(r'\d+\.?\d+|[a-zA-Z0-9]+')
for word in doc:
    #temp = regex.findall(word)
    temp = nltk.word_tokenize(word)
    #PICKLE = "averaged_perceptron_tagger.pickle"
    #AP_MODEL_LOC = 'file:'+str(find('taggers/averaged_perceptron_tagger/'+PICKLE))
    #tagger = PerceptronTagger(load=False)
    #tagger.load(AP_MODEL_LOC)
    #pos_tag = tagger.tag
    temp = nltk.pos_tag(temp)
    filtered_words = []
    for w in temp:
        s = w
        try:
            stopword[s]
        except:
            filtered_words.append(s)
    for a in filtered_words:
        words_before_stemming.append(a)
        s = PorterStemmer().stem_word(a)
        
        if s[1][0]=="N":
           if len(s[0])>1:
              stemmed_words.append(s)
print words_before_stemming
print stemmed_words

