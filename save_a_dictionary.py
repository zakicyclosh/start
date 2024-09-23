import json
fruit = {'banana' : 'yellow' , 'orange': 'orange' , 'strawberry' : 'red' }
path = '/workspaces/start/folder_of_file_path/save_a_dictionnary.json'
def save_dict (fruit) :
 path = '/workspaces/start/folder_of_file_path/save_a_dictionnary.json'
 dict_to_save = fruit
 with open (path, 'w') as my_file :
  json.dump(fruit, my_file )
    

def load_dict (path):
 with open(path,'r') as my_file:
    d = json.load(my_file)
    print(d)


save_dict(fruit)

load_dict(path)
