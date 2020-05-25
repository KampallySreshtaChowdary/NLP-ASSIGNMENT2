import nltk
import string
sreshta_file = open('sreshta_b160809cs.txt', 'r')
text = sreshta_file.read()
print("-----------------------------------------------------------------------")
print(text)
print("-----------------------------------------------------------------------")
cleantext=""
i=0
while i < len(text):
    if text[i] != '\n' and text[i] != '-':
        cleantext += text[i]
        i=i+1
    elif text[i] == '-' and text[i+1] == ' ':
        i=i+2
    else:
        cleantext += ' '
        i=i+1
print("-----------------------------------------------------------------------")        
print(cleantext)
print("-----------------------------------------------------------------------")
sres_words = nltk.word_tokenize(cleantext)
print("-----------------------------------------------------------------------")        
print(sres_words)
print("-----------------------------------------------------------------------")
descriptive = set(sres_words) - set(nltk.corpus.stopwords.words("english"))
print("-----------------------------------------------------------------------")        
print(descriptive)
print("-----------------------------------------------------------------------")
porter = nltk.PorterStemmer()
text=""
for word in descriptive:
    text += porter.stem(word) + ' '
print("-----------------------------------------------------------------------")        
print(text)
print("-----------------------------------------------------------------------")
outputfile = open("Output_sres.txt", "w")
outputfile.write(text)
outputfile.close()
