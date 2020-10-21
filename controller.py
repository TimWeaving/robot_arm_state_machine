# -*- coding: utf-8 -*-
'''
Created on Sat Oct 17 17:25:21 2020

@author: evans
'''

import time
import state_machine2


new_jobs = ['move up', 'move left', 'move claw','play africa by toto']

joint_list = []
for  x in range(7):
    joint_list.append( state_machine2.joint(x))


def right(joint_list):
    is_ready = False
    while(is_ready):
        is_ready = True
        for joint in joint_list:
            if(not joint.is_ready()):
                is_ready = False

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

    joint_movement=[(0,100),(3,200),(6,60)]
    for instruction in joint_movement:
        joint = instruction[0]
        movement = instruction[1]
        joint_list[joint].update_jobs([movement])
    print()


def africa_for_toto():
    pass


left(joint_list)

left(joint_list)

right(joint_list)

time.sleep(4)
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