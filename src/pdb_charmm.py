#!/usr/bin/python
# circle_plate_charge.py
# Author: Jing Huang; Date: Apirl 14, 2016
#
import library_charmm as lib_charmm
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

def initialize_operation_charmm(NAME):
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

def convert_residue_list(residue_list):
    """ Convert strings in residue list to integers """
    for item in range(len(residue_list)):
        residue_list[item] = int(residue_list[item])
    return residue_list

def write_charge_distribution(NAME_CHARGE_DISTRIBUTION,list_pdb,T1,X,Y,Z,Q):
    """ Write the obtained charge distribution to a .txt output-file """
    f1 = open(NAME_CHARGE_DISTRIBUTION+".txt", "w")
    for i in list_pdb:
        if (T1[i] == "ATOM"):
            print >> f1, ("%14.10f  %14.10f  %14.10f  %14.10f " %(X[i],Y[i],Z[i],Q[i]))
    f1.close()

def charge_distribution_generation_charmm(NAME,NAME_CHARGE_DISTRIBUTION,N_TERMINAL,C_TERMINAL,ASPP,GLUP,DISU):
    """ Generate the charge distribution according the amber force field """
    pdb_contents = read_pdb(NAME)
    # Change strings to integers in the residue lists
    ASPP = convert_residue_list(ASPP)
    GLUP = convert_residue_list(GLUP)
    DISU = convert_residue_list(DISU)
    NO_CHA,list_pdb,T1,ATOM_N,ATOM_T,CHAIN_T,RESI_T,RESI_N,X,Y,Z,Q,CHARGE = initialize_operation_charmm(NAME)
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
                    RESI_T[i] =  RESI_T[i] + "N"
                    Q[i] = lib_charmm.N_terminal_charge(ATOM_T[i],RESI_T[i])
                elif (RESI_N[i] in C_TERMINAL):
                    RESI_T[i] = RESI_T[i] + "C"
                    Q[i] = lib_charmm.C_terminal_charge(ATOM_T[i],RESI_T[i])
                elif (RESI_T[i] == "ASP" and (RESI_N[i] in ASPP)):
                    RESI_T[i] = "ASPP"
                    Q[i] = lib_charmm.charmm_charge_resid(ATOM_T[i],RESI_T[i])
                elif (RESI_T[i] == "GLU" and (RESI_N[i] in GLUP)):
                    RESI_T[i] = "GLUP"
                    Q[i] = lib_charmm.charmm_charge_resid(ATOM_T[i],RESI_T[i])
                elif (RESI_T[i] == "CYS" and (RESI_N[i] in DISU)):
                    RESI_T[i] = "DISU"
                    Q[i] = lib_charmm.charmm_charge_resid(ATOM_T[i],RESI_T[i])
                else:
                    Q[i] = lib_charmm.charmm_charge_resid(ATOM_T[i],RESI_T[i])
            else:
                Q[i] = lib_charmm.charmm_charge_resid(ATOM_T[i],RESI_T[i])
                CHARGE = CHARGE + Q[i]

    write_charge_distribution(NAME_CHARGE_DISTRIBUTION,list_pdb,T1,X,Y,Z,Q)
    processing.write_command_line_amber(NAME,NAME_CHARGE_DISTRIBUTION,CHARGE)

