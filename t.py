from os import listdir
import slate
import nltk
import re
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
#words = stopwords.words('english')
stopword = ['http','www','com','introduction','cid','years','document','topic','topics','subtopics','results']
#for i in words:
#    stopword[i]=1
'''with open('unique_authors.txt') as f:
    authors = f.readlines()
    authors_list=[]
    authors_filtered_full_NNPS=[]
    for i in authors:
        i = i.split('\t')
        #print i[0]
        authors_list.append(i[0])
#print authors_list
'''
count = 0
text_file_list=[]
for fle in listdir("test1"):
    if fle[-5]=="_":
        print fle 
        text_file_list.append(fle)
        #print len(text_file_list)
        named_entity=[]
        sent=[]
        save=""
        nme=""
	data = open("./test1/"+fle, 'r').read()            #extracted pdf data
	data = data.decode('utf-8')
	sent_tokenize_list = sent_tokenize(data) #sentence tokenization
    	op = open("./entities1/"+fle+"_entity","wb")
    	print len(sent_tokenize_list)    
    	for i in sent_tokenize_list:
            print i
    	    i =  i.split('\n\n')
            
            for j in i:
                #print j
                if len(j)>3:
                   sent.append(j)      
        print len(sent)
    	full_text_filtered_words=[]
    	full_text_final_filtered_words=[]
    	citation_filtered_words=[]
    	save=""
    	nme=""
    	citation_sentences=[]
    	flag=0
    	for i in sent:
            i = i.replace('-\n',"")
            i = i.replace('\n'," ")
            print i
            #split different lines
    	    full_text_NNPS=[]
    	    authors_filtered_full_NNPS=set()
    	    authors_filtered_citation_NNPS=set()
            iscitation=0
            '''
            if flag==0 and i=="Abstract":
                print i
                flag=1
                continue
            try:
                i = str(i)
                
                if flag==0:
                    continue
                if i=="References":
                    break
                if len(i)>1:
                    
		    if re.match('.*\[.*\].*', i, re.DOTALL):   #extracting all the sentences having citations for e.g.[1],[3, 5]
                        iscitation = 1
		    b = word_tokenize(i)                         #word tokeniser
    	    	    temp = pos_tag(b)
    	    	    #print temp
    	    	    for word in temp:
                        one = word[0].decode('string-escape')
                        if 1:
                        #if(len(one)>1) and (one.find('/')<0) and (one.find('|')<0) and one not in stopword: #removing mathematical terms if any
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
                                    nnp_flag=0
                        	if nme:
                                    full_text_NNPS.append(nme)
                            	    nme=""
                            	    nn_flag=0
                    #for s in b:
    		    for i in full_text_NNPS:
            		notauniversity=0
            		isalgo=0
    	    		notdot_flag=1
            		il = i.lower()
            		for letter in il:
                	    if letter ==".":
                    		notdot_flag=0
    	    		#if dot_flag==0:
            		#    il = il.split(" ")
            		#    l=[]
        		#for text_word in il:
            		#	    if text_word :
            		#            l.append(filter(lambda x: text_word in x, authors_list))
            		if il.find('university')==-1 and i.find('institute')==-1 and i.find('college')==-1:
                	    #not a university name
                	    notauniversity=1
            		if il.find('algorithm')!=-1 or il.find('technique')!=-1:
                	    isalgo=1
            		if (notauniversity and notdot_flag):
                            authors_filtered_full_NNPS.add(i + "NNP")
 			    if iscitation:
				authors_filtered_citation_NNPS.add(i + "NNP")
	    
	    		if isalgo:
                	    authors_filtered_full_NNPS.add(i + "NN")
                            if iscitation:
                                authors_filtered_citation_NNPS.add(i+"NNP")
       			    #print "filtered_full_NNPS"
            except:
                i="a"
        op.write(str(authors_filtered_citation_NNPS))
    	op.write("\n") 
    	print authors_filtered_citation_NNPS
                    
   
         	
	op.close()
        count = count + 1
        print "Paper Number : "
        print  count 
       
    	#if count > 5:
        #      break'''
