_string = input ('enter a word :')     

def sort_a_string(_string) :
 list_string = _string.split(' ')          ### get each string which sperated with white space 
 list_string = sorted(list_string,key = str.casefold) ### sort the string using sort function and key str.casefold return list of strings sorted
 print(' '.join(list_string))     ### created a sentence using the sorted list and keeping the gap between them as space


sort_a_string(_string)