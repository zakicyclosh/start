


path = '/workspaces/start/folder_of_file_path/password.txt'
n_of_word = input ('enter the desired number of word :')



def generate_password (n_of_word,path):
    with open (path,'r') as file :
        d = file.read()
        print(d)





generate_password(n_of_word, path)