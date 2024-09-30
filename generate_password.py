import re
import random


path = '/workspaces/start/folder_of_file_path/password.txt'
n_of_word = int(input ('enter the desired number of word :'))



def generate_password (n_of_word,path):
    password = []
    result_dict = []
    d_= {}
    with open (path,'r') as f :
       f = f.read()
       try :
        lines = f.split('\n')
        for line in lines:
            d = line.split('\t')
            try :
                result_dict.append(d)
            except KeyError:
               pass
       except ValueError:
        pass
    for sublist in result_dict :
        try :
            key = int(sublist[0]) if sublist[0].isdigit() else sublist[0]
            d_[key] = sublist[1]
        except (KeyError,IndexError):
               pass
        
    
    for _ in range(n_of_word):
      count = 0
      sum_of_number = []
      random_number_ = str()
      while count < 5 :
          random_number = random.randint(1,6)
          random_number_ += str(random_number)
          count += 1
      sum_of_number.append(random_number_)
      for item in sum_of_number :
        password.append(d_[int(item)])

     ###while True :
         #try :
           ## random_number = random.randint(11111,66666)
            #password.append(d_[random_number])
           # break
        # except (KeyError,IndexError):
              # pass
            
    print(f'Your password is :{' '.join(password)}\n Make sure to save in secure place.')
        





generate_password(n_of_word, path)