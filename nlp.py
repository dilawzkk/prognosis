import nltk
inp=open("input.txt").read()
noun=nltk.word_tokenize(inp)
print noun
f=open('medterm.txt','w')

for i in range(len(noun)):
  with open('symtom.txt','r') as f1:
    for line in f1:
      for word in line.split():
	    if noun[i] == word :
		  f.write(noun[i]+'\n')
	

