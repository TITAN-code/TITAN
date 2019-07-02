#!/usr/bin/python
# circle_plate_charge.py
# Author: Jing Huang; Date: Apirl 14, 2016
# 

def determine_type(filename):
    """ determine type of calculation """
    with open(filename,'r') as f_obj:
        contents = f_obj.read()
        line_list = contents.split("\n")
    for line in line_list:
        line_content = line.split(" ")
        if line_content[0] == "TYPE":
            TYPE = str(line_content[2])

    return TYPE

def read_input_cpc(filename):
    """ read parameters for cpc calculation """
    with open(filename,'r') as f_obj:
        contents = f_obj.read()
        line_list = contents.split("\n")
    for line in line_list:
        line_content = line.split(" ")
        if line_content[0] == "R":
            R = float(line_content[2])
        if line_content[0] == "N":
            N = int(line_content[2])
        if line_content[0] == "DIS":
            DIS = float(line_content[2])
        if line_content[0] == "FIELD":
            FIELD = float(line_content[2])
        if line_content[0] == "NAME":
            NAME = str(line_content[2])
        if line_content[0] == "OUTFORMAT":
            OUTFORMAT = str(line_content[2])
        if line_content[0] == "POINT1_X":
            POINT1_X = float(line_content[2])
        if line_content[0] == "POINT1_Y":
            POINT1_Y = float(line_content[2])
        if line_content[0] == "POINT1_Z":
            POINT1_Z = float(line_content[2])
        if line_content[0] == "POINT2_X":
            POINT2_X = float(line_content[2])
        if line_content[0] == "POINT2_Y":
            POINT2_Y = float(line_content[2])
        if line_content[0] == "POINT2_Z":
            POINT2_Z = float(line_content[2])

    return POINT1_X,POINT1_Y,POINT1_Z,POINT2_X,POINT2_Y,POINT2_Z,R,N,DIS,FIELD,NAME,OUTFORMAT

def read_input_sl(filename):
    """ read parameters for SL calculation. """
    with open(filename,'r') as f_obj:
        contents = f_obj.read()
        line_list = contents.split("\n")
    for line in line_list:
        line_content = line.split(" ")
        if line_content[0] == "RADIUS":
            RADIUS = float(line_content[2])
        if line_content[0] == "N":
            N = float(line_content[2])
        if line_content[0] == "STEP":
            STEP = float(line_content[2])
        if line_content[0] == "CHIRALITY":
            CHIRALITY = str(line_content[2])
        if line_content[0] == "NAME":
            NAME = str(line_content[2])
        if line_content[0] == "CHARGETYPE":
            CHARGETYPE = str(line_content[2])
            if CHARGETYPE == "DNA":
                FATOM = 7
                CHARGE = 0.0
        if line_content[0] == "FATOM":
            FATOM = int(line_content[2])
        if line_content[0] == "SEQUENCE":
            SEQUENCE = str(line_content[2])
        if line_content[0] == "CHARGE":
            CHARGE = float(line_content[2])
        if line_content[0] == "XP":
            XP = float(line_content[2])
        if line_content[0] == "YP":
            YP = float(line_content[2])
        if line_content[0] == "ZP":
            ZP = float(line_content[2])

    return RADIUS,N,STEP,CHIRALITY,NAME,CHARGETYPE,FATOM,SEQUENCE,CHARGE,XP,YP,ZP

def read_input_quantification(filename):
    """ read parameters for EF quantification """
    with open(filename,'r') as f_obj:
        contents = f_obj.read()
        line_list = contents.split("\n")
    for line in line_list:
        line_content = line.split(" ")
        if line_content[0] == "UNIT":
            UNIT = str(line_content[2])
        if line_content[0] == "FILE":
            FILE = str(line_content[2])
        if line_content[0] == "NAME":
            NAME = str(line_content[2])
        if line_content[0] == "CHARGE_SELECT":
            CHARGE_SELECT = str(line_content[2])
        if line_content[0] == "CHARGE_SEQ":
            CHARGE_SEQ = line_content[2]
        if line_content[0] == "DIRECTION":
            DIRECTION = line_content[2]

    return UNIT, FILE, NAME, CHARGE_SELECT, CHARGE_SEQ, DIRECTION

def read_input_quantification_manual(filename):
    """ in case DIRECTION = MANUAL was selected, the direction vector parameters have to be read """
    with open(filename,'r') as f_obj:
        contents = f_obj.read()
        line_list = contents.split("\n")
    for line in line_list:
        line_content = line.split(" ")
        if line_content[0] == "V1X":
            V1X = float(line_content[2])
        if line_content[0] == "V1Y":
            V1Y = float(line_content[2])
        if line_content[0] == "V1Z":
            V1Z = float(line_content[2])
        if line_content[0] == "V2X":
            V2X = float(line_content[2])
        if line_content[0] == "V2Y":
            V2Y = float(line_content[2])
        if line_content[0] == "V2Z":
            V2Z = float(line_content[2])
        if line_content[0] == "XP":
            XP = float(line_content[2])
        if line_content[0] == "YP":
            YP = float(line_content[2])
        if line_content[0] == "ZP":
            ZP = float(line_content[2])

    return V1X, V1Y, V1Z, V2X, V2Y, V2Z, XP, YP, ZP

def read_input_quantification_select(filename):
    """ in case DIRECTION = SELECT was selected, the coordination file and atom numbers determining the direction vector parameters have to be read """
    with open(filename,'r') as f_obj:
        contents = f_obj.read()
        line_list = contents.split("\n")
    for line in line_list:
        line_content = line.split(" ")
        if line_content[0] == "DIRECTION_FILE":
            DIRECTION_FILE = str(line_content[2])
        if line_content[0] == "ATOM1":
            ATOM1 = int(line_content[2])
        if line_content[0] == "ATOM2":
            ATOM2 = int(line_content[2])
        if line_content[0] == "ATOM_CENTER":
            ATOM_CENTER = int(line_content[2])

    return DIRECTION_FILE,ATOM1,ATOM2,ATOM_CENTER

def read_input_pdb(filename):
    """ read the additional parameters in case the starting point for EF quantification is a .pdb file """
    with open(filename,'r') as f_obj:
        contents = f_obj.read()
        line_list = contents.split("\n")
    for line in line_list:
        line_content = line.split(" ")
        if line_content[0] == "NAME_CHARGE_DISTRIBUTION":
            NAME_CHARGE_DISTRIBUTION = str(line_content[2])
        if line_content[0] == "FORCE":
            FORCE = str(line_content[2])
        if line_content[0] == "N_TERMINAL":
            N_TERMINAL = [int(line_content[2])]
        if line_content[0] == "C_TERMINAL":
            C_TERMINAL = [int(line_content[2])]

    return NAME_CHARGE_DISTRIBUTION,FORCE,N_TERMINAL,C_TERMINAL

def read_input_charmm(filename):
    """ read the additional parameters in case the selected force field for the charge distribution to be extracted from the .pdb file is CHARMM """
    with open(filename,'r') as f_obj:
        contents = f_obj.read()
        line_list = contents.split("\n")
    for line in line_list:
        line_content = line.split(" ")
        if line_content[0] == "ASPP":
            try:
                ASPP = line_content[2].split(",")
            except:
                ASPP = []
        if line_content[0] == "GLUP":
            try:
                GLUP = line_content[2].split(",")
            except:
                GLUP = []
        if line_content[0] == "DISU":
            try:
                DISU = line_content[2].split(",")
            except:
                DISU = []

    return ASPP,GLUP,DISU
