from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
import os
path_dir="E:/fyp2/codes/index_table_generation/files/Text_Files"
dir_list = os.listdir(path_dir)
for x in dir_list:
    text = open(f"Text_Files/{x}").read().lower()
    stopWords = set(stopwords.words('english'))
    stopWords.update((',','.',':','and','I','A','And','So','arnt','This','When','It','many','Many','so','cant','Yes','yes','No','no','These','these','his'))
    stopWords.update(('his','one','could','try','may'))
#stopWords = set(nltk.corpus.stopwords.words('english'))
#stopWords.append('.')
    words = word_tokenize(text)
    wordsFiltered = []

    for w in words:
       if w not in stopWords:
          wordsFiltered.append(w)
    def listToString(s): 
    
    # initialize an empty string
        str1 = " " 
    
    # return string  
        return (str1.join(s))

    string=listToString(wordsFiltered)
#print(wordsFiltered)
    f = open(f"Stemming/{x}", "w")
    f.write(string)
    f.close()


