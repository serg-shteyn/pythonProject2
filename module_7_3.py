#Оператор "with"
from io import open_code


class WordsFinder:
    file_names = []

    def __init__(self, *files):
        for i in files:
            self.file_names.append(i)

    def get_all_words(self):
        all_words={}
        for i in self.file_names:
            with open(i,encoding='utf-8') as file:
                words = []
                for line in file:
                    words += self.trim_line(line).split()
            all_words[i] = words
        return all_words

    def trim_line(self,line):
        trim_chars = [',', '.', '=', '!', '?', ';', ':', ' - ']
        line  = line.lower()
        for i in trim_chars:
            line = line.replace(i,'')
        return line
        
    def find(self,word):
    	res={}
    	for key, value in self.get_all_words().items():
    		for i in range(len(value)):
    			if value[i].lower()==word.lower():
    				res[key]=i+1
    				break
    			else:
    				res[key]=(f'not find {word}')
    	return res
    	
    def count(self,word):
    	res={}
    	for key, value in self.get_all_words().items():
    		count=0
    		for i in range(len(value)):
    			if value[i].lower()==word.lower():
    				count+=1
    		res[key]=count
    	return res
    	
				
			


mytxt = WordsFinder('Rudyard_Kipling.txt')
print(mytxt.get_all_words())

print(mytxt.find('iF')) # 1 слово по счёту
print(mytxt.count('iF')) # 14 слов iF в тексте всего
