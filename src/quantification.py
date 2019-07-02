#!/usr/bin/python
# circle_plate_charge.py
# Author: Jing Huang; Date: Apirl 14, 2016
# 
import math,sys,os,shutil
import header as header

def calculate_field(NAME,list,content,CHARGE_SEQ,CHARGE_SELECT,UNIT,XP,YP,ZP,VX,VY,VZ):
    """ calculate the field strength"""
    NO_CHA,COUNT,EFX,EFY,EFZ,OEF,X,Y,Z,Q,CHARGE_SEQ = initialize_electric_field(NAME,CHARGE_SELECT,CHARGE_SEQ)
    if CHARGE_SELECT == "PART":
        CHARGE_SEQ = convert_charge_seq(CHARGE_SEQ)
    f2 = open(NAME+".save", "w")
    for i in range(NO_CHA):
        X[i]  = content[i][0]  # X coordinate BOHR
        Y[i]  = content[i][1]  # Y coordinate BOHR
        Z[i]  = content[i][2]  # Z coordinate BOHR
        if i in CHARGE_SEQ:
            Q[i] = content[i][3]  # Charge
            print >> f2, (" %.10f     %.10f     %.10f     %.10f " %(X[i],Y[i],Z[i],Q[i]))
            COUNT = COUNT + 1
        else:
            Q[i] = 0.00
        if UNIT == "BOHR":
            (EFX1, EFY1, EFZ1) = eef_xyz_bohr(X[i],Y[i],Z[i],XP,YP,ZP,Q[i])
        elif UNIT == "ANS":
            (EFX1, EFY1, EFZ1) = eef_xyz_ans(X[i],Y[i],Z[i],XP,YP,ZP,Q[i])
        EFX = EFX + EFX1
        EFY = EFY + EFY1
        EFZ = EFZ + EFZ1
        OEF1 = projvU(VX,VY,VZ,EFX1,EFY1,EFZ1)
        OEF = OEF + OEF1
        i = i + 1
    f2.close()
    
    EFTOT = math.sqrt(EFX*EFX + EFY*EFY + EFZ*EFZ)
    return EFX,EFY,EFZ,OEF,EFTOT,NO_CHA,COUNT


def read_coordinates_and_charges(NAME):
    """ read coordinates and charges from .txt file to quantify local electric field """
    content=[]
    with open(NAME+".txt","r") as f:
        for line in f:
            content.append(list(map(float,line.split())))
            if not line.split():
                continue
    #   print(result[1][2])
    f.close()
    return content

def linecount1(NAME):
    count1 = 0
    count = len(open(NAME+".txt", "rU").readlines())
    with open(NAME+".txt","r") as f:
        for line in f:
            if not line.split():
                count1 = count1 + 1
    f.close()
    line1 = count - count1
    return line1

def eef_xyz_ans(X,Y,Z,X0,Y0,Z0,Q):
    # X,Y,Z,X0,Y0,Z0 -> ANGSTROM
    # CALCULATE THE VALUE OF ELECTRIC FIELD (EF) AT (X0, Y0, Z0)
    # THE X-COMPONENT OF EF IS "EEFX"
    # THE Y-COMPONENT OF EF IS "EEFY"
    # THE Z-COMPONENT OF EF IS "EEFZ"
    K = 1.00                 # THE COULOMB FORCE CONSTANT (A.U.)
    R = math.sqrt((X-X0)*(X-X0)+(Y-Y0)*(Y-Y0)+(Z-Z0)*(Z-Z0))
    R = R/0.529177249           # Bohr
    DX = (X-X0)/0.529177249     # Bohr
    DY = (Y-Y0)/0.529177249     # Bohr
    DZ = (Z-Z0)/0.529177249     # Bohr
    COSXT =  (-1.0)*DX/R
    COSYT =  (-1.0)*DY/R
    COSZT =  (-1.0)*DZ/R
    EEFX = (K*Q/(R**2))*COSXT
    EEFY = (K*Q/(R**2))*COSYT
    EEFZ = (K*Q/(R**2))*COSZT
    
    return (EEFX,EEFY,EEFZ)

