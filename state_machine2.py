
import time
from enum import Enum
import threading

class State(Enum):
    startup = 1
    shutdown = 2
    waiting = 3
    write = 4

class joint:
    
    def __init__(self,joint_num):
        self.type = 0    # instance variable unique to each instance
        self.name = "joint"+str(self.type)
        self.jobs = ['left','right','help me','africa by toto']
        self.state = State.startup
        #ser = Serial()
        self.ser = object()
        self.startup()
        


    def is_ready(self):
        return self.state == State.waiting
    
    def set_finished(self):
        self.state = State.shutdown
        
    def get_finished(self):
        return self.state == State.shutdown
        
    def update_jobs(self,new_tasks):
        self.jobs.extend(new_tasks)
        
    def get_jobs(self):
        return self.jobs
    
    def startup(self):
         x = threading.Thread(target=self.serial_state_machine_startup)
         x.start()
         #x.join()
         print("done?")
        
        

    def serial_state_machine_startup(self):
        
        # do_startup
        while (self.state == State.startup):
            if (self.startup_successful()):
                self.state = State.waiting
            else:
                self.state = State.shutdown
            
        if (self.state == State.waiting):
            self.serial_state_machine_waiting()
            
        elif(self.state == State.shutdown):
             self.serial_state_machine_shutdown()   
    

    def serial_state_machine_waiting(self):
        while (self.state == State.waiting):
            if (len(self.get_jobs())> 0 ):
                self.state = State.write     
            
        if (self.state == State.write):
            self.serial_state_machine_write()
            
        elif(self.state == State.shutdown):
             self.serial_state_machine_shutdown()   
        
    
    def serial_state_machine_write(self):
        #ser = self.ser
        # will wait in this state until it gets a command
        #print(jobs)
        #print(state)
        #jobs = self.get_jobs()
        job = self.get_jobs().pop(0)
        job_finished = False
        while (self.state == State.write and not job_finished):
            print("thread"+self.name+":"+job)
            #print()
            time.sleep(1)
            job_finished = True
            # compile job into required format
            # send job over serial to robot arm
            # confirm job has been completed
            
        
        if(self.state == State.shutdown):
            self.state = State.shutdown
            self.serial_state_machine_shutdown()
        elif (len(self.get_jobs())>0):
            self.state = State.write
            self.serial_state_machine_write()       
        elif(len(self.get_jobs()) == 0):
            self.state = State.waiting
            self.serial_state_machine_waiting() 
    
    
    def serial_state_machine_shutdown(self):
        #ser.close()
        print("shutdown complete")
        return 0
        # maybe return arm to starting point 
    
    def startup_successful(self):
        return True
   
    '''
Axis_0 = joint(0)

while(not Axis_0.is_ready()):
    time.sleep(0.1)

Axis_0.update_jobs(["do a new job"]) 

time.sleep(0.1)
while(not Axis_0.is_ready()):
    time.sleep(1)

time.sleep(0.1)
Axis_0.set_finished()

'''
'''
new_jobs = ['startup','move up', 'move left', 'move claw','play africa by toto']
finished = False
#serial_state_machine_generic(0)
serial_state_machine_startup()
time.sleep(3)
new_jobs = ['another job']
finished = True

'''