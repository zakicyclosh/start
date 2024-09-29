from collections import Counter
import random 


def roll_dice (*dice) :
    final_sum_list = []
    counts = Counter()
    for i in range(1000001):
            counts[sum((random.randint(1,side) for side in dice))] += 1
            

    print ('outcomes')
    for outcomes in range (len(dice) ,sum(dice)+1):
     probabilities =  counts[outcomes] * 100 / 1000000
     print(f'{outcomes}:{probabilities:.2F}%')
    


roll_dice(6,6,4)