# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 18:53:46 2018

@author: evans
"""

import csv


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
                t.append([row[0]])
                T.append(row[1])
                H.append(row[2])
                #print(f'\t{row[0]} {row[1]} {row[2]}')
                line_count += 1
        print(f'Processed {line_count} lines.')

def write_file(title,data,filename):
    csv.register_dialect('myDialect',
    quoting=csv.QUOTE_ALL,
    skipinitialspace=True)
    with open(filename, 'w') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(title)
        for row in data:
            writer.writerow(data)
    f.close()
    #'person1.csv'