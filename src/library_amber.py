#!/usr/bin/python

import sys
import datetime

def library_warning_message():
    """ Message shown in the terminal in case the assignment of a point charge to an atom was not succesfull """
    print ("AN ERROR HAS OCCURED!")
    print (" ")
    print ("PLEASE CONFIRM THE CORRECT ASSIGNMENT OF N_TERMINAL & C_TERMINAL IN THE INPUT FILE")
    print (" ")
    print ("OTHERWISE:")
    print (" ")
    print ("THE ERROR IS MOST LIKELY DUE TO THE PRESENCE OF NON-STANDARD RESIDUES IN THE .pdb-FILE.")
    print ("CONSIDER COMPILING AN ALTERNATIVE AMBER-LIBRARY WITH THE NON-STANDARD RESIDUES INCLUDED.")
    print (" ")
    print (" ----- ERROR TERMINATION OF TITAN AT " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " -----")
    sys.exit()

def amber_charge_resid(ATOM_NAME,RES_NAME):
 if (RES_NAME == "ALA"): 
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =   0.0337 
   elif (ATOM_NAME == "HA"):
     charge =   0.0823 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1825 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0603 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0603 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0603 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ARG"):
   if (ATOM_NAME == "N"):
     charge =  -0.3479 
   elif (ATOM_NAME == "H"):
     charge =   0.2747 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2637 
   elif (ATOM_NAME == "HA"):
     charge =   0.1560 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0007 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0327 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0327 
   elif (ATOM_NAME == "CG"):
     charge =   0.0390 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0285 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0285 
   elif (ATOM_NAME == "CD"):
     charge =   0.0486 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0687 
   elif (ATOM_NAME == "HD3"):
     charge =   0.0687 
   elif (ATOM_NAME == "NE"):
     charge =  -0.5295 
   elif (ATOM_NAME == "HE"):
     charge =   0.3456 
   elif (ATOM_NAME == "CZ"):
     charge =   0.8076 
   elif (ATOM_NAME == "NH1"):
     charge =  -0.8627 
   elif (ATOM_NAME == "HH11"):
     charge =   0.4478 
   elif (ATOM_NAME == "HH12"):
     charge =   0.4478 
   elif (ATOM_NAME == "NH2"):
     charge =  -0.8627 
   elif (ATOM_NAME == "HH21"):
     charge =   0.4478 
   elif (ATOM_NAME == "HH22"):
     charge =   0.4478 
   elif (ATOM_NAME == "C"):
     charge =   0.7341 
   elif (ATOM_NAME == "O"):
     charge =  -0.5894 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ASH"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =   0.0341 
   elif (ATOM_NAME == "HA"):
     charge =   0.0864 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0316 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0488 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0488 
   elif (ATOM_NAME == "CG"):
     charge =   0.6462 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.5554 
   elif (ATOM_NAME == "OD2"):
     charge =  -0.6376 
   elif (ATOM_NAME == "HD2"):
     charge =   0.4747 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ASN"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =   0.0143 
   elif (ATOM_NAME == "HA"):
     charge =   0.1048 
   elif (ATOM_NAME == "CB"):
     charge =  -0.2041 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0797 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0797 
   elif (ATOM_NAME == "CG"):
     charge =   0.7130 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.5931 
   elif (ATOM_NAME == "ND2"):
     charge =  -0.9191 
   elif (ATOM_NAME == "HD21"):
     charge =   0.4196 
   elif (ATOM_NAME == "HD22"):
     charge =   0.4196 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ASP"):
   if (ATOM_NAME == "N"):
     charge =  -0.5163 
   elif (ATOM_NAME == "H"):
     charge =   0.2936 
   elif (ATOM_NAME == "CA"):
     charge =   0.0381 
   elif (ATOM_NAME == "HA"):
     charge =   0.0880 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0303 
   elif (ATOM_NAME == "HB2"):
     charge =  -0.0122 
   elif (ATOM_NAME == "HB3"):
     charge =  -0.0122 
   elif (ATOM_NAME == "CG"):
     charge =   0.7994 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.8014 
   elif (ATOM_NAME == "OD2"):
     charge =  -0.8014 
   elif (ATOM_NAME == "C"):
     charge =   0.5366 
   elif (ATOM_NAME == "O"):
     charge =  -0.5819 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CYM"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0351 
   elif (ATOM_NAME == "HA"):
     charge =   0.0508 
   elif (ATOM_NAME == "CB"):
     charge =  -0.2413 
   elif (ATOM_NAME == "HB3"):
     charge =   0.1122 
   elif (ATOM_NAME == "HB2"):
     charge =   0.1122 
   elif (ATOM_NAME == "SG"):
     charge =  -0.8844 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CYS"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =   0.0213 
   elif (ATOM_NAME == "HA"):
     charge =   0.1124 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1231 
   elif (ATOM_NAME == "HB2"):
     charge =   0.1112 
   elif (ATOM_NAME == "HB3"):
     charge =   0.1112 
   elif (ATOM_NAME == "SG"):
     charge =  -0.3119 
   elif (ATOM_NAME == "HG"):
     charge =   0.1933 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CYX"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =   0.0429 
   elif (ATOM_NAME == "HA"):
     charge =   0.0766 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0790 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0910 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0910 
   elif (ATOM_NAME == "SG"):
     charge =  -0.1081 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLH"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =   0.0145 
   elif (ATOM_NAME == "HA"):
     charge =   0.0779 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0071 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0256 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0256 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0174 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0430 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0430 
   elif (ATOM_NAME == "CD"):
     charge =   0.6801 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.5838 
   elif (ATOM_NAME == "OE2"):
     charge =  -0.6511 
   elif (ATOM_NAME == "HE2"):
     charge =   0.4641 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLN"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0031 
   elif (ATOM_NAME == "HA"):
     charge =   0.0850 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0036 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0171 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0171 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0645 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0352 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0352 
   elif (ATOM_NAME == "CD"):
     charge =   0.6951 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.6086 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.9407 
   elif (ATOM_NAME == "HE21"):
     charge =   0.4251 
   elif (ATOM_NAME == "HE22"):
     charge =   0.4251 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLU"):
   if (ATOM_NAME == "N"):
     charge =  -0.5163 
   elif (ATOM_NAME == "H"):
     charge =   0.2936 
   elif (ATOM_NAME == "CA"):
     charge =   0.0397 
   elif (ATOM_NAME == "HA"):
     charge =   0.1105 
   elif (ATOM_NAME == "CB"):
     charge =   0.0560 
   elif (ATOM_NAME == "HB2"):
     charge =  -0.0173 
   elif (ATOM_NAME == "HB3"):
     charge =  -0.0173 
   elif (ATOM_NAME == "CG"):
     charge =   0.0136 
   elif (ATOM_NAME == "HG2"):
     charge =  -0.0425 
   elif (ATOM_NAME == "HG3"):
     charge =  -0.0425 
   elif (ATOM_NAME == "CD"):
     charge =   0.8054 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.8188 
   elif (ATOM_NAME == "OE2"):
     charge =  -0.8188 
   elif (ATOM_NAME == "C"):
     charge =   0.5366 
   elif (ATOM_NAME == "O"):
     charge =  -0.5819 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLY"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0252 
   elif (ATOM_NAME == "HA2"):
     charge =   0.0698 
   elif (ATOM_NAME == "HA3"):
     charge =   0.0698 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "HID"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =   0.0188 
   elif (ATOM_NAME == "HA"):
     charge =   0.0881 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0462 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0402 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0402 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0266 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.3811 
   elif (ATOM_NAME == "HD1"):
     charge =   0.3649 
   elif (ATOM_NAME == "CE1"):
     charge =   0.2057 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1392 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.5727 
   elif (ATOM_NAME == "CD2"):
     charge =   0.1292 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1147 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "HIE"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0581 
   elif (ATOM_NAME == "HA"):
     charge =   0.1360 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0074 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0367 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0367 
   elif (ATOM_NAME == "CG"):
     charge =   0.1868 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.5432 
   elif (ATOM_NAME == "CE1"):
     charge =   0.1635 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1435 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.2795 
   elif (ATOM_NAME == "HE2"):
     charge =   0.3339 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.2207 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1862 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "HIP"):
   if (ATOM_NAME == "N"):
     charge =  -0.3479 
   elif (ATOM_NAME == "H"):
     charge =   0.2747 
   elif (ATOM_NAME == "CA"):
     charge =  -0.1354 
   elif (ATOM_NAME == "HA"):
     charge =   0.1212 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0414 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0810 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0810 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0012 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.1513 
   elif (ATOM_NAME == "HD1"):
     charge =   0.3866 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.0170 
   elif (ATOM_NAME == "HE1"):
     charge =   0.2681 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.1718 
   elif (ATOM_NAME == "HE2"):
     charge =   0.3911 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1141 
   elif (ATOM_NAME == "HD2"):
     charge =   0.2317 
   elif (ATOM_NAME == "C"):
     charge =   0.7341 
   elif (ATOM_NAME == "O"):
     charge =  -0.5894 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ILE"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0597 
   elif (ATOM_NAME == "HA"):
     charge =   0.0869 
   elif (ATOM_NAME == "CB"):
     charge =   0.1303 
   elif (ATOM_NAME == "HB"):
     charge =   0.0187 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.3204 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0882 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0882 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0882 
   elif (ATOM_NAME == "CG1"):
     charge =  -0.0430 
   elif (ATOM_NAME == "HG12"):
     charge =   0.0236 
   elif (ATOM_NAME == "HG13"):
     charge =   0.0236 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.0660 
   elif (ATOM_NAME == "HD11"):
     charge =   0.0186 
   elif (ATOM_NAME == "HD12"):
     charge =   0.0186 
   elif (ATOM_NAME == "HD13"):
     charge =   0.0186 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "LEU"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0518 
   elif (ATOM_NAME == "HA"):
     charge =   0.0922 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1102 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0457 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0457 
   elif (ATOM_NAME == "CG"):
     charge =   0.3531 
   elif (ATOM_NAME == "HG"):
     charge =  -0.0361 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.4121 
   elif (ATOM_NAME == "HD11"):
     charge =   0.1000 
   elif (ATOM_NAME == "HD12"):
     charge =   0.1000 
   elif (ATOM_NAME == "HD13"):
     charge =   0.1000 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.4121 
   elif (ATOM_NAME == "HD21"):
     charge =   0.1000 
   elif (ATOM_NAME == "HD22"):
     charge =   0.1000 
   elif (ATOM_NAME == "HD23"):
     charge =   0.1000 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "LYN"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0721 
   elif (ATOM_NAME == "HA"):
     charge =   0.0994 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0485 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0340 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0340 
   elif (ATOM_NAME == "CG"):
     charge =   0.0661 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0104 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0104 
   elif (ATOM_NAME == "CD"):
     charge =  -0.0377 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0115 
   elif (ATOM_NAME == "HD3"):
     charge =   0.0115 
   elif (ATOM_NAME == "CE"):
     charge =   0.3260 
   elif (ATOM_NAME == "HE2"):
     charge =  -0.0336 
   elif (ATOM_NAME == "HE3"):
     charge =  -0.0336 
   elif (ATOM_NAME == "NZ"):
     charge =  -1.0358 
   elif (ATOM_NAME == "HZ2"):
     charge =   0.3860 
   elif (ATOM_NAME == "HZ3"):
     charge =   0.3860 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "LYS"):
   if (ATOM_NAME == "N"):
     charge =  -0.3479 
   elif (ATOM_NAME == "H"):
     charge =   0.2747 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2400 
   elif (ATOM_NAME == "HA"):
     charge =   0.1426 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0094 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0362 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0362 
   elif (ATOM_NAME == "CG"):
     charge =   0.0187 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0103 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0103 
   elif (ATOM_NAME == "CD"):
     charge =  -0.0479 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0621 
   elif (ATOM_NAME == "HD3"):
     charge =   0.0621 
   elif (ATOM_NAME == "CE"):
     charge =  -0.0143 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1135 
   elif (ATOM_NAME == "HE3"):
     charge =   0.1135 
   elif (ATOM_NAME == "NZ"):
     charge =  -0.3854 
   elif (ATOM_NAME == "HZ1"):
     charge =   0.3400 
   elif (ATOM_NAME == "HZ2"):
     charge =   0.3400 
   elif (ATOM_NAME == "HZ3"):
     charge =   0.3400 
   elif (ATOM_NAME == "C"):
     charge =   0.7341 
   elif (ATOM_NAME == "O"):
     charge =  -0.5894 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "MET"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0237 
   elif (ATOM_NAME == "HA"):
     charge =   0.0880 
   elif (ATOM_NAME == "CB"):
     charge =   0.0342 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0241 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0241 
   elif (ATOM_NAME == "CG"):
     charge =   0.0018 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0440 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0440 
   elif (ATOM_NAME == "SD"):
     charge =  -0.2737 
   elif (ATOM_NAME == "CE"):
     charge =  -0.0536 
   elif (ATOM_NAME == "HE1"):
     charge =   0.0684 
   elif (ATOM_NAME == "HE2"):
     charge =   0.0684 
   elif (ATOM_NAME == "HE3"):
     charge =   0.0684 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "PHE"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0024 
   elif (ATOM_NAME == "HA"):
     charge =   0.0978 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0343 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0295 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0295 
   elif (ATOM_NAME == "CG"):
     charge =   0.0118 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1256 
   elif (ATOM_NAME == "HD1"):
     charge =   0.1330 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.1704 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1430 
   elif (ATOM_NAME == "CZ"):
     charge =  -0.1072 
   elif (ATOM_NAME == "HZ"):
     charge =   0.1297 
   elif (ATOM_NAME == "CE2"):
     charge =  -0.1704 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1430 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1256 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1330 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "PRO"):
   if (ATOM_NAME == "N"):
     charge =  -0.2548 
   elif (ATOM_NAME == "CD"):
     charge =   0.0192 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0391 
   elif (ATOM_NAME == "HD3"):
     charge =   0.0391 
   elif (ATOM_NAME == "CG"):
     charge =   0.0189 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0213 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0213 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0070 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0253 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0253 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0266 
   elif (ATOM_NAME == "HA"):
     charge =   0.0641 
   elif (ATOM_NAME == "C"):
     charge =   0.5896 
   elif (ATOM_NAME == "O"):
     charge =  -0.5748 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "SER"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0249 
   elif (ATOM_NAME == "HA"):
     charge =   0.0843 
   elif (ATOM_NAME == "CB"):
     charge =   0.2117 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0352 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0352 
   elif (ATOM_NAME == "OG"):
     charge =  -0.6546 
   elif (ATOM_NAME == "HG"):
     charge =   0.4275 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "THR"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0389 
   elif (ATOM_NAME == "HA"):
     charge =   0.1007 
   elif (ATOM_NAME == "CB"):
     charge =   0.3654 
   elif (ATOM_NAME == "HB"):
     charge =   0.0043 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.2438 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0642 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0642 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0642 
   elif (ATOM_NAME == "OG1"):
     charge =  -0.6761 
   elif (ATOM_NAME == "HG1"):
     charge =   0.4102 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "TRP"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0275 
   elif (ATOM_NAME == "HA"):
     charge =   0.1123 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0050 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0339 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0339 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1415 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1638 
   elif (ATOM_NAME == "HD1"):
     charge =   0.2062 
   elif (ATOM_NAME == "NE1"):
     charge =  -0.3418 
   elif (ATOM_NAME == "HE1"):
     charge =   0.3412 
   elif (ATOM_NAME == "CE2"):
     charge =   0.1380 
   elif (ATOM_NAME == "CZ2"):
     charge =  -0.2601 
   elif (ATOM_NAME == "HZ2"):
     charge =   0.1572 
   elif (ATOM_NAME == "CH2"):
     charge =  -0.1134 
   elif (ATOM_NAME == "HH2"):
     charge =   0.1417 
   elif (ATOM_NAME == "CZ3"):
     charge =  -0.1972 
   elif (ATOM_NAME == "HZ3"):
     charge =   0.1447 
   elif (ATOM_NAME == "CE3"):
     charge =  -0.2387 
   elif (ATOM_NAME == "HE3"):
     charge =   0.1700 
   elif (ATOM_NAME == "CD2"):
     charge =   0.1243 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "TYR"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0014 
   elif (ATOM_NAME == "HA"):
     charge =   0.0876 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0152 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0295 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0295 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0011 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1906 
   elif (ATOM_NAME == "HD1"):
     charge =   0.1699 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.2341 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1656 
   elif (ATOM_NAME == "CZ"):
     charge =   0.3226 
   elif (ATOM_NAME == "OH"):
     charge =  -0.5579 
   elif (ATOM_NAME == "HH"):
     charge =   0.3992 
   elif (ATOM_NAME == "CE2"):
     charge =  -0.2341 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1656 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1906 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1699 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "VAL"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0875 
   elif (ATOM_NAME == "HA"):
     charge =   0.0969 
   elif (ATOM_NAME == "CB"):
     charge =   0.2985 
   elif (ATOM_NAME == "HB"):
     charge =  -0.0297 
   elif (ATOM_NAME == "CG1"):
     charge =  -0.3192 
   elif (ATOM_NAME == "HG11"):
     charge =   0.0791 
   elif (ATOM_NAME == "HG12"):
     charge =   0.0791 
   elif (ATOM_NAME == "HG13"):
     charge =   0.0791 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.3192 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0791 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0791 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0791 
   elif (ATOM_NAME == "C"):
     charge =   0.5973 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "WAT"):
   if (ATOM_NAME == "O"):
     charge =  -0.8340 
   elif (ATOM_NAME == "H1"):
     charge =   0.4170 
   elif (ATOM_NAME == "H2"):
     charge =   0.4170 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "Na+"):
   if (ATOM_NAME == "Na+"):
     charge =   1.0000 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "Cl-"):
   if (ATOM_NAME == "Cl-"):
     charge =  -1.0000 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 else:
   print ("THE RESIDUE %s IS WRONG" %(RES_NAME)) 
 try:
   return charge
 except:
   library_warning_message()