def eef_xyz_bohr(X,Y,Z,X0,Y0,Z0,Q):
    # X,Y,Z,X0,Y0,Z0 -> BOHR
    # CALCULATE THE VALUE OF ELECTRIC FIELD (EF) AT (X0, Y0, Z0)
    # THE X-COMPONENT OF EF IS "EEFX"
    # THE Y-COMPONENT OF EF IS "EEFY"
    # THE Z-COMPONENT OF EF IS "EEFZ"
    K = 1.00                 # THE COULOMB FORCE CONSTANT (A.U.)
    R = math.sqrt((X-X0)*(X-X0)+(Y-Y0)*(Y-Y0)+(Z-Z0)*(Z-Z0))
    R = R           # Bohr
    DX = (X-X0)     # Bohr
    DY = (Y-Y0)     # Bohr
    DZ = (Z-Z0)     # Bohr
    COSXT =  (-1.0)*DX/R
    COSYT =  (-1.0)*DY/R
    COSZT =  (-1.0)*DZ/R
    EEFX = (K*Q/(R**2))*COSXT
    EEFY = (K*Q/(R**2))*COSYT
    EEFZ = (K*Q/(R**2))*COSZT
    
    return (EEFX,EEFY,EEFZ)

def projvU(XV,YV,ZV,XU,YU,ZU):
    #
    # VECTOR V -> (XV, YV, ZV);
    # VECTOR U -> (XU, YU, ZU);
    # THE FUNCTION PROJVU MEANS:
    #
    # THE VECTOR PROJECTION OF A NONZERO VECTOR U ON (OR ONTO) A NONZERO VECTOR V
    #
    VU = XV*XU + YV*YU + ZV*ZU
    MAGV = math.sqrt(XV*XV + YV*YV + ZV*ZV)
    PROJ = VU/MAGV
    return (PROJ)

def calculate_direction_vector(V1X, V1Y, V1Z, V2X, V2Y, V2Z):
    """ calculate the direction vector """
    VX = V2X - V1X
    VY = V2Y - V1Y
    VZ = V2Z - V1Z
    
    return VX,VY,VZ

def initialize_electric_field(NAME,CHARGE_SELECT,CHARGE_SEQ):
    """ initialize the electric field """
    COUNT = 0
    # NUMBER OF CHARGES
    NO_CHA = linecount1(NAME)
    list = range(NO_CHA)
    # INITIALIZE THE VALUE OF ELECTRIC FIELD
    EFX = 0.00
    EFY = 0.00
    EFZ = 0.00
    OEF = 0.00
    if (CHARGE_SELECT == "ALL"):
        CHARGE_SEQ = R(1,NO_CHA)
    X = range(NO_CHA)
    Y = range(NO_CHA)
    Z = range(NO_CHA)
    Q = range(NO_CHA)

    return NO_CHA,COUNT,EFX,EFY,EFZ,OEF,X,Y,Z,Q,CHARGE_SEQ

def convert_charge_seq(CHARGE_SEQ):
    "in case of CHARGE_SELECT = SELECT, the read-in CHARGE_SEQ-string has to be converted into a list, i.e. an actual selection"
    string = CHARGE_SEQ
    CHARGE_SEQ = []
    seq_list = string.split("+")
    seq_list2 = []
    for element in seq_list:
        seq_list2.append(element.split("("))
    for i in range(len(seq_list2)):
        if seq_list2[i][0] == "P":
            CHARGE_SEQ += P(int(seq_list2[i][1].strip(")")))
        if seq_list2[i][0] == "R":
            boundaries = seq_list2[i][1].split(",")
            left_boundary = int(boundaries[0])
            right_boundary = int(boundaries[1].strip(")"))
            CHARGE_SEQ += R(left_boundary,right_boundary)
    return CHARGE_SEQ

def R(i,j):
    """define range of charges to be read"""
    L = []
    L = range(i-1,j)
    return L

def P(i):
    """ define a single charge to be read"""
    L = [i-1]
    return L

