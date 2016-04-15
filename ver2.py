from os import listdir
import slate
import nltk
import re
import csv
tot = csv.writer(open("finaltokens.csv",'wa'))
stemmer = nltk.stem.porter.PorterStemmer()
#tot=open('total.txt',"wa")
#data = open('b_text', 'r').read()            #extracted pdf data
#data = data.decode('utf-8')
#print data
#import codecs
#from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import subprocess
#sent_tokenize_list = sent_tokenize(data)       #sentence tokenisation
#print len(sent_tokenize_list)
sent=[]
stopword={}
total_words=set()
#words = stopwords.words('english')
orglist=['ieee','acm','icml']
stopword = ['http','www','com','introduction','cid','years','document','topic','topics','subtopics','results']
#for i in words:
#    stopword[i]=1
with open('unique_authors.txt') as f:
    authors = f.readlines()
    authors_list=set()
    authors_filtered_full_NNPS=[]
    for i in authors:
        i = i.split('\t')
        #print i[0]
        authors_list.add(i[0])
"""with open('places.txt') as f:
    places = f.readlines()
    places_list =set()
    for i in places:
        i = i.split('\t')
        #print i[0]
        places_list.add(i[2])
"""
#print authors_list
count = 0
#text_file_list=[]
for fle in listdir("Text"):
    print fle 
    #text_file_list.append(fle)
    #print len(text_file_list)
    named_entity=[]
    sent=[]
    save=""
    nme=""
    data = open("./Text/"+fle, 'r').read()            #extracted pdf data
    data = data.decode('utf-8')

    sent_tokenize_list = sent_tokenize(data) #sentence tokenization
    op = open("./entities/"+fle+"_entity","wb")
    #print (sent_tokenize_list)    
    full_text_filtered_words=[]
    full_text_NNPS=[]
    citation_filtered_words=[]
    save=""
    nme=""
    citation_sentences=[]
    flag=0
    for i in sent_tokenize_list:
        i = i.replace('-\n',"")
        i = i.replace('\n'," ")
        #i = re.sub(r'\W+', '', i)
        #print type(i)
        #split different lines
        ck=i.find("Abstract")
        if flag==0 and ck>-1:
                #print i
                flag=1
                continue
        try:
            #i = str(i)
	    #print i
            if flag==0:
                continue
            k=i.find('References')                    #removing all content in references
            if k>-1:
                #i=i[:k]
		break
            #print i
            if re.match('.*\[.*\].*', i, re.DOTALL) or re.match('.*\([a-z]*.*[0-9]{4}.*\).*', i, re.DOTALL): #extracting all the sentences having citations for e.g.[1],[3, 5]
                b = word_tokenize(i)
                temp = pos_tag(b)
		#print i
                #word tokenised and tagged
                
                citation_sentences.append(i)
                for word in temp:
                    one = word[0].decode('string-escape')
                    if (len(one)>1) and (one.find('/')<0) and (one.find('|')<0): #removing mathematical terms if any
                        if word[1]=="NNP":
                            save+=one+" "
                            if nme:
                                full_text_NNPS.append(nme)
                                nme=""

                        elif word[1]=="NN":
                            nme+=one+" "
                            if save :
                                full_text_NNPS.append(save)
                                save=""
        
                        else:
                            if save :
                                full_text_NNPS.append(save)
                                save=""

                            if nme:
                                full_text_NNPS.append(nme)
                                nme=""
        except:
            pass
        authors_filtered_citation_NNPS=set()
        for i in full_text_NNPS:
            notauniversity=0
            isalgo=0
	    
            isnotorg=1
            notdot_flag=1
	    isauth=1
	    isplace=1
            il = i.lower()
	    #print il
	    if il.isdigit():
		#print il
		continue
            #for letter in il:
            #    if letter ==".":
            #        notdot_flag=0
            if il.find('conference')!=-1 or il in orglist:
                isnotorg=0
            #if dot_flag==0:
            #    il = il.split(" ")
            #    l=[]
                #for text_word in il:
            #       if text_word :
            #            l.append(filter(lambda x: text_word in x, authors_list))
            if il.find('university')==-1 and i.find('institute')==-1 and i.find('college')==-1 and i.find('dataset')==-1 and i.find('set')==-1 and i.find('use')==-1 and i.find('research')==-1 and i.find('column')==-1 and i.find('name')==-1 and i.find('patent')==-1 and i.find('c++')==-1 and i.find('python')==-1 and i.find('equation')==-1 and i.find('approach')==-1:
                #not a university name
                notauniversity=1
            if il.find('algorithm')!=-1 or il.find('technique')!=-1 or il.find('method')!=-1 :
                isalgo=1
	    """for author in authors_list:
		if il==author:
			isauth=0
			break"""
	    """for place in places_list:
		if il==place:
			isplace=0
			break"""
            word = re.sub(r'\W+', '', il)
            word = stemmer.stem(word).lower()
            if (notauniversity and notdot_flag and isnotorg and isauth):
                authors_filtered_citation_NNPS.add(word)# + "NNP")
        
            if isalgo:
                authors_filtered_citation_NNPS.add(word)# + "NN")
        #print "filtered_full_NNPS"
    op.write(str(authors_filtered_citation_NNPS))
    op.write("\n")
    #print authors_filtered_citation_NNPS
    op.close()
    #total_words = total_words.union(authors_filtered_citation_NNPS)
    count = count + 1
    print "Paper Number : "
    print  count 
    """if count>10:
        break"""
    tot.writerow(list(authors_filtered_citation_NNPS))
    #f.write(str(total_words))
