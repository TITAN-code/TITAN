#!/usr/bin/python
# calc_EFF_ans.py
# Author: Jing Huang; Date: July 15, 2016
#
# A TOOL TO CALCULATE THE STRENGTH OF ELECTRIC FIELD 
# AT THE POINT (XP, YP, ZP) ORIENTED TO THE DIRECTION 
# VECTOR   V   FROM THE POINT (V1X, V1Y, V1Z) TO THE 
# POINT (V2X, V2Y, V2Z)
#
import math,sys

def header_command_line():
    print ("                                                                 ")
    print ("  ****************************************************************** ")
    print ("  *                                                                * ")
    print ("  *                    TITAN - VERSION 1.2                         * ")
    print ("  *                                                                * ")
    print ("  *           FROM THE HEBREW UNIVERISTY OF JERUSALEM              * ")
    print ("  *    THIJS STUYVER, JING HUANG, DIBYENDU MALLICK, SASON SHAIK    * ")
    print ("  *              J. COMPUT. CHEM. X, XXX-XXX (2019)                * ")
    print ("  *                                                                * ")
    print ("  ****************************************************************** ")
    print ("                                                                 ")
    print ("                                                                 ")
    print ("                     ANGSTROM TO BOHR CONVERSION                    ")
    print ("                                                                 ")

def read_input(NAME):
    result=[]
    with open(NAME,"r") as f:
        for line in f:
            result.append(list(map(float,line.split())))
            if not line.split():
                continue
    f.close()
    return result
#
# result[i][j] : i -> the (i+1) th charge
# X[i]  = result[i][0]  ANGSTROM 
# Y[i]  = result[i][1]  ANGSTROM 
# Z[i]  = result[i][2]  ANGSTROM 
# Q[i]  = result[i][3]  e-        a.u.
#
# THE NUMBERS OF THE LINES IN THE FILE
#
def linecount1(NAME):
    count1 = 0
    count = len(open(NAME, "rU").readlines())
    with open(NAME,"r") as f:
        for line in f:
            if not line.split():
                count1 = count1 + 1
    f.close()
    line1 = count - count1
    return line1

def convert(NAME):
    """ the main program """
    header_command_line()
    i = 0
    # NUMBER OF CHARGES
    result = read_input(NAME)
    NO_CHA = linecount1(NAME)
    list = range(NO_CHA)
    #
    X = range(NO_CHA)
    Y = range(NO_CHA)
    Z = range(NO_CHA)
    Q = range(NO_CHA)
    #
    f1 = open(NAME.strip(".txt")+"_bohr.txt", "w")
    for i in list:
    #
        X[i]  = result[i][0]/0.529177249  # X coordinate Bohr
        Y[i]  = result[i][1]/0.529177249  # Y coordinate Bohr
        Z[i]  = result[i][2]/0.529177249  # Z coordinate Bohr
        Q[i]  = result[i][3]  # Charge
        print >> f1, (" %.10f     %.10f     %.10f     %.10f " %(X[i],Y[i],Z[i],Q[i]))
    #
    print ("  ****************************************************************** ")
    print (" ")
    print ("      THE COORDINATE CONVERSION HAS BEEN COMPLETED SUCCESFULLY ")
    print (" ")
    print ("  ****************************************************************** ")


# ----------------------------------------------------
# Main
if __name__ == '__main__':
    
    # Get Input
    if len(sys.argv[1:]) == 1:
        filename = sys.argv[1]
        convert(filename)
    else:
        print 'ERROR: Wrong input'
        print 'Usage:'
        print 'python ans2bohr.py NAME.txt'

