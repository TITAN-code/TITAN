#!/usr/bin/python
# circle_plate_charge.py
# Author: Jing Huang; Date: Apirl 14, 2016
#
import library_amber as lib_amb
import processing as processing

def linecount1(NAME):
    count1 = 0
    count = len(open(NAME+".pdb", "rU").readlines())
    with open(NAME+".pdb","r") as f:
        for line in f:
            if not line.split():
                count1 = count1 + 1
    f.close()
    line1 = count - count1
    return line1

def typeread(x):
    y = x
    return y

def read_pdb(NAME):
    """ read and store the content of the .pdb file """
    pdb_contents = []
    with open(NAME+".pdb","r") as file_pdb:
        for line in file_pdb:
            pdb_contents.append(list(map(typeread,line.split('\n'))))
            if not line.split():
                continue
    file_pdb.close()

    return pdb_contents

def initialize_operation_amber(NAME):
    """ Initialize all lists and parameters for the charge distribution generation """
    NO_CHA = linecount1(NAME)
    list_pdb = range(NO_CHA)
    T1 = range(NO_CHA)
    ATOM_N = range(NO_CHA)
    ATOM_T = range(NO_CHA)
    CHAIN_T = range(NO_CHA)
    RESI_T = range(NO_CHA)
    RESI_N = range(NO_CHA)
    X = range(NO_CHA)
    Y = range(NO_CHA)
    Z = range(NO_CHA)
    Q = range(NO_CHA)
    CHARGE = 0.00

    return NO_CHA,list_pdb,T1,ATOM_N,ATOM_T,CHAIN_T,RESI_T,RESI_N,X,Y,Z,Q,CHARGE

def write_charge_distribution(NAME_CHARGE_DISTRIBUTION,list_pdb,T1,X,Y,Z,Q):
    """ write the obtained charge distribution to a .txt output-file """
    f1 = open(NAME_CHARGE_DISTRIBUTION+".txt", "w")
    for i in list_pdb:
        if (T1[i] == "ATOM"):
            print >> f1, ("%14.10f  %14.10f  %14.10f  %14.10f " %(X[i],Y[i],Z[i],Q[i]))
    f1.close()

def charge_distribution_generation_amber(NAME,NAME_CHARGE_DISTRIBUTION,N_TERMINAL,C_TERMINAL):
    """ Generate the charge distribution according the amber force field """
    pdb_contents = read_pdb(NAME)
    NO_CHA,list_pdb,T1,ATOM_N,ATOM_T,CHAIN_T,RESI_T,RESI_N,X,Y,Z,Q,CHARGE = initialize_operation_amber(NAME)
    list_amino = ["ALA","ARG","ASN","ASP","CYS","CYX","GLN","GLU","GLY","HID","HIE","HIP","ILE","LEU","LYS","MET","PHE","PRO","SER","THR","TRP","TYR" ,"VAL"]
    for i in list_pdb:
        RESULT = pdb_contents[i][0]
        T1[i] = RESULT[0:4]
        if (T1[i] == "ATOM"):
            ATOMN = RESULT[6:11]
            ATOMT = RESULT[12:16]
            CHAINT = RESULT[16:17]
            RESIT = RESULT[17:21]
            RESIN = RESULT[22:27]
            X1 = RESULT[29:38]
            Y1 = RESULT[38:46]
            Z1 = RESULT[46:54]
            #
            ATOM_N[i] = int(ATOMN.strip())
            ATOM_T[i] = ATOMT.strip()
            CHAIN_T[i] = CHAINT.strip()
            RESI_T[i] = RESIT.strip()
            RESI_N[i] = int(RESIN.strip())
            X[i] = float(X1.strip())
            Y[i] = float(Y1.strip())
            Z[i] = float(Z1.strip())
            if (RESI_T[i] in list_amino):
                if (RESI_N[i] in N_TERMINAL):
                    RESI_T[i] =  "N" + RESI_T[i]
                    Q[i] = lib_amb.N_terminal_charge(ATOM_T[i],RESI_T[i])
                elif (RESI_N[i] in C_TERMINAL):
                    RESI_T[i] = "C" + RESI_T[i]
                    Q[i] = lib_amb.C_terminal_charge(ATOM_T[i],RESI_T[i])
                else:
                    Q[i] = lib_amb.amber_charge_resid(ATOM_T[i],RESI_T[i])
            else:
                Q[i] = lib_amb.amber_charge_resid(ATOM_T[i],RESI_T[i])
                CHARGE = CHARGE + Q[i]

    write_charge_distribution(NAME_CHARGE_DISTRIBUTION,list_pdb,T1,X,Y,Z,Q)
    processing.write_command_line_amber(NAME,NAME_CHARGE_DISTRIBUTION,CHARGE)

