#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Mukhamad Suhermanto

Evaluating Raccoon's life
This assignment enables students to interact, process, and manipulate a txt file. 
Taking a txt file as an input, process it as necessary, and yield an output in the form of txt file as well.


@author: msuherma@purdue.edu
"""
#importing necessary modules
import math
import numpy as np

#Part 1: Reading ASCII file
fin = open ("2008Male00006.txt", "r")  # arg1 = name of the file, arg2= read only ("r")
lines = fin.readlines()                #lines is used as variable
print(lines)
fin.close()                            #to close the file

headers=lines[0].strip().split(",") # making the headers stripped, from 1st line (lines[0])

#Part 2. Create a list to store the data
n_line=len(lines)
values=[]
for line in lines[1:n_line]:
    '''
    This loop is to create the values to be listed into the dictionary;
    except the last line (-1), since it convey the last status of the animal.
    The status of the animal is stored without separating symbol
    '''
    if line.find(",") != -1:
        values.append([n_line for n_line in line.strip().split(",")])
    else:
        status = line.strip()

#Part 3: Creating the dictionary containing the header as the keys and values for the contents
keys_vals = {} #creating blank
for i in range(len(headers)):
    '''
    This loop is to create the headers(keys) and values stored in dictionary
    '''
    keys_vals[headers[i].strip()] = [row[i] for row in values]
    
## This part contains the mathematical calculation needed for this assignment

# Mean/average of list
def list_mean(l):
    listmean = list_sum(l)/len(l)
    return listmean
    
# Cumulative sum of list
def list_sum(l):
    listsum = 0
    for i in range(len(l)):
        listsum = listsum + float(l[i])
    return listsum

# Distance between two points provided as two lists
def distance_calc(l1,l2):
    # 1-D array for distance with initial value = 0
    dist=[0]*len(l1)
    for i in range(1,len(l1)):
        l1[i] = float(l1[i])
        l1[i-1] = float(l1[i-1])
        l2[i] = float(l2[i])
        l2[i-1] = float(l2[i-1])
        dist[i] = math.sqrt((l1[i]-l1[i-1])**2+(l2[i]-l2[i-1])**2)
    return dist
## end of the mathematical calculation functions

#Part 4: list to store the distances and add it to dictionary
Distance = {}
Distance['Distance'] = distance_calc(keys_vals['X'],keys_vals['Y'])
keys_vals = dict(keys_vals, **Distance)

## Parts below are to create new text file containing all required output

#Part 5: calculating distance and cumulative sum based on function defined        
keys_vals['Distance'] = [0] + distance_calc(keys_vals['X'],keys_vals['Y'])
keys_vals['Distance traveled'] = list_sum(keys_vals['Distance'])

#Part 6: writing a new text file with updated info on racoon's life time data and selected data from initial files
fw = open("Georges_life.txt","w")

fw.write('Raccoon name: ' + headers[3]+ str(keys_vals['George #'][0]) + '\n') # to print name of Raccoon and Number
fw.write('Average Location: X=' + str(list_mean(keys_vals['X'])) + ',Y=' + str(list_mean(keys_vals['Y'])) + '\n')
fw.write('Distance traveled: '+ str(sum(keys_vals['Distance'])) + '\n')
fw.write('Average energy level: ' + str(list_mean(keys_vals['Energy Level'])) + '\n')
fw.write('Raccoon end state: ' + lines[-1] + '\r\n')
sep = '\t' # set seperator type (comma, tab, space, etc)
fw.write('Date'+sep+'Time'+sep+'X'+sep+'Y'+sep+'Asleep'+sep+'Behavior Mode'+sep+'Distance traveled'+'\n') #creating the headers
new_values=[]
for i in range(len(values)):
    new_values.append(keys_vals['Day'][i] + "\t" + keys_vals['Time'][i] + "\t" +
                    str(keys_vals['X'][i]) + "\t" + str(keys_vals['Y'][i]) +
                    "\t" + keys_vals['Asleep'][i] + "\t"+ keys_vals['Behavior Mode'][i]
                    + "\t" + str(keys_vals['Distance'][i]) + "\n")
fw.writelines(new_values) #this is to add the new values after the header
