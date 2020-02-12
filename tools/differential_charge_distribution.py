#!/usr/bin/python

import numpy as np
import sys
import math

def header_command_line():
    print ("                                                                 ")
    print ("  ****************************************************************** ")
    print ("  *                                                                * ")
    print ("  *                    TITAN - VERSION 1.3                         * ")
    print ("  *                                                                * ")
    print ("  *           FROM THE HEBREW UNIVERSITY OF JERUSALEM              * ")
    print ("  *    THIJS STUYVER, JING HUANG, DIBYENDU MALLICK, SASON SHAIK    * ")
    print ("  *              J. COMPUT. CHEM. 41, 74-81 (2020)                 * ")
    print ("  *                                                                * ")
    print ("  ****************************************************************** ")
    print ("                                                                 ")
    print ("                                                                 ")
    print ("                  DIFFERENTIAL CHARGE DISTRIBUTION               ")
    print ("                                                                 ")


def differential_charge_distribution(filename1,filename2,output_filename):
    """ Determine and write the differential charge distribution from two charge distributions """
    header_command_line()

    X1,Y1,Z1,Q1,X2,Y2,Z2,Q2 = extract_charge_distributions(filename1,filename2)

    X_differential,Y_differential,Z_differential,Q_differential = X1[:],Y1[:],Z1[:],Q1[:]

    X_differential, Y_differential, Z_differential, Q_differential = append_differential(X1,Y1,Z1,Q1,X2,Y2,Z2,Q2,X_differential,Y_differential,Z_differential,Q_differential)

    try:
        write_output(X_differential, Y_differential, Z_differential, Q_differential, output_filename)
        print ("  ******************************************************************** ")
        print (" ")
        print (" THE DIFFERENTIAL CHARGE DISTRIBUTION HAS SUCCESSFULLY BEEN GENERATED ")
        print (" ")
        print ("  ******************************************************************** ")
    except:
        print ("  ****************************************************************** ")
        print (" ")
        print ("                            ERROR TERMINATION ")
        print (" ")
        print ("  ****************************************************************** ")



def append_differential(X1,Y1,Z1,Q1,X2,Y2,Z2,Q2,X_differential,Y_differential,Z_differential,Q_differential):
    """ Check whether points of the two charge distributions overlap; if so: subtract the corresponding Q2, if not: append new point """
    for point1 in range(len(Q2)):
        counter = 0
        #print point1
        for point2 in range(len(Q1)):
            counter += 1
            distance = determine_distance_between_two_points(X1[point2],Y1[point2],Z1[point2],X2[point1],Y2[point1],Z2[point1])
            if distance < 0.001:
                break
        if counter > 0 and counter < len(Q1)+1:
            #print counter
            Q_differential[counter-1] += -Q2[point1]
        else:
            X_differential, Y_differential, Z_differential, Q_differential = append_differential_distribution(X_differential,Y_differential,Z_differential,Q_differential,X2,Y2,Z2,Q2,point1)

    return X_differential, Y_differential, Z_differential, Q_differential

def append_differential_distribution(X_differential,Y_differential,Z_differential,Q_differential,X2,Y2,Z2,Q2,point1):
    """ Append the individual differential lists """
    X_differential.append(X2[point1])
    Y_differential.append(Y2[point1])
    Z_differential.append(Z2[point1])
    Q_differential.append(-Q2[point1])

    return X_differential,Y_differential,Z_differential,Q_differential

def extract_charge_distributions(filename1,filename2):
    """ Extract the charge distributions from the two input files """
    content1 = read_coordinates_and_charges(filename1)
    X1,Y1,Z1,Q1 = process_coordinates_and_charges(content1)

    content2 = read_coordinates_and_charges(filename2)
    X2,Y2,Z2,Q2 = process_coordinates_and_charges(content2)

    return X1,Y1,Z1,Q1,X2,Y2,Z2,Q2

def determine_distance_between_two_points(X1,Y1,Z1,X2,Y2,Z2):
    """ Determine the distance between two points """
    distance = math.sqrt((float(X1)-float(X2))**2+(float(Y1)-float(Y2))**2+(float(Z1)-float(Z2))**2)

    return distance

def process_coordinates_and_charges(content):
    """ Turn the content into separate coordinate and charge lists """
    number_of_points = len(content)
    X,Y,Z,Q = initialize(number_of_points)
    for point in range(number_of_points):
        X[point]  = content[point][0]
        Y[point]  = content[point][1]
        Z[point]  = content[point][2]
        Q[point]  = content[point][3]

    return X,Y,Z,Q

def initialize(number_of_points):
    """ Initialize coordinate and charge lists """
    X = range(number_of_points)
    Y = range(number_of_points)
    Z = range(number_of_points)
    Q = range(number_of_points)

    return X,Y,Z,Q

def read_coordinates_and_charges(NAME):
    """ read coordinates and charges from .txt file """
    content=[]
    with open(NAME,"r") as f:
        for line in f:
            content.append(list(map(float,line.split())))
            if not line.split():
                continue
    f.close()
    return content

def format_output(X_differential, Y_differential, Z_differential, Q_differential):
    """ Format the differential charge distribution """

    X_differential_aligned = align_numbers(X_differential)
    Y_differential_aligned = align_numbers(Y_differential)
    Z_differential_aligned = align_numbers(Z_differential)
    Q_differential_aligned = align_numbers(Q_differential)

    return X_differential_aligned, Y_differential_aligned, Z_differential_aligned, Q_differential_aligned

def write_output(X_differential, Y_differential, Z_differential, Q_differential,output_filename):
    """ Write the output """
    X_differential, Y_differential, Z_differential, Q_differential = format_output(X_differential, Y_differential, Z_differential, Q_differential)
    file = open(output_filename + '.txt','a')
    for point in range(len(X_differential)):
        file.write(' %s \t %s \t %s \t %s \n' % (X_differential[point], Y_differential[point], Z_differential[point], Q_differential[point]))
    file.close()

def align_numbers(list):
    """ Align all numbers nicely """
    list_aligned = []
    for number in list:
        if '-' in str(number):
            list_aligned.append(str(number))
        else:
            list_aligned.append(' ' + str(number))
    return list_aligned

# ----------------------------------------------------
# Main
if __name__ == '__main__':

    # Get Input
    if len(sys.argv[1:]) == 3:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
        output_filename = sys.argv[3]
        differential_charge_distribution(filename1,filename2,output_filename)
    else:
        print 'ERROR: Wrong input'
        print 'Usage:'
        print 'python differential_charge_distribution.py NAME1.txt NAME2.txt output'