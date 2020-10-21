
#from datetime import datetime
import time
#import numpy as np 
from enum import Enum

#import plot_data
#import email_me 


serial_port='\.\COM5'
real_serial= False

'''
if(real_serial):
    import serial
    arduino = serial.Serial(serial_port, 9600,timeout=1.0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)    
else:
    import FakeArduino as serial
    arduino = serial.Serial(serial_port, 9600,timeout=1.0)
'''

class State(Enum):
    startup = 1
    shutdown = 2
    waiting = 3
    write = 4


    
def serial_state_machine_generic(state):
    # maybe some jobs here 
    while (state == 0):
        # do job/jobs until state changes
        # state is changed once jobs are complete e.g. by the movement finishing
        time.sleep(1)
        print("here")
        state = 1
       
    if (state == 0):
        # go to next state depending on the outcome of what happened e..g success or failure
        serial_state_machine_generic()
        pass
    elif(state == 1):
         serial_state_machine_generic_next(state)

    return 0

def serial_state_machine_generic_next(state):
    # maybe some jobs here 
    while (state == 1):
        # do job/jobs until state changes
        # state is changed once jobs are complete e.g. by the movement finishing
        state = 2
        time.sleep(1)
        print("there")
       
    if (state == 0):
        # go to next state depending on the outcome of what happened e..g success or failure
        pass
    elif(state == 2):
         # some other condition e.g. movement aborted
        return 0 


def serial_state_machine_startup():
    state = State.startup
    #ser = Serial()
    ser = object()
    jobs = []
    # do_startup
    while (state == State.startup):
        if (startup_successful()):
            state = State.waiting
        else:
            state = State.shutdown
        
    if (state == State.waiting):
        serial_state_machine_waiting(state,ser,jobs)
        
    elif(state == State.shutdown):
         serial_state_machine_shutdown(state,ser,jobs)   

def serial_state_machine_waiting(state,ser,jobs):
    # will wait in this state until it gets a command
    while (state == State.waiting):
        jobs = check_task_list(jobs)
        if (len(jobs)>0):
            state = State.write     
        if (is_finished()):
            state = State.shutdown
        
    if (state == State.write):
        serial_state_machine_write(state,ser,jobs)
        
    elif(state == State.shutdown):
         serial_state_machine_shutdown(state,ser,jobs)   
    return 0 

def serial_state_machine_write(state,ser,jobs):
    # will wait in this state until it gets a command
    job = jobs.pop(0)
    job_done = False
    while (state == State.write and not job_done):
        time.sleep(1)
        print(job)
        job_done = True
        # compile job into required format
        # send job over serial to robot arm
        # confirm job has been completed
    
    if(len(jobs) == 0 and is_finished()):
        state = State.shutdown
    elif(len(jobs) == 0 and not is_finished()):
        state = State.waiting
    elif (len(jobs)>0):
        serial_state_machine_write(state,ser,jobs)        


def serial_state_machine_shutdown(state,ser,jobs):
    #ser.close()
    return 0
    # maybe return arm to starting point 

def startup_successful():
    return True

def is_finished():
    global finished
    return finished

def check_task_list_broke(jobs):
    return jobs

def check_task_list(jobs):
    global new_jobs
    copy_new_jobs = new_jobs.copy()
    new_jobs = []
    jobs.extend(copy_new_jobs)
    return jobs


new_jobs = ['startup','move up', 'move left', 'move claw','play africa by toto']
finished = False
#serial_state_machine_generic(0)
serial_state_machine_startup()
time.sleep(3)
new_jobs = ['another job']
finished = True