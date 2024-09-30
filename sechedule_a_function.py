import sched
import time


def schedule_a_function(event_time,function,*args) :
    s = sched.scheduler(time.time,time.sleep)
    s.enterabs(event_time,1,function,argument=args)
    print(f'{function}{args}scheduled for {time.asctime(time.localtime(event_time))}')
    s.run()


schedule_a_function(time.time()+360,print,'hello!')