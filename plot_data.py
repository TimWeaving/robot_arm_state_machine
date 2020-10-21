# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 22:11:40 2019

@author: evans
"""
import matplotlib.pyplot as plt
import csv

def write_file(title,data,filename):
    with open('data.csv', 'w', newline='') as csvfile:
        w = csv.writer(csvfile, delimiter=',',quotechar=',', quoting=csv.QUOTE_MINIMAL)
        w.writerow(title)
        for line in (data):
            w.writerow(line)
 
def plot_data(data):
    T, temperture,humidity = zip(*data)
    fig = plt.figure(figsize=(20,10))
    ax1 = fig.add_subplot(1,1,1)


    ax1.plot(T, temperture)
    ax1.plot(T, humidity)



def read_file(file):
    temperture=[]
    humidity=[]
    T=[]
    with open(file, "rt") as csvfile:
        csv_reader=csv.reader(csvfile, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if  not line_count:
                #print(f'Column names are {", ".join(row)}')
                t=", ".join(row)
                print (t)
                line_count += 1
            else:
                T.append(row[0])
                temperture.append([row[1]])
                humidity.append(row[2])
                #print(f'\t{row[0]} {row[1]} {row[2]}')
                line_count += 1
        print(f'Processed {line_count} lines.')
    return (T,temperture,humidity)