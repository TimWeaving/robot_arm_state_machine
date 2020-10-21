# -*- coding: utf-8 -*-
'''
Created on Sat Oct 17 17:25:21 2020

@author: evans
'''

import time
import state_machine2

def right(joint_list):
    is_ready = False
    while(is_ready):
        is_ready = True
        for joint in joint_list:
            if(not joint.is_ready()):
                is_ready = False
    print("Right")
    joint_movement=[(3,1000),(3,800),(6,600),(1,600)]
    for instruction in joint_movement:
        joint = instruction[0]
        movement = instruction[1]
        joint_list[joint].update_jobs([movement])
    print()

def left(joint_list):
    is_ready = False
    while(is_ready):
        is_ready = True
        for joint in joint_list:
            if(not joint.is_ready()):
                is_ready = False
    print("Left")
    joint_movement=[(0,100),(3,200),(6,60)]
    for instruction in joint_movement:
        joint = instruction[0]
        movement = instruction[1]
        joint_list[joint].update_jobs([movement])


def africa_by_toto(joint_list):
    left(joint_list)
    time.sleep(2) # should work without these??
    left(joint_list)
    time.sleep(2) # should work without these???
    right(joint_list)
    time.sleep(2)

if __name__ == '__main__':
    #joint_movement=[(3,1000),(3,800),(6,600),(1,600)] example instruction list
    joint_list = []
    for  x in range(7):
        joint_list.append( state_machine2.joint(x))

    africa_by_toto(joint_list)


    for  joint in joint_list:
        joint.set_finished()




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