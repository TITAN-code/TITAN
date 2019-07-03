#!/usr/bin/python
# calc_EFF_ans.py
# Author: Jing Huang; Date: July 15, 2016
#
# A TOOL TO CALCULATE THE STRENGTH OF ELECTRIC FIELD 
# AT THE POINT (XP, YP, ZP) ORIENTED TO THE DIRECTION 
# VECTOR   V   FROM THE POINT (V1X, V1Y, V1Z) TO THE 
# POINT (V2X, V2Y, V2Z)
#
import math
#
# Define the constant of EF calculation.
#
#--------------
#    INPUT
#--------------
#
NAME = "full"
#--------------
# END OF INPUT
#--------------
#
# READ COORDINATIONS AND CHARGES 
#
result=[]
with open(NAME+".txt","r") as f:
   for line in f:
      result.append(list(map(float,line.split())))
      if not line.split():
	   continue
#   print(result[1][2])
f.close()
#
# result[i][j] : i -> the (i+1) th charge
# X[i]  = result[i][0]  BOHR 
# Y[i]  = result[i][1]  BOHR 
# Z[i]  = result[i][2]  BOHR 
# Q[i]  = result[i][3]  e-        a.u.
#
# THE NUMBERS OF THE LINES IN THE FILE
#
def linecount1():
 count1 = 0
 count = len(open(NAME+".txt", "rU").readlines())
 with open(NAME+".txt","r") as f:
   for line in f:
      if not line.split():
       count1 = count1 + 1
 f.close()
 line1 = count - count1 
 return line1
#
#
# MAIN PORGRAM
#
i = 0
# NUMBER OF CHARGES
NO_CHA = linecount1()
list = range(NO_CHA)
#
X = range(NO_CHA)
Y = range(NO_CHA)
Z = range(NO_CHA)
Q = range(NO_CHA)
#
f1 = open(NAME+"_ans.txt", "w")
for i in list:
#
    X[i]  = result[i][0]*0.529177249  # X coordinate Bohr 
    Y[i]  = result[i][1]*0.529177249  # Y coordinate Bohr 
    Z[i]  = result[i][2]*0.529177249  # Z coordinate Bohr 
    Q[i]  = result[i][3]  # Charge
    print >> f1, (" %.10f     %.10f     %.10f     %.10f " %(X[i],Y[i],Z[i],Q[i]))
#
print " "
print "****************"
print " "
print "      Done"
print " "
print "****************"
print " "
print " "