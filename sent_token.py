#with open('b_text') as line:
#    data=line.readlines()
#print data
import nltk
data = open('b_text', 'r').read()
data = data.decode('utf-8')
#print data
import codecs
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
sent_tokenize_list = sent_tokenize(data)
print len(sent_tokenize_list)
final_sent=[]
final_sent.append(sent_tokenize_list[0])
final_sent.append(sent_tokenize_list[1])
#for i in sent_tokenize_list:
#    print i
'''final_sent=[]
for i in sent_tokenize_list:
    i = i.split('\n\n')
    for j in i:
        if len(j)>3:
            final_sent.append(j)
'''
#print final_sent
sent=[]
for i in sent_tokenize_list:
    i =  i.split('\n\n')
    for j in i:
        if len(j)>3:
            sent.append(j)

f = codecs.open('sent_output2.0', 'w', encoding='utf8')
for i in sent:
    i = i.replace('-\n', "")
    i = i.replace('\n',' ')
    
    #print i
    #print ""
    f.write(i+'\n')

words_tokenised=[]
full_file_tokeniser=[]
stopword={}
#words = stopwords.words('english')
#print words
words = [u'.', u',', u'This', u'In', u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why', u'how', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'no', u'nor', u'not', u'only', u'own', u'same', u'so', u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don', u'should', u'now', u'd', u'll', u'm', u'o', u're', u've', u'y', u'ain', u'aren', u'couldn', u'didn', u'doesn', u'hadn', u'hasn', u'haven', u'isn', u'ma', u'mightn', u'mustn', u'needn', u'shan', u'shouldn', u'wasn', u'weren', u'won', u'wouldn']

filtered_words = []
final_filtered_words=[]
for i in words:
    stopword[i]=1
for i in sent:
    i = i.replace('-\n', "")
    i = i.replace('\n',' ')
    try:
        i = str(i)
        if i == "References":
            break
        if len(i)>1:
            b = word_tokenize(i)
            for s in b:
                if len(s)>1:
                    try:
                        stopword[s]
                    except:
                        filtered_words.append(s)
            final_filtered_words.append(filtered_words)
            filtered_words=[]
    except:
        i = "a" #just random. No use of this line 
#for i in final_filtered_words:
#    for j in i:
        #print j

pos_list=[]
final_pos_list=[]
for i in final_filtered_words:
    if len(i)>2:
        #print i
        temp = nltk.pos_tag(i)
        namedEnt = nltk.ne_chunk(temp)
        print namedEnt
        #namedEnt.draw()
        #print temp
        #pos_list.append(temp)
    	final_pos_list.append(temp)
    #pos_list=[]

#print final_pos_list

