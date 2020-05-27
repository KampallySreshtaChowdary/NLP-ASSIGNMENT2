import nltk

sreshta_file = open('sreshta_b160809cs.txt', 'r')
text = sreshta_file.read()
print("-----------------------------------------------------------------")
print(text)
print("-----------------------------------------------------------------")
for line in sreshta_file.readlines():
 if line!="\n":
     words = line.split(" ")
     for word in words:
         if not word.lower() in set(nltk.corpus.stopwords.words("english")):
             appendFile = open('stopwords_removed.txt','a')
             appendFile.write(" "+word)
             appendFile.close() 
             
file = open("stopwords_removed.txt", 'r')
text = file.read()             
print("-----------------------------------------------------------------")        
print(text)
print("-----------------------------------------------------------------")
sres_words = nltk.word_tokenize(text)
print("-----------------------------------------------------------------")        
print(sres_words)
print("-----------------------------------------------------------------")

porter = nltk.PorterStemmer()
text=""
for word in sres_words:
    text += porter.stem(word) + " "
outputfile = open("Output_sres.txt", "w")
outputfile.write(text)
outputfile.close()
