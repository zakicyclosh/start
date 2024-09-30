from collections import Counter
import re

path = '/workspaces/start/folder_of_file_path/txt_file.txt'
def count_words(path) :
    with open (path,'r',encoding = 'UTF-8') as txt:
        d = txt.read()
        word_list = re.findall(r"[0-9a-zA-Z-']+",d)
        word_list = [word.upper() for word in word_list]
        count = Counter(word_list)
        for word in word_list :
            count[word] += 1
        print ( f'Total words : {len(word_list)}')
        print('Top 20 words:')
        for word , value in count.most_common(20) :
            print(f'{word}:{value}')

count_words(path)
