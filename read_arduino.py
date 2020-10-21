
from datetime import datetime
import time
import numpy as np 
from enum import Enum

#import plot_data
#import email_me 


serial_port='\.\COM5'
real_serial=0


if(real_serial):
    import serial
    arduino = serial.Serial(serial_port, 9600,timeout=1.0, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)    
else:
    import FakeArduino as serial
    arduino = serial.Serial(serial_port, 9600,timeout=1.0)


class State(Enum):
    startup = 1
    shutdown = 2
    waiting = 3
    write = 4

new_jobs = ['move up', 'move left', 'move claw','play africa by toto']
    
def serial_state_machine_generic():
    # maybe some jobs here 
    state = 0
    while (state == 0):
        # do job/jobs until state changes
        # state is changed once jobs are complete e.g. by the movement finishing
        state = 1
        
       
    if (state == 0):
        # go to next state depending on the outcome of what happened e..g success or failure
        pass
    elif(state == 1):
         # some other condition e.g. movement aborted
        pass
    pass



def serial_state_machine_startup():
    ser = serial()
    state = State()
    jobs = []
    # do_startup
    while (state == State.startup):
        if (startup_successful()):
            state = State.waiting()
        else:
            state = state.shutdown
        print("i'm here startup")
        
    if (state == State.waiting):
        serial_state_machine_waiting(state,ser,jobs)
        
    elif(state == State.shutdown()):
         serial_state_machine_shutdown(state,ser,jobs)   

def serial_state_machine_waiting(state,ser,jobs):
    # will wait in this state until it gets a command
    while (state == State.waiting):
        jobs = check_task_list()
        if (len(jobs)>0):
            state = state.write        
        
    if (state == State.write):
        serial_state_machine_waiting(ser)
        
    elif(state == State.shutdown()):
         serial_state_machine_shutdown()   
    return 0 

def serial_state_machine_write(state,ser,jobs):
    # will wait in this state until it gets a command
    job = jobs.pop(0)
    while (state == State.write):
        # compile job into required format
        # send job over serial to robot arm
        # confirm job has been completed
        time.sleep(0.5)
        print(job)
        job_done = True
        if(len(jobs) == 0 and job_done == True):
            state = State.waiting
        
    if (state == State.write):
        serial_state_machine_waiting(ser)
        
    elif(state == State.shutdown()):
         serial_state_machine_shutdown()   

def serial_state_machine_shutdown(state,ser,jobs):
    ser.close()
    # maybe return arm to starting point 

def startup_successful():
    return True

def check_task_list(jobs):
    global new_jobs
    return jobs.extend(new_jobs)


