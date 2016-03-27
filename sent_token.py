#with open('b_text') as line:
#    data=line.readlines()
#print data
import nltk
import re
data = open('b_text', 'r').read()            #extracted pdf data
data = data.decode('utf-8')
#print data
import codecs
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
sent_tokenize_list = sent_tokenize(data)       #sentence tokenisation
print len(sent_tokenize_list)
sent=[]
for i in sent_tokenize_list:
    i =  i.split('\n\n')
    for j in i:
        if len(j)>3:
            sent.append(j)                    #split different lines
citation_sentences=[]
f = codecs.open('sent_output2.0', 'w', encoding='utf8')
for i in sent:
    i = i.replace('-\n', "")                 #     merge the words at the end of the sentence. for e.g. proba- 
    i = i.replace('\n',' ')		     #remove the next line and merge those two words in a sentence by space.
    #print i
    #print ""
    if i=="References":			    #remove the References part
        break
    elif re.match('.*\[.*\].*', i, re.DOTALL):   #extracting all the sentences having citations for e.g.[1], [3, 5] etc...
        f.write(i+'\n')
        #citation_sentences.append(i)                          # writing those sentences extracted from the pdf in a file(sentence wise).


with open('sent_output2.0') as f:
    sentences = f.readlines()
    #print sentence
    for sentence in sentences:
        if re.match('.*\[.*\].*', sentence, re.DOTALL):
            citation_sentences.append(sentence)

#print citation_sentences

#print citation_sentences


words_tokenised=[]
full_file_tokeniser=[]
stopword={}
#words = stopwords.words('english')
#print words
words = [u'=', u'.', u',', u'This', u'In', u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'no', u'nor', u'not', u'only', u'own', u'same', u'so', u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now', u'd', u'll', u'm', u'o', u're', u've', u'y', u'ain', u'aren', u'couldn', u'didn', u'doesn', u'hadn', u'hasn', u'haven', u'isn', u'ma', u'mightn', u'mustn', u'needn', u'shan', u'shouldn', u'wasn', u'weren', u'won', u'wouldn']

filtered_words = []
final_filtered_words=[]
for i in words:
    stopword[i]=1
for i in citation_sentences:
    i = i.replace('-\n', "")
    i = i.replace('\n',' ')
    try:
        i = str(i)
        if i == "References":                            #remove the references part
            break
        if len(i)>1:
            b = word_tokenize(i)                         #word tokeniser
            for s in b:
                #if len(s)>1:
                #    try:
                #        stopword[s]                     #stopwords cannot be removed before ner recognition.
                #    except:
                filtered_words.append(s)
            final_filtered_words.append(filtered_words)         #list of lists of tokenised words per sentence.
            filtered_words=[]
    except:
        i = "a" #Do something. 
#print final_filtered_words


pos_list=[]
final_pos_list=[]
named_entity=[]
save=""
flag=0
for i in final_filtered_words:
    if len(i)>2:
        #print i
        temp = nltk.pos_tag(i)                           #POS Tagging
        #namedEnt = nltk.ne_chunk(temp)			 ###ner recognition
        #print temp		 			 #gives all the pos per sentence. 
        for word in temp:
            #print word[0]
            one = word[0].decode('string-escape')
            print one
            if (len(one)>1) and (one.find('/')<0) and (one.find('|')<0): #removing mathematical terms if any
                if word[1]=="NNP":
                    save+=one+" "
                    flag=1
                elif word[1][0]=="N":
                    if flag==1:
                        flag=0
                        #print save
                        named_entity.append(save)
                        save=""
                    if word not in stopword:
                        #print word[0]
                        named_entity.append(one)
print named_entity							# list of all named entities
    