def N_terminal_charge(ATOM_NAME,RES_NAME):
 if (RES_NAME == "ACE"): 
   if (ATOM_NAME == "HH31"):
     charge =   0.1123 
   elif (ATOM_NAME == "CH3"):
     charge =  -0.3662 
   elif (ATOM_NAME == "HH32"):
     charge =   0.1123 
   elif (ATOM_NAME == "HH33"):
     charge =   0.1123 
   elif (ATOM_NAME == "C"):
     charge =   0.5972 
   elif (ATOM_NAME == "O"):
     charge =  -0.5679 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NALA"):
   if (ATOM_NAME == "N"):
     charge =   0.1414 
   elif (ATOM_NAME == "H1"):
     charge =   0.1997 
   elif (ATOM_NAME == "H2"):
     charge =   0.1997 
   elif (ATOM_NAME == "H3"):
     charge =   0.1997 
   elif (ATOM_NAME == "CA"):
     charge =   0.0962 
   elif (ATOM_NAME == "HA"):
     charge =   0.0889 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0597 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0300 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0300 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0300 
   elif (ATOM_NAME == "C"):
     charge =   0.6163 
   elif (ATOM_NAME == "O"):
     charge =  -0.5722 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NARG"):
   if (ATOM_NAME == "N"):
     charge =   0.1305 
   elif (ATOM_NAME == "H1"):
     charge =   0.2083 
   elif (ATOM_NAME == "H2"):
     charge =   0.2083 
   elif (ATOM_NAME == "H3"):
     charge =   0.2083 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0223 
   elif (ATOM_NAME == "HA"):
     charge =   0.1242 
   elif (ATOM_NAME == "CB"):
     charge =   0.0118 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0226 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0226 
   elif (ATOM_NAME == "CG"):
     charge =   0.0236 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0309 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0309 
   elif (ATOM_NAME == "CD"):
     charge =   0.0935 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0527 
   elif (ATOM_NAME == "HD3"):
     charge =   0.0527 
   elif (ATOM_NAME == "NE"):
     charge =  -0.5650 
   elif (ATOM_NAME == "HE"):
     charge =   0.3592 
   elif (ATOM_NAME == "CZ"):
     charge =   0.8281 
   elif (ATOM_NAME == "NH1"):
     charge =  -0.8693 
   elif (ATOM_NAME == "HH11"):
     charge =   0.4494 
   elif (ATOM_NAME == "HH12"):
     charge =   0.4494 
   elif (ATOM_NAME == "NH2"):
     charge =  -0.8693 
   elif (ATOM_NAME == "HH21"):
     charge =   0.4494 
   elif (ATOM_NAME == "HH22"):
     charge =   0.4494 
   elif (ATOM_NAME == "C"):
     charge =   0.7214 
   elif (ATOM_NAME == "O"):
     charge =  -0.6013 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NASN"):
   if (ATOM_NAME == "N"):
     charge =   0.1801 
   elif (ATOM_NAME == "H1"):
     charge =   0.1921 
   elif (ATOM_NAME == "H2"):
     charge =   0.1921 
   elif (ATOM_NAME == "H3"):
     charge =   0.1921 
   elif (ATOM_NAME == "CA"):
     charge =   0.0368 
   elif (ATOM_NAME == "HA"):
     charge =   0.1231 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0283 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0515 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0515 
   elif (ATOM_NAME == "CG"):
     charge =   0.5833 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.5744 
   elif (ATOM_NAME == "ND2"):
     charge =  -0.8634 
   elif (ATOM_NAME == "HD21"):
     charge =   0.4097 
   elif (ATOM_NAME == "HD22"):
     charge =   0.4097 
   elif (ATOM_NAME == "C"):
     charge =   0.6163 
   elif (ATOM_NAME == "O"):
     charge =  -0.5722 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NASP"):
   if (ATOM_NAME == "N"):
     charge =   0.0782 
   elif (ATOM_NAME == "H1"):
     charge =   0.2200 
   elif (ATOM_NAME == "H2"):
     charge =   0.2200 
   elif (ATOM_NAME == "H3"):
     charge =   0.2200 
   elif (ATOM_NAME == "CA"):
     charge =   0.0292 
   elif (ATOM_NAME == "HA"):
     charge =   0.1141 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0235 
   elif (ATOM_NAME == "HB2"):
     charge =  -0.0169 
   elif (ATOM_NAME == "HB3"):
     charge =  -0.0169 
   elif (ATOM_NAME == "CG"):
     charge =   0.8194 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.8084 
   elif (ATOM_NAME == "OD2"):
     charge =  -0.8084 
   elif (ATOM_NAME == "C"):
     charge =   0.5621 
   elif (ATOM_NAME == "O"):
     charge =  -0.5889 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NCYS"):
   if (ATOM_NAME == "N"):
     charge =   0.1325 
   elif (ATOM_NAME == "H1"):
     charge =   0.2023 
   elif (ATOM_NAME == "H2"):
     charge =   0.2023 
   elif (ATOM_NAME == "H3"):
     charge =   0.2023 
   elif (ATOM_NAME == "CA"):
     charge =   0.0927 
   elif (ATOM_NAME == "HA"):
     charge =   0.1411 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1195 
   elif (ATOM_NAME == "HB2"):
     charge =   0.1188 
   elif (ATOM_NAME == "HB3"):
     charge =   0.1188 
   elif (ATOM_NAME == "SG"):
     charge =  -0.3298 
   elif (ATOM_NAME == "HG"):
     charge =   0.1975 
   elif (ATOM_NAME == "C"):
     charge =   0.6123 
   elif (ATOM_NAME == "O"):
     charge =  -0.5713 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NCYX"):
   if (ATOM_NAME == "N"):
     charge =   0.2069 
   elif (ATOM_NAME == "H1"):
     charge =   0.1815 
   elif (ATOM_NAME == "H2"):
     charge =   0.1815 
   elif (ATOM_NAME == "H3"):
     charge =   0.1815 
   elif (ATOM_NAME == "CA"):
     charge =   0.1055 
   elif (ATOM_NAME == "HA"):
     charge =   0.0922 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0277 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0680 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0680 
   elif (ATOM_NAME == "SG"):
     charge =  -0.0984 
   elif (ATOM_NAME == "C"):
     charge =   0.6123 
   elif (ATOM_NAME == "O"):
     charge =  -0.5713 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NGLN"):
   if (ATOM_NAME == "N"):
     charge =   0.1493 
   elif (ATOM_NAME == "H1"):
     charge =   0.1996 
   elif (ATOM_NAME == "H2"):
     charge =   0.1996 
   elif (ATOM_NAME == "H3"):
     charge =   0.1996 
   elif (ATOM_NAME == "CA"):
     charge =   0.0536 
   elif (ATOM_NAME == "HA"):
     charge =   0.1015 
   elif (ATOM_NAME == "CB"):
     charge =   0.0651 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0050 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0050 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0903 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0331 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0331 
   elif (ATOM_NAME == "CD"):
     charge =   0.7354 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.6133 
   elif (ATOM_NAME == "NE2"):
     charge =  -1.0031 
   elif (ATOM_NAME == "HE21"):
     charge =   0.4429 
   elif (ATOM_NAME == "HE22"):
     charge =   0.4429 
   elif (ATOM_NAME == "C"):
     charge =   0.6123 
   elif (ATOM_NAME == "O"):
     charge =  -0.5713 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NGLU"):
   if (ATOM_NAME == "N"):
     charge =   0.0017 
   elif (ATOM_NAME == "H1"):
     charge =   0.2391 
   elif (ATOM_NAME == "H2"):
     charge =   0.2391 
   elif (ATOM_NAME == "H3"):
     charge =   0.2391 
   elif (ATOM_NAME == "CA"):
     charge =   0.0588 
   elif (ATOM_NAME == "HA"):
     charge =   0.1202 
   elif (ATOM_NAME == "CB"):
     charge =   0.0909 
   elif (ATOM_NAME == "HB2"):
     charge =  -0.0232 
   elif (ATOM_NAME == "HB3"):
     charge =  -0.0232 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0236 
   elif (ATOM_NAME == "HG2"):
     charge =  -0.0315 
   elif (ATOM_NAME == "HG3"):
     charge =  -0.0315 
   elif (ATOM_NAME == "CD"):
     charge =   0.8087 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.8189 
   elif (ATOM_NAME == "OE2"):
     charge =  -0.8189 
   elif (ATOM_NAME == "C"):
     charge =   0.5621 
   elif (ATOM_NAME == "O"):
     charge =  -0.5889 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NGLY"):
   if (ATOM_NAME == "N"):
     charge =   0.2943 
   elif (ATOM_NAME == "H1"):
     charge =   0.1642 
   elif (ATOM_NAME == "H2"):
     charge =   0.1642 
   elif (ATOM_NAME == "H3"):
     charge =   0.1642 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0100 
   elif (ATOM_NAME == "HA2"):
     charge =   0.0895 
   elif (ATOM_NAME == "HA3"):
     charge =   0.0895 
   elif (ATOM_NAME == "C"):
     charge =   0.6163 
   elif (ATOM_NAME == "O"):
     charge =  -0.5722 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NHID"):
   if (ATOM_NAME == "N"):
     charge =   0.1542 
   elif (ATOM_NAME == "H1"):
     charge =   0.1963 
   elif (ATOM_NAME == "H2"):
     charge =   0.1963 
   elif (ATOM_NAME == "H3"):
     charge =   0.1963 
   elif (ATOM_NAME == "CA"):
     charge =   0.0964 
   elif (ATOM_NAME == "HA"):
     charge =   0.0958 
   elif (ATOM_NAME == "CB"):
     charge =   0.0259 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0209 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0209 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0399 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.3819 
   elif (ATOM_NAME == "HD1"):
     charge =   0.3632 
   elif (ATOM_NAME == "CE1"):
     charge =   0.2127 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1385 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.5711 
   elif (ATOM_NAME == "CD2"):
     charge =   0.1046 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1299 
   elif (ATOM_NAME == "C"):
     charge =   0.6123 
   elif (ATOM_NAME == "O"):
     charge =  -0.5713 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NHIE"):
   if (ATOM_NAME == "N"):
     charge =   0.1472 
   elif (ATOM_NAME == "H1"):
     charge =   0.2016 
   elif (ATOM_NAME == "H2"):
     charge =   0.2016 
   elif (ATOM_NAME == "H3"):
     charge =   0.2016 
   elif (ATOM_NAME == "CA"):
     charge =   0.0236 
   elif (ATOM_NAME == "HA"):
     charge =   0.1380 
   elif (ATOM_NAME == "CB"):
     charge =   0.0489 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0223 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0223 
   elif (ATOM_NAME == "CG"):
     charge =   0.1740 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.5579 
   elif (ATOM_NAME == "CE1"):
     charge =   0.1804 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1397 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.2781 
   elif (ATOM_NAME == "HE2"):
     charge =   0.3324 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.2349 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1963 
   elif (ATOM_NAME == "C"):
     charge =   0.6123 
   elif (ATOM_NAME == "O"):
     charge =  -0.5713 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NHIP"):
   if (ATOM_NAME == "N"):
     charge =   0.2560 
   elif (ATOM_NAME == "H1"):
     charge =   0.1704 
   elif (ATOM_NAME == "H2"):
     charge =   0.1704 
   elif (ATOM_NAME == "H3"):
     charge =   0.1704 
   elif (ATOM_NAME == "CA"):
     charge =   0.0581 
   elif (ATOM_NAME == "HA"):
     charge =   0.1047 
   elif (ATOM_NAME == "CB"):
     charge =   0.0484 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0531 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0531 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0236 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.1510 
   elif (ATOM_NAME == "HD1"):
     charge =   0.3821 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.0011 
   elif (ATOM_NAME == "HE1"):
     charge =   0.2645 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.1739 
   elif (ATOM_NAME == "HE2"):
     charge =   0.3921 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1433 
   elif (ATOM_NAME == "HD2"):
     charge =   0.2495 
   elif (ATOM_NAME == "C"):
     charge =   0.7214 
   elif (ATOM_NAME == "O"):
     charge =  -0.6013 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NILE"):
   if (ATOM_NAME == "N"):
     charge =   0.0311 
   elif (ATOM_NAME == "H1"):
     charge =   0.2329 
   elif (ATOM_NAME == "H2"):
     charge =   0.2329 
   elif (ATOM_NAME == "H3"):
     charge =   0.2329 
   elif (ATOM_NAME == "CA"):
     charge =   0.0257 
   elif (ATOM_NAME == "HA"):
     charge =   0.1031 
   elif (ATOM_NAME == "CB"):
     charge =   0.1885 
   elif (ATOM_NAME == "HB"):
     charge =   0.0213 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.3720 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0947 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0947 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0947 
   elif (ATOM_NAME == "CG1"):
     charge =  -0.0387 
   elif (ATOM_NAME == "HG12"):
     charge =   0.0201 
   elif (ATOM_NAME == "HG13"):
     charge =   0.0201 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.0908 
   elif (ATOM_NAME == "HD11"):
     charge =   0.0226 
   elif (ATOM_NAME == "HD12"):
     charge =   0.0226 
   elif (ATOM_NAME == "HD13"):
     charge =   0.0226 
   elif (ATOM_NAME == "C"):
     charge =   0.6123 
   elif (ATOM_NAME == "O"):
     charge =  -0.5713 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NLEU"):
   if (ATOM_NAME == "N"):
     charge =   0.1010 
   elif (ATOM_NAME == "H1"):
     charge =   0.2148 
   elif (ATOM_NAME == "H2"):
     charge =   0.2148 
   elif (ATOM_NAME == "H3"):
     charge =   0.2148 
   elif (ATOM_NAME == "CA"):
     charge =   0.0104 
   elif (ATOM_NAME == "HA"):
     charge =   0.1053 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0244 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0256 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0256 
   elif (ATOM_NAME == "CG"):
     charge =   0.3421 
   elif (ATOM_NAME == "HG"):
     charge =  -0.0380 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.4106 
   elif (ATOM_NAME == "HD11"):
     charge =   0.0980 
   elif (ATOM_NAME == "HD12"):
     charge =   0.0980 
   elif (ATOM_NAME == "HD13"):
     charge =   0.0980 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.4104 
   elif (ATOM_NAME == "HD21"):
     charge =   0.0980 
   elif (ATOM_NAME == "HD22"):
     charge =   0.0980 
   elif (ATOM_NAME == "HD23"):
     charge =   0.0980 
   elif (ATOM_NAME == "C"):
     charge =   0.6123 
   elif (ATOM_NAME == "O"):
     charge =  -0.5713 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NLYS"):
   if (ATOM_NAME == "N"):
     charge =   0.0966 
   elif (ATOM_NAME == "H1"):
     charge =   0.2165 
   elif (ATOM_NAME == "H2"):
     charge =   0.2165 
   elif (ATOM_NAME == "H3"):
     charge =   0.2165 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0015 
   elif (ATOM_NAME == "HA"):
     charge =   0.1180 
   elif (ATOM_NAME == "CB"):
     charge =   0.0212 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0283 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0283 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0048 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0121 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0121 
   elif (ATOM_NAME == "CD"):
     charge =  -0.0608 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0633 
   elif (ATOM_NAME == "HD3"):
     charge =   0.0633 
   elif (ATOM_NAME == "CE"):
     charge =  -0.0181 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1171 
   elif (ATOM_NAME == "HE3"):
     charge =   0.1171 
   elif (ATOM_NAME == "NZ"):
     charge =  -0.3764 
   elif (ATOM_NAME == "HZ1"):
     charge =   0.3382 
   elif (ATOM_NAME == "HZ2"):
     charge =   0.3382 
   elif (ATOM_NAME == "HZ3"):
     charge =   0.3382 
   elif (ATOM_NAME == "C"):
     charge =   0.7214 
   elif (ATOM_NAME == "O"):
     charge =  -0.6013 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NMET"):
   if (ATOM_NAME == "N"):
     charge =   0.1592 
   elif (ATOM_NAME == "H1"):
     charge =   0.1984 
   elif (ATOM_NAME == "H2"):
     charge =   0.1984 
   elif (ATOM_NAME == "H3"):
     charge =   0.1984 
   elif (ATOM_NAME == "CA"):
     charge =   0.0221 
   elif (ATOM_NAME == "HA"):
     charge =   0.1116 
   elif (ATOM_NAME == "CB"):
     charge =   0.0865 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0125 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0125 
   elif (ATOM_NAME == "CG"):
     charge =   0.0334 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0292 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0292 
   elif (ATOM_NAME == "SD"):
     charge =  -0.2774 
   elif (ATOM_NAME == "CE"):
     charge =  -0.0341 
   elif (ATOM_NAME == "HE1"):
     charge =   0.0597 
   elif (ATOM_NAME == "HE2"):
     charge =   0.0597 
   elif (ATOM_NAME == "HE3"):
     charge =   0.0597 
   elif (ATOM_NAME == "C"):
     charge =   0.6123 
   elif (ATOM_NAME == "O"):
     charge =  -0.5713 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NPHE"):
   if (ATOM_NAME == "N"):
     charge =   0.1737 
   elif (ATOM_NAME == "H1"):
     charge =   0.1921 
   elif (ATOM_NAME == "H2"):
     charge =   0.1921 
   elif (ATOM_NAME == "H3"):
     charge =   0.1921 
   elif (ATOM_NAME == "CA"):
     charge =   0.0733 
   elif (ATOM_NAME == "HA"):
     charge =   0.1041 
   elif (ATOM_NAME == "CB"):
     charge =   0.0330 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0104 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0104 
   elif (ATOM_NAME == "CG"):
     charge =   0.0031 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1392 
   elif (ATOM_NAME == "HD1"):
     charge =   0.1374 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.1602 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1433 
   elif (ATOM_NAME == "CZ"):
     charge =  -0.1208 
   elif (ATOM_NAME == "HZ"):
     charge =   0.1329 
   elif (ATOM_NAME == "CE2"):
     charge =  -0.1603 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1433 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1391 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1374 
   elif (ATOM_NAME == "C"):
     charge =   0.6123 
   elif (ATOM_NAME == "O"):
     charge =  -0.5713 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NPRO"):
   if (ATOM_NAME == "N"):
     charge =  -0.2020 
   elif (ATOM_NAME == "H2"):
     charge =   0.3120 
   elif (ATOM_NAME == "H3"):
     charge =   0.3120 
   elif (ATOM_NAME == "CD"):
     charge =  -0.0120 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1000 
   elif (ATOM_NAME == "HD3"):
     charge =   0.1000 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1210 
   elif (ATOM_NAME == "HG2"):
     charge =   0.1000 
   elif (ATOM_NAME == "HG3"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HB2"):
     charge =   0.1000 
   elif (ATOM_NAME == "HB3"):
     charge =   0.1000 
   elif (ATOM_NAME == "CA"):
     charge =   0.1000 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "C"):
     charge =   0.5260 
   elif (ATOM_NAME == "O"):
     charge =  -0.5000 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NSER"):
   if (ATOM_NAME == "N"):
     charge =   0.1849 
   elif (ATOM_NAME == "H1"):
     charge =   0.1898 
   elif (ATOM_NAME == "H2"):
     charge =   0.1898 
   elif (ATOM_NAME == "H3"):
     charge =   0.1898 
   elif (ATOM_NAME == "CA"):
     charge =   0.0567 
   elif (ATOM_NAME == "HA"):
     charge =   0.0782 
   elif (ATOM_NAME == "CB"):
     charge =   0.2596 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0273 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0273 
   elif (ATOM_NAME == "OG"):
     charge =  -0.6714 
   elif (ATOM_NAME == "HG"):
     charge =   0.4239 
   elif (ATOM_NAME == "C"):
     charge =   0.6163 
   elif (ATOM_NAME == "O"):
     charge =  -0.5722 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NTHR"):
   if (ATOM_NAME == "N"):
     charge =   0.1812 
   elif (ATOM_NAME == "H1"):
     charge =   0.1934 
   elif (ATOM_NAME == "H2"):
     charge =   0.1934 
   elif (ATOM_NAME == "H3"):
     charge =   0.1934 
   elif (ATOM_NAME == "CA"):
     charge =   0.0034 
   elif (ATOM_NAME == "HA"):
     charge =   0.1087 
   elif (ATOM_NAME == "CB"):
     charge =   0.4514 
   elif (ATOM_NAME == "HB"):
     charge =  -0.0323 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.2554 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0627 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0627 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0627 
   elif (ATOM_NAME == "OG1"):
     charge =  -0.6764 
   elif (ATOM_NAME == "HG1"):
     charge =   0.4070 
   elif (ATOM_NAME == "C"):
     charge =   0.6163 
   elif (ATOM_NAME == "O"):
     charge =  -0.5722 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NTRP"):
   if (ATOM_NAME == "N"):
     charge =   0.1913 
   elif (ATOM_NAME == "H1"):
     charge =   0.1888 
   elif (ATOM_NAME == "H2"):
     charge =   0.1888 
   elif (ATOM_NAME == "H3"):
     charge =   0.1888 
   elif (ATOM_NAME == "CA"):
     charge =   0.0421 
   elif (ATOM_NAME == "HA"):
     charge =   0.1162 
   elif (ATOM_NAME == "CB"):
     charge =   0.0543 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0222 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0222 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1654 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1788 
   elif (ATOM_NAME == "HD1"):
     charge =   0.2195 
   elif (ATOM_NAME == "NE1"):
     charge =  -0.3444 
   elif (ATOM_NAME == "HE1"):
     charge =   0.3412 
   elif (ATOM_NAME == "CE2"):
     charge =   0.1575 
   elif (ATOM_NAME == "CZ2"):
     charge =  -0.2710 
   elif (ATOM_NAME == "HZ2"):
     charge =   0.1589 
   elif (ATOM_NAME == "CH2"):
     charge =  -0.1080 
   elif (ATOM_NAME == "HH2"):
     charge =   0.1411 
   elif (ATOM_NAME == "CZ3"):
     charge =  -0.2034 
   elif (ATOM_NAME == "HZ3"):
     charge =   0.1458 
   elif (ATOM_NAME == "CE3"):
     charge =  -0.2265 
   elif (ATOM_NAME == "HE3"):
     charge =   0.1646 
   elif (ATOM_NAME == "CD2"):
     charge =   0.1132 
   elif (ATOM_NAME == "C"):
     charge =   0.6123 
   elif (ATOM_NAME == "O"):
     charge =  -0.5713 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NTYR"):
   if (ATOM_NAME == "N"):
     charge =   0.1940 
   elif (ATOM_NAME == "H1"):
     charge =   0.1873 
   elif (ATOM_NAME == "H2"):
     charge =   0.1873 
   elif (ATOM_NAME == "H3"):
     charge =   0.1873 
   elif (ATOM_NAME == "CA"):
     charge =   0.0570 
   elif (ATOM_NAME == "HA"):
     charge =   0.0983 
   elif (ATOM_NAME == "CB"):
     charge =   0.0659 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0102 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0102 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0205 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.2002 
   elif (ATOM_NAME == "HD1"):
     charge =   0.1720 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.2239 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1650 
   elif (ATOM_NAME == "CZ"):
     charge =   0.3139 
   elif (ATOM_NAME == "OH"):
     charge =  -0.5578 
   elif (ATOM_NAME == "HH"):
     charge =   0.4001 
   elif (ATOM_NAME == "CE2"):
     charge =  -0.2239 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1650 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.2002 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1720 
   elif (ATOM_NAME == "C"):
     charge =   0.6123 
   elif (ATOM_NAME == "O"):
     charge =  -0.5713 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NVAL"):
   if (ATOM_NAME == "N"):
     charge =   0.0577 
   elif (ATOM_NAME == "H1"):
     charge =   0.2272 
   elif (ATOM_NAME == "H2"):
     charge =   0.2272 
   elif (ATOM_NAME == "H3"):
     charge =   0.2272 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0054 
   elif (ATOM_NAME == "HA"):
     charge =   0.1093 
   elif (ATOM_NAME == "CB"):
     charge =   0.3196 
   elif (ATOM_NAME == "HB"):
     charge =  -0.0221 
   elif (ATOM_NAME == "CG1"):
     charge =  -0.3129 
   elif (ATOM_NAME == "HG11"):
     charge =   0.0735 
   elif (ATOM_NAME == "HG12"):
     charge =   0.0735 
   elif (ATOM_NAME == "HG13"):
     charge =   0.0735 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.3129 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0735 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0735 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0735 
   elif (ATOM_NAME == "C"):
     charge =   0.6163 
   elif (ATOM_NAME == "O"):
     charge =  -0.5722 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 else:
   print ("THE RESIDUE %s IS WRONG" %(RES_NAME)) 
 try:
    return charge
 except:
    library_warning_message()

