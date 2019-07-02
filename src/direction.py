#!/usr/bin/python
# circle_plate_charge.py
# Author: Jing Huang; Date: Apirl 14, 2016

import math

def typeread(x):
    y = x
    return y

def determine_direction(DIRECTION_FILE,ATOM1,ATOM2,ATOM_CENTER):
    """ Determine direction from atom positions in DIRECTION_FILE """
    content_list = read_direction_file(DIRECTION_FILE)
    for i in range(len(content_list)):
        if (i == ATOM1-1):
            V1X = float(content_list[i][1])
            V1Y = float(content_list[i][2])
            V1Z = float(content_list[i][3])
        elif (i == ATOM2-1):
            V2X = float(content_list[i][1])
            V2Y = float(content_list[i][2])
            V2Z = float(content_list[i][3])
        else:
            pass
        if (i == ATOM_CENTER-1):
            XP = float(content_list[i][1])
            YP = float(content_list[i][2])
            ZP = float(content_list[i][3])
        else:
            pass

    return V1X, V1Y, V1Z, V2X, V2Y, V2Z, XP, YP, ZP

def read_direction_file(DIRECTION_FILE):
    """ Read the DIRECTION_FILE """
    content_list = []
    with open(DIRECTION_FILE + ".txt","r") as file_point:
        for line in file_point:
            content_list.append(list(map(typeread,line.split())))
            if not line.split():
                continue
    file_point.close()

    return content_list
