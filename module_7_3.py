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


mytxt = WordsFinder('products.txt','test.txt')
mytxt.get_all_words()