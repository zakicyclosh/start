number = input("enter a number :")
### def to find the primes of the input number 
def find_all_number_prime (number) :
  prime_number = []
  devisor = 2
  if number.isdigit() == False : #### this line is to check if the input is an int if true we continue if False the function retun "this is not an number"
   print("this is not an number")
   return None
  else :
    number = int(number)     ### after checking thatnumber is an int , we need to convert the number to int as input return auto an str type
    while number >= devisor : ### while the number given by the user is bigger or equal the devisor we gonna enter this loop
        if number % devisor != 0 : #### we check first if number is prime of the 1st devisor if not we add 1 to the devisor 
         devisor += 1
        else :  
         prime_number.append(devisor)
         number = number/devisor
        
  print("the primes of the number",prime_number)


find_all_number_prime(number)