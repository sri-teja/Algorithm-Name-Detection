from os import listdir
from stop_words import get_stop_words
#stop_words = get_stop_words('english')
stop_words=['http','www','com','https','png','jpg','cid','years','document','topic','topics','subtopics']
import slate
import nltk
import re
from nltk import pos_tag, word_tokenize
from nltk import PorterStemmer
if 1:
	"""for fle in listdir("PAKDD-3year"):
	print fle
	with open("PAKDD-3year/"+fle) as f:"""
	with open('TWave High-Order Analysis of Spatiotemporal Data.pdf') as f:
		doc = slate.PDF(f)
		print type(doc)
		#doc=re.findall(r"[\w]+", doc.lower())
	#print doc
	named_entity=[]
	tr=""
	flag=0
	for content in doc:

		k=content.find('References')					#removing all content in references
		if k>-1:
			content=content[:k]
			#print content
		#tokenizing paragraphs
		para=re.split(r'[.\t]*', content)

		for sentence in para:							#sentence tokenization
		 #print "sentence",sentence,
		 if re.match('.*\[.*\].*', sentence, re.DOTALL):
		 	#print sentence
			listt=re.findall(r"[\w]+", sentence) 	#word tokenization
			temp = nltk.pos_tag(listt)
			for z in temp:
				if z[1]=="NNP":						#merging named entities into a single word
					tr+=z[0]+" "
					flag=1
				elif z[1][0]=="N":
					#print z
					if z[0] not in stop_words:
						named_entity.append(z[0])
					if flag==1:
						flag=0
						named_entity.append(tr)
						tr=""	
				else:
					if flag==1:
						flag=0
						named_entity.append(tr)
						tr=""	
					del z
	print "named_entity"
	for x in named_entity:
				print x
