import string
given_word = input("enter a word :")   ### we clean the text make it lower delete punctuation and white space 
given_word = given_word.lower()
given_word = given_word.translate(str.maketrans('','',string.punctuation))
given_word = given_word.replace(' ','')
 

def ispalindrome(given_word) :
    reversed_word = given_word[::-1]          ### the function help check if the given word and reversed are the same and can be pronounced from both side with ignoring spaces and punctuation.
    for char in given_word : 
        if char.isdigit() == True :    ### here we check if the string has an number if so return an error message 
            print('we only consider letter')
            return None
    if given_word != reversed_word :
        return False
    return True

print(ispalindrome(given_word)) ### try level, race car , go hang a salami - i 'm a lasagna hog.