def write_output_quant(UNIT,NAME,NO_CHA,EFX,EFY,EFZ,OEF,EFTOT,XP,YP,ZP,V1X,V1Y,V1Z,V2X,V2Y,V2Z,VX,VY,VZ,COUNT):
    """ write output of quant to .ef file """
    f1 = open(NAME+".ef", "w")
    header.header_output_file(f1)
    print >> f1, " "
    print >> f1, " "
    print >> f1, "-----------------------------------------------------------"
    print >> f1, " "
    print >> f1, "          ELECTRIC FIELD STRENGTH QUANTIFICATION"
    print >> f1, " "
    print >> f1, "-----------------------------------------------------------"
    print >> f1, " "
    print >> f1, " "
    if UNIT == "BOHR":
        print >> f1, " THE UNIT OF LENGTH IS BOHR"
    elif UNIT == "ANS":
        print >> f1, " THE UNIT OF LENGTH IS ANGSTROM"
    print >> f1, " "
    print >> f1, " "
    print >> f1, "-----------------------------------------------------------"
    print >> f1, " "
    print >> f1, "                      CHARGE DISTRIBUTION"
    print >> f1, " "
    print >> f1, "-----------------------------------------------------------"
    print >> f1, " "
    print >> f1, (" THE CHARGE DISTRIBUTION IS SHOWN IN THE FILE %s.txt. "%(NAME))
    print >> f1, " "
    print >> f1, (" THERE ARE %d POINT CHARGES IN THIS CHARGE DISTRIBUTION. "%(NO_CHA))
    print >> f1, " "
    print >> f1, (" %d POINT CHARGES ARE CONSIDERED IN THE ELECTRIC FIELD CALCULATION." %(COUNT))
    print >> f1, " "
    print >> f1, " "
    print >> f1, " "
    print >> f1, "-----------------------------------------------------------"
    print >> f1, " "
    print >> f1, "             THE STRENGTH OF THE ELECTRIC FIELD"
    print >> f1, " "
    print >> f1, "-----------------------------------------------------------"
    print >> f1, " "
    print >> f1, (" THE STRENGTH OF THE ELECTRIC FIELD AT POINT (%.10f, %.10f, %.10f) : " %(XP, YP, ZP))
    print >> f1, " "
    print >> f1, (" X-COMPONENT OF THE EF: %.10f  A.U.;"%(EFX))
    print >> f1, (" Y-COMPONENT OF THE EF: %.10f  A.U.;"%(EFY))
    print >> f1, (" Z-COMPONENT OF THE EF: %.10f  A.U.;"%(EFZ))
    print >> f1, (" TOTAL STRENGTH OF THE EF: %.10f  A.U.."%(EFTOT))
    print >> f1, (" ")
    print >> f1, (" ")
    print >> f1, (" ")
    print >> f1, "-----------------------------------------------------------"
    print >> f1, " "
    print >> f1, "  THE STRENGTH OF ELECTRIC FIELD ALONG DIRECTION VECTOR V"
    print >> f1, " "
    print >> f1, "-----------------------------------------------------------"
    print >> f1, " "
    print >> f1, " "
    print >> f1, (" THE DIRECTION VECTER  V  (%.10f,  %.10f,  %.10f), " %(VX,VY,VZ))
    print >> f1, (" DEFINED FROM POINT V1(%.10f,  %.10f,  %.10f)"%(V1X,V1Y,V1Z))
    print >> f1, (" TO V2(%.10f,  %.10f,  %.10f)"%(V2X,V2Y,V2Z))
    print >> f1, " "
    print >> f1, " "
    print >> f1, (" THE STRENGTH OF THE EF ORIENTED ALONG THE DIRECTION VECTOR V IS %.10f A.U." %(OEF))
    print >> f1, " "
    print >> f1, " "
    print >> f1, " THE ELECTRIC FIELD HAS SUCCESFULLY BEEN QUANTIFIED"
    print >> f1, " "
    print >> f1, " "
    header.conclusion_output_file(f1)
    f1.close()


