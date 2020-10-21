
import time

from enum import Enum


class State(Enum):
    startup = 1
    shutdown = 2
    waiting = 3
    write = 4

class joint:
    
    def __init__(self,joint_num):
        self.type = joint_num    # instance variable unique to each instance
        self.name = "joint"+str(self.type)
        self.jobs = ['left','right','africa by toto']
        self.state = State.startup
        self.state = State.startup
        #ser = Serial()
        self.ser = object()

    def is_ready(self):
        return self.state== State.waiting
    
    def set_finished(self):
        self.state = State.shutdown
        
    def get_finished(self):
        return self.state == State.shutdown
        
    def update_jobs(self,new_tasks):
        self.jobs.extend(new_tasks)
        
    def get_jobs(self):
        return self.jobs
    
    def startup(self):
        self.serial_state_machine_startup(self.ser,self.jobs)
        
    
    #self.serial_state_machine_startup()
    

    def serial_state_machine_startup(self,ser,jobs):
        state = self.state
        # do_startup
        while (state == State.startup):
            if (self.startup_successful()):
                state = State.waiting
            else:
                state = State.shutdown
            
        if (state == State.waiting):
            self.serial_state_machine_waiting(state,ser,jobs)
            
        elif(state == State.shutdown):
             self.serial_state_machine_shutdown(state,ser,jobs)   
    
    def serial_state_machine_waiting(self,state,ser,jobs):
        start = time.time()
        print("write:")
        while (state == State.waiting):
            jobs = self.get_jobs()
            if (len(jobs)>0):
                state = State.write     
            if (self.get_finished()or (time.time()-start)>2.0):
                state = State.shutdown
            
        if (state == State.write):
            self.serial_state_machine_write(state,ser,jobs)
            
        elif(state == State.shutdown):
             self.serial_state_machine_shutdown(state,ser,jobs)   
        return 0 
    
    def serial_state_machine_write(self,state,ser,jobs):
        # will wait in this state until it gets a command
        print("write:")
        job = jobs.pop(0)
        job_done = False
        while (state == State.write and not job_done):
            time.sleep(1)
            print(job)
            job_done = True
            # compile job into required format
            # send job over serial to robot arm
            # confirm job has been completed
        
        if(state == State.shutdown):
            self.serial_state_machine_shutdown(state,ser,jobs)
        elif(len(jobs) == 0):
            state = State.waiting
            self.serial_state_machine_waiting(state,ser,jobs)
        elif (len(jobs)>0):
            self.serial_state_machine_write(state,ser,jobs)        
    
    
    def serial_state_machine_shutdown(self,state,ser,jobs):
        #ser.close()
        print("shutdown complete")
        return 0
        # maybe return arm to starting point 
    
    def startup_successful(self):
        return True
    
a = joint(0)
#a.update_jobs(["do a new job"])
a.startup()
time.sleep(1)
a.set_finished()

print(a.get_finished())
'''
new_jobs = ['startup','move up', 'move left', 'move claw','play africa by toto']
finished = False
#serial_state_machine_generic(0)
serial_state_machine_startup()
time.sleep(3)
new_jobs = ['another job']
finished = True

'''