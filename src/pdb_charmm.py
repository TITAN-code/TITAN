#!/usr/bin/python

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

def convert_atom_seq(ATOM_SEQ):
    "in case of ATOM_SELECT = PART, the read-in ATOM_SEQ-string has to be converted into a list, i.e. an actual selection"
    string = ATOM_SEQ
    ATOM_SEQ = []
    seq_list = string.split("+")
    seq_list2 = []
    for element in seq_list:
        seq_list2.append(element.split("("))
    for i in range(len(seq_list2)):
        if seq_list2[i][0] == "P":
            ATOM_SEQ += P(int(seq_list2[i][1].strip(")")))
        if seq_list2[i][0] == "R":
            boundaries = seq_list2[i][1].split(",")
            left_boundary = int(boundaries[0])
            right_boundary = int(boundaries[1].strip(")"))
            ATOM_SEQ += R(left_boundary,right_boundary)
    return ATOM_SEQ

def R(i,j):
    """define range of atoms to be read"""
    L = []
    L = range(i,j+1)
    return L

def P(i):
    """ define a single atom to be read"""
    L = [i]
    return L

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
    try:
        for item in range(len(residue_list)):
            residue_list[item] = int(residue_list[item])
    except:
        pass
    return residue_list

def write_charge_distribution(NAME,NAME_CHARGE_DISTRIBUTION,list_pdb,ATOM_SELECT,ATOM_SEQ,ATOM_N,ATOM_T,RESI_N,RESI_T,T1,X,Y,Z,Q):
    """ write the obtained charge distribution to a .txt output-file """
    f1 = open(NAME_CHARGE_DISTRIBUTION+".txt", "w")
    f2 = open(NAME+"_sequence"+".save", "w")
    if ATOM_SELECT == "ALL":
        for i in list_pdb:
            if (T1[i] == "ATOM"):
                print >> f1, ("%14.10f  %14.10f  %14.10f  %14.10f " %(X[i],Y[i],Z[i],Q[i]))
                print >> f2, ("%s  %s %s  %s %14.10f  %14.10f  %14.10f  %14.10f " %(ATOM_N[i],ATOM_T[i],RESI_N[i],RESI_T[i],X[i],Y[i],Z[i],Q[i]))
    elif ATOM_SELECT == "PART":
        for i in list_pdb:
            if (ATOM_N[i] in ATOM_SEQ):
                if (T1[i] == "ATOM"):
                    print >> f1, ("%14.10f  %14.10f  %14.10f  %14.10f " %(X[i],Y[i],Z[i],Q[i]))
                    print >> f2, ("%s  %s %s  %s %14.10f  %14.10f  %14.10f  %14.10f " %(ATOM_N[i],ATOM_T[i],RESI_N[i],RESI_T[i],X[i],Y[i],Z[i],Q[i]))
    f1.close()
    f2.close()

def charge_distribution_generation_charmm(NAME,NAME_CHARGE_DISTRIBUTION,ATOM_SELECT,ATOM_SEQ,N_TERMINAL,C_TERMINAL,ASPP,GLUP,DISU):
    """ Generate the charge distribution according the amber force field """
    pdb_contents = read_pdb(NAME)
    # Change strings to integers in the residue lists
    ASPP = convert_residue_list(ASPP)
    GLUP = convert_residue_list(GLUP)
    DISU = convert_residue_list(DISU)
    NO_CHA,list_pdb,T1,ATOM_N,ATOM_T,CHAIN_T,RESI_T,RESI_N,X,Y,Z,Q,CHARGE = initialize_operation_charmm(NAME)
    if ATOM_SELECT == "PART":
        ATOM_SEQ = convert_atom_seq(ATOM_SEQ)
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

    write_charge_distribution(NAME,NAME_CHARGE_DISTRIBUTION,list_pdb,ATOM_SELECT,ATOM_SEQ,ATOM_N,ATOM_T,RESI_N,RESI_T,T1,X,Y,Z,Q)
    processing.write_command_line_amber(NAME,NAME_CHARGE_DISTRIBUTION,CHARGE)

