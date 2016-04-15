from gensim import models
model = models.Word2Vec.load('./model3.dat')
from os import listdir
import os
import re
tp=['neuralnetwork','datamin','kmean','matrix','neighbor','crf','hmm','lda','svm','knn','decisiontreebas','backprop','spade','tfidf','mergesort','c45tree','search','plsa','machinelearn','cluster','randomforest','network','markov','reinforcementlearn','cart','regressiontre','naivebay','minmax','graph','algorithm','method']

fp=['associ','accept','accuraci','research','refer','vari','facebook','stream','task','target','addit','time','inform','uncertainti','factor','detect','online','system','group','distance','vector','part','type','express','imag','springer','world','busin','news','problem','concept','dataset','databas','approach','method','success','algorithm','analysi','acmsymposium','ieee','evalu','process','model']
import csv
ifile= open("finaltokens.csv","rb")
reader = csv.reader(ifile)
import numpy
ct=0
path = "./Output/"
if not os.path.exists(path):
    os.makedirs(path)



for fle, row in zip(listdir('Text'),reader):
	ct+=1
	ple=0
	f1 = open(path+fle[:-5]+"_tp","wa")
	f2 = open(path+fle[:-5]+"_fp","wa")
	#f3 = open(path+fle[:-5]+"_mc","wa")
	tokens=set()
	false_tokens=set()
	misc=set()
        #print row
        #f1.write(str(ct)+"\n")
        #f2.write(str(ct)+"\n")
        #f3.write(str(ct)+"\n")
	for col in row:
		if col.isdigit():
			continue
		if re.match(".*cid[0-9].*",col):
			continue
		isadd=0
		isfalseadd=0
		for entry in fp:
				try:
					if model.similarity(entry,col)>0.35:
						false_tokens.add(col)
						isfalseadd=1
						break
                    		except:
					pass
		"""for entry in fp:
				try:
					if col.find(entry)!=-1:
						false_tokens.add(col)
						isfalseadd=1
						break
				except:
					pass
		"""
		if not isfalseadd:	
		 for entry in tp:
                	try:
				if model.similarity(entry,col)> 0.35:
					tokens.add(col)
					isadd = 1
					ple=1
					break
			except:
				pass
		 for entry in tp:
			try:
				if col.find(entry)!=-1:
					tokens.add(col)
					isadd=1
					ple=1
					break
			except:
				pass
			
		if not isadd and not isfalseadd:
			misc.add(col)
	if ple==0:
                #f1.write(x[0]+"\n")
		print ct
	f1.write(str(tokens)+"\n")	
	f2.write(str(false_tokens)+"\n\n")
	f2.write(str(misc)+"\n")

	
		
