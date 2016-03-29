from os import listdir
#with open('b_text') as line:
#    data=line.readlines()
import slate
import nltk
import re
#data = open('b_text', 'r').read()            #extracted pdf data
#data = data.decode('utf-8')
#print data
import codecs
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import subprocess
#sent_tokenize_list = sent_tokenize(data)       #sentence tokenisation
#print len(sent_tokenize_list)
sent=[]
stopword={}
words = stopwords.words('english')
for i in words:
    stopword[i]=1
with open('unique_authors.txt') as f:
    authors = f.readlines()
    authors_list=[]
    authors_filtered_full_NNPS=[]
    for i in authors:
        i = i.split('\t')
        #print i[0]
        authors_list.append(i[0])
#print authors_list
count = 0
text_file_list=[]
for fle in listdir("PAKDD-3year"):
    if fle[-5]=="_":
        
        text_file_list.append(fle)
        #print len(text_file_list)
        named_entity=[]
        save=""
	data = open("./PAKDD-3year/"+fle, 'r').read()            #extracted pdf data
	data = data.decode('utf-8')
	sent_tokenize_list = sent_tokenize(data) #sentence tokenization
        op = open("./entities/"+fle+"_entity","wb")
        #print len(sent_tokenize_list)    
	for i in sent_tokenize_list:
    	    i =  i.split('\n\n')
            for j in i:
                if len(j)>3:
                    sent.append(j)      

	full_text_filtered_words=[]
	full_text_final_filtered_words=[]
        citation_filtered_words=[]
	save=""
        citation_sentences=[]
	for i in sent:
    	    i = i.replace('-\n',"")
            i = i.replace('\n'," ")
                  #split different lines
    	    try:
                i = str(i)
                
                if len(i)>1 and i!="References":
                    b = word_tokenize(i)                         #word tokeniser
                    for s in b:
                	full_text_filtered_words.append(s)
            	    full_text_final_filtered_words.append(full_text_filtered_words) #list of listsof tokenised words per sentence.
                    if re.match('.*\[.*\].*', i, re.DOTALL):   #extracting all the sentences having citations for e.g.[1],[3, 5]
                        citation_sentences.append(i)
                        citation_filtered_words.append(full_text_filtered_words) 
			#writing those sentences extracted from the pdf in a file(sentence wise).
                full_text_filtered_words=[]
    	    except:
                i = "a" #Do something. 
	#print citation_sentences
	full_text_NNPS=[]
	for i in full_text_final_filtered_words:
    	    temp = pos_tag(i)
    	    #print temp
    	    for word in temp:
                one = word[0].decode('string-escape')
                if(len(one)>1) and (one.find('/')<0) and (one.find('|')<0): #removing mathematical terms if any
                    if word[1]=="NNP":
                        save+=one+" "
                        flag=1

                    else:
                        flag=0
                        if save and save not in stopword:
                            full_text_NNPS.append(save)
                            save=""
	#print "full_text_NNPs"
	#print full_text_NNPS
   
	authors_filtered_full_NNPS=set()
	for i in full_text_NNPS:
    	    dot_flag=0
            il = i.lower()
            for letter in il:
                if letter ==".":
                    dot_flag=1
    	    if dot_flag==0:
                il = il.split(" ")
                l=[]
        	for text_word in il:
            	    if text_word :
                        l.append(filter(lambda x: text_word in x, authors_list))
        	if len(l[0])==0:
                    authors_filtered_full_NNPS.add(i)
        #print "filtered_full_NNPS"
        op.write(str(authors_filtered_full_NNPS))
        op.write("\n") 
        print authors_filtered_full_NNPS
         	
	full_citation_NNPS=[]
	for i in citation_filtered_words:
    	    temp = pos_tag(i)
    	    #print temp
    	    for word in temp:
                one = word[0].decode('string-escape')
                if(len(one)>1) and (one.find('/')<0) and (one.find('|')<0): #removing mathematical terms if any
                    if word[1]=="NNP":
                        save+=one+" "
                        flag=1

                    else:
                        flag=0
                        if save and save not in stopword:
                            full_citation_NNPS.append(save)
                            save=""
	#print "full_citation_NNPs"
	#print full_citation_NNPS
   
	authors_filtered_citation_NNPS=set()
	for i in full_citation_NNPS:
    	    dot_flag=0
            il = i.lower()
            for letter in il:
                if letter ==".":
                    dot_flag=1
    	    if dot_flag==0:
                il = il.split(" ")
                l=[]
        	for text_word in il:
            	    if text_word :
                        l.append(filter(lambda x: text_word in x, authors_list))
        	if len(l[0])==0:
                    authors_filtered_citation_NNPS.add(i)
        #print "filtered_citation_NNPs"
        op.write(str(authors_filtered_citation_NNPS))
        op.write("\n")
        print authors_filtered_citation_NNPS
        op.close()

	count = count + 1
        print "Paper Number : "
        print  count 
       
        if count > 5:
            break


