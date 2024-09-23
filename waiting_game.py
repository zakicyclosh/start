import time 
import os 
def waiting_game ():
 while True :
   os.system('cls' if os.name == 'nt' else 'clear')
   print('Your target time is 4 seconds. /n ---press enter to begin---')
   star_time = time.perf_counter()
   input('---Press enter again after 4 seconds---')
   Elapsed_time = time.perf_counter() - star_time
   if Elapsed_time == 4 :
      print('You re insaaaaaaane !!!!')
   elif Elapsed_time > 4 :
      print(f'({Elapsed_time - 4 : .3f}seconds too slow)')
   else :
      print(f'({4 - Elapsed_time : .3f}seconds too fast)')

   time.sleep(4)



waiting_game()