def C_terminal_charge(ATOM_NAME,RES_NAME):
 if (RES_NAME == "CALA"): 
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.1747 
   elif (ATOM_NAME == "HA"):
     charge =   0.1067 
   elif (ATOM_NAME == "CB"):
     charge =  -0.2093 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0764 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0764 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0764 
   elif (ATOM_NAME == "C"):
     charge =   0.7731 
   elif (ATOM_NAME == "O"):
     charge =  -0.8055 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8055 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CARG"):
   if (ATOM_NAME == "N"):
     charge =  -0.3481 
   elif (ATOM_NAME == "H"):
     charge =   0.2764 
   elif (ATOM_NAME == "CA"):
     charge =  -0.3068 
   elif (ATOM_NAME == "HA"):
     charge =   0.1447 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0374 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0371 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0371 
   elif (ATOM_NAME == "CG"):
     charge =   0.0744 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0185 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0185 
   elif (ATOM_NAME == "CD"):
     charge =   0.1114 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0468 
   elif (ATOM_NAME == "HD3"):
     charge =   0.0468 
   elif (ATOM_NAME == "NE"):
     charge =  -0.5564 
   elif (ATOM_NAME == "HE"):
     charge =   0.3479 
   elif (ATOM_NAME == "CZ"):
     charge =   0.8368 
   elif (ATOM_NAME == "NH1"):
     charge =  -0.8737 
   elif (ATOM_NAME == "HH11"):
     charge =   0.4493 
   elif (ATOM_NAME == "HH12"):
     charge =   0.4493 
   elif (ATOM_NAME == "NH2"):
     charge =  -0.8737 
   elif (ATOM_NAME == "HH21"):
     charge =   0.4493 
   elif (ATOM_NAME == "HH22"):
     charge =   0.4493 
   elif (ATOM_NAME == "C"):
     charge =   0.8557 
   elif (ATOM_NAME == "O"):
     charge =  -0.8266 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8266 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CASN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2080 
   elif (ATOM_NAME == "HA"):
     charge =   0.1358 
   elif (ATOM_NAME == "CB"):
     charge =  -0.2299 
   elif (ATOM_NAME == "HB2"):
     charge =   0.1023 
   elif (ATOM_NAME == "HB3"):
     charge =   0.1023 
   elif (ATOM_NAME == "CG"):
     charge =   0.7153 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.6010 
   elif (ATOM_NAME == "ND2"):
     charge =  -0.9084 
   elif (ATOM_NAME == "HD21"):
     charge =   0.4150 
   elif (ATOM_NAME == "HD22"):
     charge =   0.4150 
   elif (ATOM_NAME == "C"):
     charge =   0.8050 
   elif (ATOM_NAME == "O"):
     charge =  -0.8147 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8147 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CASP"):
   if (ATOM_NAME == "N"):
     charge =  -0.5192 
   elif (ATOM_NAME == "H"):
     charge =   0.3055 
   elif (ATOM_NAME == "CA"):
     charge =  -0.1817 
   elif (ATOM_NAME == "HA"):
     charge =   0.1046 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0677 
   elif (ATOM_NAME == "HB2"):
     charge =  -0.0212 
   elif (ATOM_NAME == "HB3"):
     charge =  -0.0212 
   elif (ATOM_NAME == "CG"):
     charge =   0.8851 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.8162 
   elif (ATOM_NAME == "OD2"):
     charge =  -0.8162 
   elif (ATOM_NAME == "C"):
     charge =   0.7256 
   elif (ATOM_NAME == "O"):
     charge =  -0.7887 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.7887 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CCYS"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.1635 
   elif (ATOM_NAME == "HA"):
     charge =   0.1396 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1996 
   elif (ATOM_NAME == "HB2"):
     charge =   0.1437 
   elif (ATOM_NAME == "HB3"):
     charge =   0.1437 
   elif (ATOM_NAME == "SG"):
     charge =  -0.3102 
   elif (ATOM_NAME == "HG"):
     charge =   0.2068 
   elif (ATOM_NAME == "C"):
     charge =   0.7497 
   elif (ATOM_NAME == "O"):
     charge =  -0.7981 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.7981 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CCYX"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.1318 
   elif (ATOM_NAME == "HA"):
     charge =   0.0938 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1943 
   elif (ATOM_NAME == "HB2"):
     charge =   0.1228 
   elif (ATOM_NAME == "HB3"):
     charge =   0.1228 
   elif (ATOM_NAME == "SG"):
     charge =  -0.0529 
   elif (ATOM_NAME == "C"):
     charge =   0.7618 
   elif (ATOM_NAME == "O"):
     charge =  -0.8041 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8041 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CGLN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2248 
   elif (ATOM_NAME == "HA"):
     charge =   0.1232 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0664 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0452 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0452 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0210 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0203 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0203 
   elif (ATOM_NAME == "CD"):
     charge =   0.7093 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.6098 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.9574 
   elif (ATOM_NAME == "HE21"):
     charge =   0.4304 
   elif (ATOM_NAME == "HE22"):
     charge =   0.4304 
   elif (ATOM_NAME == "C"):
     charge =   0.7775 
   elif (ATOM_NAME == "O"):
     charge =  -0.8042 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8042 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CGLU"):
   if (ATOM_NAME == "N"):
     charge =  -0.5192 
   elif (ATOM_NAME == "H"):
     charge =   0.3055 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2059 
   elif (ATOM_NAME == "HA"):
     charge =   0.1399 
   elif (ATOM_NAME == "CB"):
     charge =   0.0071 
   elif (ATOM_NAME == "HB2"):
     charge =  -0.0078 
   elif (ATOM_NAME == "HB3"):
     charge =  -0.0078 
   elif (ATOM_NAME == "CG"):
     charge =   0.0675 
   elif (ATOM_NAME == "HG2"):
     charge =  -0.0548 
   elif (ATOM_NAME == "HG3"):
     charge =  -0.0548 
   elif (ATOM_NAME == "CD"):
     charge =   0.8183 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.8220 
   elif (ATOM_NAME == "OE2"):
     charge =  -0.8220 
   elif (ATOM_NAME == "C"):
     charge =   0.7420 
   elif (ATOM_NAME == "O"):
     charge =  -0.7930 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.7930 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CGLY"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2493 
   elif (ATOM_NAME == "HA2"):
     charge =   0.1056 
   elif (ATOM_NAME == "HA3"):
     charge =   0.1056 
   elif (ATOM_NAME == "C"):
     charge =   0.7231 
   elif (ATOM_NAME == "O"):
     charge =  -0.7855 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.7855 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CHID"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.1739 
   elif (ATOM_NAME == "HA"):
     charge =   0.1100 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1046 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0565 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0565 
   elif (ATOM_NAME == "CG"):
     charge =   0.0293 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.3892 
   elif (ATOM_NAME == "HD1"):
     charge =   0.3755 
   elif (ATOM_NAME == "CE1"):
     charge =   0.1925 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1418 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.5629 
   elif (ATOM_NAME == "CD2"):
     charge =   0.1001 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1241 
   elif (ATOM_NAME == "C"):
     charge =   0.7615 
   elif (ATOM_NAME == "O"):
     charge =  -0.8016 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8016 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CHIE"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2699 
   elif (ATOM_NAME == "HA"):
     charge =   0.1650 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1068 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0620 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0620 
   elif (ATOM_NAME == "CG"):
     charge =   0.2724 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.5517 
   elif (ATOM_NAME == "CE1"):
     charge =   0.1558 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1448 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.2670 
   elif (ATOM_NAME == "HE2"):
     charge =   0.3319 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.2588 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1957 
   elif (ATOM_NAME == "C"):
     charge =   0.7916 
   elif (ATOM_NAME == "O"):
     charge =  -0.8065 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8065 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CHIP"):
   if (ATOM_NAME == "N"):
     charge =  -0.3481 
   elif (ATOM_NAME == "H"):
     charge =   0.2764 
   elif (ATOM_NAME == "CA"):
     charge =  -0.1445 
   elif (ATOM_NAME == "HA"):
     charge =   0.1115 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0800 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0868 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0868 
   elif (ATOM_NAME == "CG"):
     charge =   0.0298 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.1501 
   elif (ATOM_NAME == "HD1"):
     charge =   0.3883 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.0251 
   elif (ATOM_NAME == "HE1"):
     charge =   0.2694 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.1683 
   elif (ATOM_NAME == "HE2"):
     charge =   0.3913 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1256 
   elif (ATOM_NAME == "HD2"):
     charge =   0.2336 
   elif (ATOM_NAME == "C"):
     charge =   0.8032 
   elif (ATOM_NAME == "O"):
     charge =  -0.8177 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8177 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CILE"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.3100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1375 
   elif (ATOM_NAME == "CB"):
     charge =   0.0363 
   elif (ATOM_NAME == "HB"):
     charge =   0.0766 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.3498 
   elif (ATOM_NAME == "HG21"):
     charge =   0.1021 
   elif (ATOM_NAME == "HG22"):
     charge =   0.1021 
   elif (ATOM_NAME == "HG23"):
     charge =   0.1021 
   elif (ATOM_NAME == "CG1"):
     charge =  -0.0323 
   elif (ATOM_NAME == "HG12"):
     charge =   0.0321 
   elif (ATOM_NAME == "HG13"):
     charge =   0.0321 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.0699 
   elif (ATOM_NAME == "HD11"):
     charge =   0.0196 
   elif (ATOM_NAME == "HD12"):
     charge =   0.0196 
   elif (ATOM_NAME == "HD13"):
     charge =   0.0196 
   elif (ATOM_NAME == "C"):
     charge =   0.8343 
   elif (ATOM_NAME == "O"):
     charge =  -0.8190 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8190 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CLEU"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2847 
   elif (ATOM_NAME == "HA"):
     charge =   0.1346 
   elif (ATOM_NAME == "CB"):
     charge =  -0.2469 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0974 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0974 
   elif (ATOM_NAME == "CG"):
     charge =   0.3706 
   elif (ATOM_NAME == "HG"):
     charge =  -0.0374 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.4163 
   elif (ATOM_NAME == "HD11"):
     charge =   0.1038 
   elif (ATOM_NAME == "HD12"):
     charge =   0.1038 
   elif (ATOM_NAME == "HD13"):
     charge =   0.1038 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.4163 
   elif (ATOM_NAME == "HD21"):
     charge =   0.1038 
   elif (ATOM_NAME == "HD22"):
     charge =   0.1038 
   elif (ATOM_NAME == "HD23"):
     charge =   0.1038 
   elif (ATOM_NAME == "C"):
     charge =   0.8326 
   elif (ATOM_NAME == "O"):
     charge =  -0.8199 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8199 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CLYS"):
   if (ATOM_NAME == "N"):
     charge =  -0.3481 
   elif (ATOM_NAME == "H"):
     charge =   0.2764 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2903 
   elif (ATOM_NAME == "HA"):
     charge =   0.1438 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0538 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0482 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0482 
   elif (ATOM_NAME == "CG"):
     charge =   0.0227 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0134 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0134 
   elif (ATOM_NAME == "CD"):
     charge =  -0.0392 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0611 
   elif (ATOM_NAME == "HD3"):
     charge =   0.0611 
   elif (ATOM_NAME == "CE"):
     charge =  -0.0176 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1121 
   elif (ATOM_NAME == "HE3"):
     charge =   0.1121 
   elif (ATOM_NAME == "NZ"):
     charge =  -0.3741 
   elif (ATOM_NAME == "HZ1"):
     charge =   0.3374 
   elif (ATOM_NAME == "HZ2"):
     charge =   0.3374 
   elif (ATOM_NAME == "HZ3"):
     charge =   0.3374 
   elif (ATOM_NAME == "C"):
     charge =   0.8488 
   elif (ATOM_NAME == "O"):
     charge =  -0.8252 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8252 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CMET"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2597 
   elif (ATOM_NAME == "HA"):
     charge =   0.1277 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0236 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0480 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0480 
   elif (ATOM_NAME == "CG"):
     charge =   0.0492 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0317 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0317 
   elif (ATOM_NAME == "SD"):
     charge =  -0.2692 
   elif (ATOM_NAME == "CE"):
     charge =  -0.0376 
   elif (ATOM_NAME == "HE1"):
     charge =   0.0625 
   elif (ATOM_NAME == "HE2"):
     charge =   0.0625 
   elif (ATOM_NAME == "HE3"):
     charge =   0.0625 
   elif (ATOM_NAME == "C"):
     charge =   0.8013 
   elif (ATOM_NAME == "O"):
     charge =  -0.8105 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8105 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CPHE"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.1825 
   elif (ATOM_NAME == "HA"):
     charge =   0.1098 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0959 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0443 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0443 
   elif (ATOM_NAME == "CG"):
     charge =   0.0552 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1300 
   elif (ATOM_NAME == "HD1"):
     charge =   0.1408 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.1847 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1461 
   elif (ATOM_NAME == "CZ"):
     charge =  -0.0944 
   elif (ATOM_NAME == "HZ"):
     charge =   0.1280 
   elif (ATOM_NAME == "CE2"):
     charge =  -0.1847 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1461 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1300 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1408 
   elif (ATOM_NAME == "C"):
     charge =   0.7660 
   elif (ATOM_NAME == "O"):
     charge =  -0.8026 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8026 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CPRO"):
   if (ATOM_NAME == "N"):
     charge =  -0.2802 
   elif (ATOM_NAME == "CD"):
     charge =   0.0434 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0331 
   elif (ATOM_NAME == "HD3"):
     charge =   0.0331 
   elif (ATOM_NAME == "CG"):
     charge =   0.0466 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0172 
   elif (ATOM_NAME == "HG3"):
     charge =   0.0172 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0543 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0381 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0381 
   elif (ATOM_NAME == "CA"):
     charge =  -0.1336 
   elif (ATOM_NAME == "HA"):
     charge =   0.0776 
   elif (ATOM_NAME == "C"):
     charge =   0.6631 
   elif (ATOM_NAME == "O"):
     charge =  -0.7697 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.7697 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CSER"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2722 
   elif (ATOM_NAME == "HA"):
     charge =   0.1304 
   elif (ATOM_NAME == "CB"):
     charge =   0.1123 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0813 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0813 
   elif (ATOM_NAME == "OG"):
     charge =  -0.6514 
   elif (ATOM_NAME == "HG"):
     charge =   0.4474 
   elif (ATOM_NAME == "C"):
     charge =   0.8113 
   elif (ATOM_NAME == "O"):
     charge =  -0.8132 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8132 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CTHR"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2420 
   elif (ATOM_NAME == "HA"):
     charge =   0.1207 
   elif (ATOM_NAME == "CB"):
     charge =   0.3025 
   elif (ATOM_NAME == "HB"):
     charge =   0.0078 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.1853 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0586 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0586 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0586 
   elif (ATOM_NAME == "OG1"):
     charge =  -0.6496 
   elif (ATOM_NAME == "HG1"):
     charge =   0.4119 
   elif (ATOM_NAME == "C"):
     charge =   0.7810 
   elif (ATOM_NAME == "O"):
     charge =  -0.8044 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8044 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CTRP"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2084 
   elif (ATOM_NAME == "HA"):
     charge =   0.1272 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0742 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0497 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0497 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0796 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1808 
   elif (ATOM_NAME == "HD1"):
     charge =   0.2043 
   elif (ATOM_NAME == "NE1"):
     charge =  -0.3316 
   elif (ATOM_NAME == "HE1"):
     charge =   0.3413 
   elif (ATOM_NAME == "CE2"):
     charge =   0.1222 
   elif (ATOM_NAME == "CZ2"):
     charge =  -0.2594 
   elif (ATOM_NAME == "HZ2"):
     charge =   0.1567 
   elif (ATOM_NAME == "CH2"):
     charge =  -0.1020 
   elif (ATOM_NAME == "HH2"):
     charge =   0.1401 
   elif (ATOM_NAME == "CZ3"):
     charge =  -0.2287 
   elif (ATOM_NAME == "HZ3"):
     charge =   0.1507 
   elif (ATOM_NAME == "CE3"):
     charge =  -0.1837 
   elif (ATOM_NAME == "HE3"):
     charge =   0.1491 
   elif (ATOM_NAME == "CD2"):
     charge =   0.1078 
   elif (ATOM_NAME == "C"):
     charge =   0.7658 
   elif (ATOM_NAME == "O"):
     charge =  -0.8011 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8011 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CTYR"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.2015 
   elif (ATOM_NAME == "HA"):
     charge =   0.1092 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0752 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0490 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0490 
   elif (ATOM_NAME == "CG"):
     charge =   0.0243 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1922 
   elif (ATOM_NAME == "HD1"):
     charge =   0.1780 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.2458 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1673 
   elif (ATOM_NAME == "CZ"):
     charge =   0.3395 
   elif (ATOM_NAME == "OH"):
     charge =  -0.5643 
   elif (ATOM_NAME == "HH"):
     charge =   0.4017 
   elif (ATOM_NAME == "CE2"):
     charge =  -0.2458 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1673 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1922 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1780 
   elif (ATOM_NAME == "C"):
     charge =   0.7817 
   elif (ATOM_NAME == "O"):
     charge =  -0.8070 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8070 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CVAL"):
   if (ATOM_NAME == "N"):
     charge =  -0.3821 
   elif (ATOM_NAME == "H"):
     charge =   0.2681 
   elif (ATOM_NAME == "CA"):
     charge =  -0.3438 
   elif (ATOM_NAME == "HA"):
     charge =   0.1438 
   elif (ATOM_NAME == "CB"):
     charge =   0.1940 
   elif (ATOM_NAME == "HB"):
     charge =   0.0308 
   elif (ATOM_NAME == "CG1"):
     charge =  -0.3064 
   elif (ATOM_NAME == "HG11"):
     charge =   0.0836 
   elif (ATOM_NAME == "HG12"):
     charge =   0.0836 
   elif (ATOM_NAME == "HG13"):
     charge =   0.0836 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.3064 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0836 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0836 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0836 
   elif (ATOM_NAME == "C"):
     charge =   0.8350 
   elif (ATOM_NAME == "O"):
     charge =  -0.8173 
   elif (ATOM_NAME == "OXT"):
     charge =  -0.8173 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NHE"):
   if (ATOM_NAME == "N"):
     charge =  -0.4630 
   elif (ATOM_NAME == "HN1"):
     charge =   0.2315 
   elif (ATOM_NAME == "HN2"):
     charge =   0.2315 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "NME"):
   if (ATOM_NAME == "N"):
     charge =  -0.4157 
   elif (ATOM_NAME == "H"):
     charge =   0.2719 
   elif (ATOM_NAME == "CH3"):
     charge =  -0.1490 
   elif (ATOM_NAME == "HH31"):
     charge =   0.0976 
   elif (ATOM_NAME == "HH32"):
     charge =   0.0976 
   elif (ATOM_NAME == "HH33"):
     charge =   0.0976 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 else:
   print ("THE RESIDUE %s IS WRONG" %(RES_NAME)) 
 try:
  return charge
 except:
    library_warning_message()

