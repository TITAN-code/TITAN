#!/usr/bin/python
# calc_EF_resid_charmm.py
# Author: Jing Huang; Date: July 24, 2016

def charmm_charge_resid(ATOM_NAME,RES_NAME):
 if (RES_NAME == "ALA"): 
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ARG"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =   0.2000 
   elif (ATOM_NAME == "HD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "NE"):
     charge =  -0.7000 
   elif (ATOM_NAME == "HE"):
     charge =   0.4400 
   elif (ATOM_NAME == "CZ"):
     charge =   0.6400 
   elif (ATOM_NAME == "NH1"):
     charge =  -0.8000 
   elif (ATOM_NAME == "HH11"):
     charge =   0.4600 
   elif (ATOM_NAME == "HH12"):
     charge =   0.4600 
   elif (ATOM_NAME == "NH2"):
     charge =  -0.8000 
   elif (ATOM_NAME == "HH21"):
     charge =   0.4600 
   elif (ATOM_NAME == "HH22"):
     charge =   0.4600 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ASN"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =   0.5500 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.5500 
   elif (ATOM_NAME == "ND2"):
     charge =  -0.6200 
   elif (ATOM_NAME == "HD21"):
     charge =   0.3200 
   elif (ATOM_NAME == "HD22"):
     charge =   0.3000 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ASP"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.2800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =   0.6200 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.7600 
   elif (ATOM_NAME == "OD2"):
     charge =  -0.7600 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CYS"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1100 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "SG"):
     charge =  -0.2300 
   elif (ATOM_NAME == "HG1"):
     charge =   0.1600 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLN"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =   0.5500 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.5500 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.6200 
   elif (ATOM_NAME == "HE21"):
     charge =   0.3200 
   elif (ATOM_NAME == "HE22"):
     charge =   0.3000 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLU"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.2800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =   0.6200 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.7600 
   elif (ATOM_NAME == "OE2"):
     charge =  -0.7600 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLY"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0200 
   elif (ATOM_NAME == "HA1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HA2"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "HSD"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0900 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.3600 
   elif (ATOM_NAME == "HD1"):
     charge =   0.3200 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0500 
   elif (ATOM_NAME == "CE1"):
     charge =   0.2500 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1300 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.7000 
   elif (ATOM_NAME == "CD2"):
     charge =   0.2200 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1000 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "HSE"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.7000 
   elif (ATOM_NAME == "CG"):
     charge =   0.2200 
   elif (ATOM_NAME == "CE1"):
     charge =   0.2500 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1300 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.3600 
   elif (ATOM_NAME == "HE2"):
     charge =   0.3200 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.0500 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "HSP"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0500 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD2"):
     charge =   0.1900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1300 
   elif (ATOM_NAME == "CG"):
     charge =   0.1900 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.5100 
   elif (ATOM_NAME == "HE2"):
     charge =   0.4400 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.5100 
   elif (ATOM_NAME == "HD1"):
     charge =   0.4400 
   elif (ATOM_NAME == "CE1"):
     charge =   0.3200 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1800 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ILE"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0900 
   elif (ATOM_NAME == "HB"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG1"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG11"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG12"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD3"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "LEU"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0900 
   elif (ATOM_NAME == "HG"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HD11"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD12"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD13"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HD21"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD22"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD23"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "LYS"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CE"):
     charge =   0.2100 
   elif (ATOM_NAME == "HE1"):
     charge =   0.0500 
   elif (ATOM_NAME == "HE2"):
     charge =   0.0500 
   elif (ATOM_NAME == "NZ"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HZ1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HZ2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HZ3"):
     charge =   0.3300 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "MET"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1400 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "SD"):
     charge =  -0.0900 
   elif (ATOM_NAME == "CE"):
     charge =  -0.2200 
   elif (ATOM_NAME == "HE1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HE2"):
     charge =   0.0900 
   elif (ATOM_NAME == "HE3"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "PHE"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =   0.0000 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HD1"):
     charge =   0.1150 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1150 
   elif (ATOM_NAME == "CZ"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HZ"):
     charge =   0.1150 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1150 
   elif (ATOM_NAME == "CE2"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1150 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "PRO"):
   if (ATOM_NAME == "N"):
     charge =  -0.2900 
   elif (ATOM_NAME == "CD"):
     charge =   0.0000 
   elif (ATOM_NAME == "HD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CA"):
     charge =   0.0200 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "SER"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =   0.0500 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "OG"):
     charge =  -0.6600 
   elif (ATOM_NAME == "HG1"):
     charge =   0.4300 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "THR"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =   0.1400 
   elif (ATOM_NAME == "HB"):
     charge =   0.0900 
   elif (ATOM_NAME == "OG1"):
     charge =  -0.6600 
   elif (ATOM_NAME == "HG1"):
     charge =   0.4300 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "TRP"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0300 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1500 
   elif (ATOM_NAME == "HD1"):
     charge =   0.2200 
   elif (ATOM_NAME == "NE1"):
     charge =  -0.5100 
   elif (ATOM_NAME == "HE1"):
     charge =   0.3700 
   elif (ATOM_NAME == "CE2"):
     charge =   0.2400 
   elif (ATOM_NAME == "CD2"):
     charge =   0.1100 
   elif (ATOM_NAME == "CE3"):
     charge =  -0.2500 
   elif (ATOM_NAME == "HE3"):
     charge =   0.1700 
   elif (ATOM_NAME == "CZ3"):
     charge =  -0.2000 
   elif (ATOM_NAME == "HZ3"):
     charge =   0.1400 
   elif (ATOM_NAME == "CZ2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HZ2"):
     charge =   0.1600 
   elif (ATOM_NAME == "CH2"):
     charge =  -0.1400 
   elif (ATOM_NAME == "HH2"):
     charge =   0.1400 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "TYR"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =   0.0000 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HD1"):
     charge =   0.1150 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1150 
   elif (ATOM_NAME == "CZ"):
     charge =   0.1100 
   elif (ATOM_NAME == "OH"):
     charge =  -0.5400 
   elif (ATOM_NAME == "HH"):
     charge =   0.4300 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1150 
   elif (ATOM_NAME == "CE2"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1150 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "VAL"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0900 
   elif (ATOM_NAME == "HB"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG1"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HG11"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG12"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG13"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "TIP3"):
   if (ATOM_NAME == "OH2"):
     charge =  -0.8340 
   elif (ATOM_NAME == "H1"):
     charge =   0.4170 
   elif (ATOM_NAME == "H2"):
     charge =   0.4170 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ASPP"):
   if (ATOM_NAME == "CB"):
     charge =  -0.2100 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =   0.7500 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.5500 
   elif (ATOM_NAME == "OD2"):
     charge =  -0.6100 
   elif (ATOM_NAME == "HD2"):
     charge =   0.4400 
   elif (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLUP"):
   if (ATOM_NAME == "CG"):
     charge =  -0.2100 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =   0.7500 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.5500 
   elif (ATOM_NAME == "OE2"):
     charge =  -0.6100 
   elif (ATOM_NAME == "HE2"):
     charge =   0.4400 
   elif (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "DISU"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1000 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "SG"):
     charge =  -0.0800 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "TAUR"):
   if (ATOM_NAME == "C1"):
     charge =   0.1600 
   elif (ATOM_NAME == "H1"):
     charge =   0.0400 
   elif (ATOM_NAME == "H2"):
     charge =   0.0400 
   elif (ATOM_NAME == "C2"):
     charge =  -0.3500 
   elif (ATOM_NAME == "H3"):
     charge =   0.0900 
   elif (ATOM_NAME == "H4"):
     charge =   0.0900 
   elif (ATOM_NAME == "N1"):
     charge =  -0.3400 
   elif (ATOM_NAME == "H5"):
     charge =   0.3200 
   elif (ATOM_NAME == "H6"):
     charge =   0.3200 
   elif (ATOM_NAME == "H7"):
     charge =   0.3200 
   elif (ATOM_NAME == "S1"):
     charge =   1.3200 
   elif (ATOM_NAME == "O1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "O2"):
     charge =  -0.6700 
   elif (ATOM_NAME == "O3"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "HEMI"):
   if (ATOM_NAME == "OX"):
     charge =  -0.3200 
   elif (ATOM_NAME == "FE"):
     charge =   0.5600 
   elif (ATOM_NAME == "NA"):
     charge =  -0.1800 
   elif (ATOM_NAME == "NB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "NC"):
     charge =  -0.1800 
   elif (ATOM_NAME == "ND"):
     charge =  -0.1800 
   elif (ATOM_NAME == "C1A"):
     charge =   0.1200 
   elif (ATOM_NAME == "C2A"):
     charge =  -0.0600 
   elif (ATOM_NAME == "C3A"):
     charge =  -0.0600 
   elif (ATOM_NAME == "C4A"):
     charge =   0.1200 
   elif (ATOM_NAME == "C1B"):
     charge =   0.1200 
   elif (ATOM_NAME == "C2B"):
     charge =  -0.0600 
   elif (ATOM_NAME == "C3B"):
     charge =  -0.0600 
   elif (ATOM_NAME == "C4B"):
     charge =   0.1200 
   elif (ATOM_NAME == "C1C"):
     charge =   0.1200 
   elif (ATOM_NAME == "C2C"):
     charge =  -0.0600 
   elif (ATOM_NAME == "C3C"):
     charge =  -0.0600 
   elif (ATOM_NAME == "C4C"):
     charge =   0.1200 
   elif (ATOM_NAME == "C1D"):
     charge =   0.1200 
   elif (ATOM_NAME == "C2D"):
     charge =  -0.0600 
   elif (ATOM_NAME == "C3D"):
     charge =  -0.0600 
   elif (ATOM_NAME == "C4D"):
     charge =   0.1200 
   elif (ATOM_NAME == "CHA"):
     charge =  -0.1000 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CHB"):
     charge =  -0.1000 
   elif (ATOM_NAME == "HB"):
     charge =   0.1000 
   elif (ATOM_NAME == "CHC"):
     charge =  -0.1000 
   elif (ATOM_NAME == "HC"):
     charge =   0.1000 
   elif (ATOM_NAME == "CHD"):
     charge =  -0.1000 
   elif (ATOM_NAME == "HD"):
     charge =   0.1000 
   elif (ATOM_NAME == "CMA"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HMA1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HMA2"):
     charge =   0.0900 
   elif (ATOM_NAME == "HMA3"):
     charge =   0.0900 
   elif (ATOM_NAME == "CAA"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HAA1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HAA2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CBA"):
     charge =  -0.2800 
   elif (ATOM_NAME == "HBA1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HBA2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CGA"):
     charge =   0.6200 
   elif (ATOM_NAME == "O1A"):
     charge =  -0.7600 
   elif (ATOM_NAME == "O2A"):
     charge =  -0.7600 
   elif (ATOM_NAME == "CMB"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HMB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HMB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "HMB3"):
     charge =   0.0900 
   elif (ATOM_NAME == "CAB"):
     charge =  -0.1500 
   elif (ATOM_NAME == "HAB"):
     charge =   0.1500 
   elif (ATOM_NAME == "CBB"):
     charge =  -0.4200 
   elif (ATOM_NAME == "HBB1"):
     charge =   0.2100 
   elif (ATOM_NAME == "HBB2"):
     charge =   0.2100 
   elif (ATOM_NAME == "CMC"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HMC1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HMC2"):
     charge =   0.0900 
   elif (ATOM_NAME == "HMC3"):
     charge =   0.0900 
   elif (ATOM_NAME == "CAC"):
     charge =  -0.1500 
   elif (ATOM_NAME == "HAC"):
     charge =   0.1500 
   elif (ATOM_NAME == "CBC"):
     charge =  -0.4200 
   elif (ATOM_NAME == "HBC1"):
     charge =   0.2100 
   elif (ATOM_NAME == "HBC2"):
     charge =   0.2100 
   elif (ATOM_NAME == "CMD"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HMD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HMD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "HMD3"):
     charge =   0.0900 
   elif (ATOM_NAME == "CAD"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HAD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HAD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CBD"):
     charge =  -0.2800 
   elif (ATOM_NAME == "HBD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HBD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CGD"):
     charge =   0.6200 
   elif (ATOM_NAME == "O1D"):
     charge =  -0.7600 
   elif (ATOM_NAME == "O2D"):
     charge =  -0.7600 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "DCR"):
   if (ATOM_NAME == "C1"):
     charge =   0.5200 
   elif (ATOM_NAME == "O2"):
     charge =  -0.7600 
   elif (ATOM_NAME == "O3"):
     charge =  -0.7600 
   elif (ATOM_NAME == "C4"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H5"):
     charge =   0.0900 
   elif (ATOM_NAME == "H6"):
     charge =   0.0900 
   elif (ATOM_NAME == "C7"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H8"):
     charge =   0.0900 
   elif (ATOM_NAME == "H9"):
     charge =   0.0900 
   elif (ATOM_NAME == "C10"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H11"):
     charge =   0.0900 
   elif (ATOM_NAME == "H12"):
     charge =   0.0900 
   elif (ATOM_NAME == "C13"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H14"):
     charge =   0.0900 
   elif (ATOM_NAME == "H15"):
     charge =   0.0900 
   elif (ATOM_NAME == "C16"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H17"):
     charge =   0.0900 
   elif (ATOM_NAME == "H18"):
     charge =   0.0900 
   elif (ATOM_NAME == "C19"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H20"):
     charge =   0.0900 
   elif (ATOM_NAME == "H21"):
     charge =   0.0900 
   elif (ATOM_NAME == "C22"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H23"):
     charge =   0.0900 
   elif (ATOM_NAME == "H24"):
     charge =   0.0900 
   elif (ATOM_NAME == "C25"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H26"):
     charge =   0.0900 
   elif (ATOM_NAME == "H27"):
     charge =   0.0900 
   elif (ATOM_NAME == "C28"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H29"):
     charge =   0.0900 
   elif (ATOM_NAME == "H30"):
     charge =   0.0900 
   elif (ATOM_NAME == "C31"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H32"):
     charge =   0.0900 
   elif (ATOM_NAME == "H33"):
     charge =   0.0900 
   elif (ATOM_NAME == "C34"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H35"):
     charge =   0.0900 
   elif (ATOM_NAME == "H36"):
     charge =   0.0900 
   elif (ATOM_NAME == "C37"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H38"):
     charge =   0.0900 
   elif (ATOM_NAME == "H39"):
     charge =   0.0900 
   elif (ATOM_NAME == "C40"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H41"):
     charge =   0.0900 
   elif (ATOM_NAME == "H42"):
     charge =   0.0900 
   elif (ATOM_NAME == "C43"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H44"):
     charge =   0.0900 
   elif (ATOM_NAME == "H45"):
     charge =   0.0900 
   elif (ATOM_NAME == "C46"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H47"):
     charge =   0.0900 
   elif (ATOM_NAME == "H48"):
     charge =   0.0900 
   elif (ATOM_NAME == "C49"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H50"):
     charge =   0.0900 
   elif (ATOM_NAME == "H51"):
     charge =   0.0900 
   elif (ATOM_NAME == "C52"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H53"):
     charge =   0.0900 
   elif (ATOM_NAME == "H54"):
     charge =   0.0900 
   elif (ATOM_NAME == "C55"):
     charge =  -0.1800 
   elif (ATOM_NAME == "H56"):
     charge =   0.0900 
   elif (ATOM_NAME == "H57"):
     charge =   0.0900 
   elif (ATOM_NAME == "C58"):
     charge =  -0.2700 
   elif (ATOM_NAME == "H59"):
     charge =   0.0900 
   elif (ATOM_NAME == "H60"):
     charge =   0.0900 
   elif (ATOM_NAME == "H61"):
     charge =   0.0900 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 else:
   print ("THE RESIDUE %s IS WRONG" %(RES_NAME)) 
 return charge
def N_terminal_charge(ATOM_NAME,RES_NAME):
 if (RES_NAME == "ALAN"): 
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ARGN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =   0.2000 
   elif (ATOM_NAME == "HD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "NE"):
     charge =  -0.7000 
   elif (ATOM_NAME == "HE"):
     charge =   0.4400 
   elif (ATOM_NAME == "CZ"):
     charge =   0.6400 
   elif (ATOM_NAME == "NH1"):
     charge =  -0.8000 
   elif (ATOM_NAME == "HH11"):
     charge =   0.4600 
   elif (ATOM_NAME == "HH12"):
     charge =   0.4600 
   elif (ATOM_NAME == "NH2"):
     charge =  -0.8000 
   elif (ATOM_NAME == "HH21"):
     charge =   0.4600 
   elif (ATOM_NAME == "HH22"):
     charge =   0.4600 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ASNN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =   0.5500 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.5500 
   elif (ATOM_NAME == "ND2"):
     charge =  -0.6200 
   elif (ATOM_NAME == "HD21"):
     charge =   0.3200 
   elif (ATOM_NAME == "HD22"):
     charge =   0.3000 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ASPN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.2800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =   0.6200 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.7600 
   elif (ATOM_NAME == "OD2"):
     charge =  -0.7600 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CYSN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1100 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "SG"):
     charge =  -0.2300 
   elif (ATOM_NAME == "HG1"):
     charge =   0.1600 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLNN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =   0.5500 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.5500 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.6200 
   elif (ATOM_NAME == "HE21"):
     charge =   0.3200 
   elif (ATOM_NAME == "HE22"):
     charge =   0.3000 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLUN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.2800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =   0.6200 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.7600 
   elif (ATOM_NAME == "OE2"):
     charge =  -0.7600 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLYN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.1300 
   elif (ATOM_NAME == "HA1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HA2"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "HSDN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0900 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.3600 
   elif (ATOM_NAME == "HD1"):
     charge =   0.3200 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0500 
   elif (ATOM_NAME == "CE1"):
     charge =   0.2500 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1300 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.7000 
   elif (ATOM_NAME == "CD2"):
     charge =   0.2200 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1000 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "HSEN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.7000 
   elif (ATOM_NAME == "CG"):
     charge =   0.2200 
   elif (ATOM_NAME == "CE1"):
     charge =   0.2500 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1300 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.3600 
   elif (ATOM_NAME == "HE2"):
     charge =   0.3200 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.0500 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "HSPN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0500 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD2"):
     charge =   0.1900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1300 
   elif (ATOM_NAME == "CG"):
     charge =   0.1900 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.5100 
   elif (ATOM_NAME == "HE2"):
     charge =   0.4400 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.5100 
   elif (ATOM_NAME == "HD1"):
     charge =   0.4400 
   elif (ATOM_NAME == "CE1"):
     charge =   0.3200 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1800 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ILEN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0900 
   elif (ATOM_NAME == "HB"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG1"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG11"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG12"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD3"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "LEUN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0900 
   elif (ATOM_NAME == "HG"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HD11"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD12"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD13"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HD21"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD22"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD23"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "LYSN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CE"):
     charge =   0.2100 
   elif (ATOM_NAME == "HE1"):
     charge =   0.0500 
   elif (ATOM_NAME == "HE2"):
     charge =   0.0500 
   elif (ATOM_NAME == "NZ"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HZ1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HZ2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HZ3"):
     charge =   0.3300 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "METN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1400 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "SD"):
     charge =  -0.0900 
   elif (ATOM_NAME == "CE"):
     charge =  -0.2200 
   elif (ATOM_NAME == "HE1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HE2"):
     charge =   0.0900 
   elif (ATOM_NAME == "HE3"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "PHEN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =   0.0000 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HD1"):
     charge =   0.1150 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1150 
   elif (ATOM_NAME == "CZ"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HZ"):
     charge =   0.1150 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1150 
   elif (ATOM_NAME == "CE2"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1150 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "PRON"):
   if (ATOM_NAME == "N"):
     charge =  -0.0700 
   elif (ATOM_NAME == "HN1"):
     charge =   0.2400 
   elif (ATOM_NAME == "HN2"):
     charge =   0.2400 
   elif (ATOM_NAME == "CD"):
     charge =   0.1600 
   elif (ATOM_NAME == "HD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CA"):
     charge =   0.1600 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "SERN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =   0.0500 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "OG"):
     charge =  -0.6600 
   elif (ATOM_NAME == "HG1"):
     charge =   0.4300 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "THRN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =   0.1400 
   elif (ATOM_NAME == "HB"):
     charge =   0.0900 
   elif (ATOM_NAME == "OG1"):
     charge =  -0.6600 
   elif (ATOM_NAME == "HG1"):
     charge =   0.4300 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "TRPN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0300 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1500 
   elif (ATOM_NAME == "HD1"):
     charge =   0.2200 
   elif (ATOM_NAME == "NE1"):
     charge =  -0.5100 
   elif (ATOM_NAME == "HE1"):
     charge =   0.3700 
   elif (ATOM_NAME == "CE2"):
     charge =   0.2400 
   elif (ATOM_NAME == "CD2"):
     charge =   0.1100 
   elif (ATOM_NAME == "CE3"):
     charge =  -0.2500 
   elif (ATOM_NAME == "HE3"):
     charge =   0.1700 
   elif (ATOM_NAME == "CZ3"):
     charge =  -0.2000 
   elif (ATOM_NAME == "HZ3"):
     charge =   0.1400 
   elif (ATOM_NAME == "CZ2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HZ2"):
     charge =   0.1600 
   elif (ATOM_NAME == "CH2"):
     charge =  -0.1400 
   elif (ATOM_NAME == "HH2"):
     charge =   0.1400 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "TYRN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =   0.0000 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HD1"):
     charge =   0.1150 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1150 
   elif (ATOM_NAME == "CZ"):
     charge =   0.1100 
   elif (ATOM_NAME == "OH"):
     charge =  -0.5400 
   elif (ATOM_NAME == "HH"):
     charge =   0.4300 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1150 
   elif (ATOM_NAME == "CE2"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1150 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "VALN"):
   if (ATOM_NAME == "N"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HT1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HT3"):
     charge =   0.3300 
   elif (ATOM_NAME == "CA"):
     charge =   0.2100 
   elif (ATOM_NAME == "HA"):
     charge =   0.1000 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0900 
   elif (ATOM_NAME == "HB"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG1"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HG11"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG12"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG13"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.5100 
   elif (ATOM_NAME == "O"):
     charge =  -0.5100 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 else:
   print ("THE RESIDUE %s IS WRONG" %(RES_NAME)) 
 return charge
def C_terminal_charge(ATOM_NAME,RES_NAME):
 if (RES_NAME == "ALAC"): 
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB3"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ARGC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =   0.2000 
   elif (ATOM_NAME == "HD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "NE"):
     charge =  -0.7000 
   elif (ATOM_NAME == "HE"):
     charge =   0.4400 
   elif (ATOM_NAME == "CZ"):
     charge =   0.6400 
   elif (ATOM_NAME == "NH1"):
     charge =  -0.8000 
   elif (ATOM_NAME == "HH11"):
     charge =   0.4600 
   elif (ATOM_NAME == "HH12"):
     charge =   0.4600 
   elif (ATOM_NAME == "NH2"):
     charge =  -0.8000 
   elif (ATOM_NAME == "HH21"):
     charge =   0.4600 
   elif (ATOM_NAME == "HH22"):
     charge =   0.4600 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ASNC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =   0.5500 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.5500 
   elif (ATOM_NAME == "ND2"):
     charge =  -0.6200 
   elif (ATOM_NAME == "HD21"):
     charge =   0.3200 
   elif (ATOM_NAME == "HD22"):
     charge =   0.3000 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ASPC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.2800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =   0.6200 
   elif (ATOM_NAME == "OD1"):
     charge =  -0.7600 
   elif (ATOM_NAME == "OD2"):
     charge =  -0.7600 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "CYSC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1100 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "SG"):
     charge =  -0.2300 
   elif (ATOM_NAME == "HG1"):
     charge =   0.1600 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLNC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =   0.5500 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.5500 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.6200 
   elif (ATOM_NAME == "HE21"):
     charge =   0.3200 
   elif (ATOM_NAME == "HE22"):
     charge =   0.3000 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLUC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.2800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =   0.6200 
   elif (ATOM_NAME == "OE1"):
     charge =  -0.7600 
   elif (ATOM_NAME == "OE2"):
     charge =  -0.7600 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "GLYC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =  -0.0200 
   elif (ATOM_NAME == "HA1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HA2"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "HSDC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0900 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.3600 
   elif (ATOM_NAME == "HD1"):
     charge =   0.3200 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0500 
   elif (ATOM_NAME == "CE1"):
     charge =   0.2500 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1300 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.7000 
   elif (ATOM_NAME == "CD2"):
     charge =   0.2200 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1000 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "HSEC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.7000 
   elif (ATOM_NAME == "CG"):
     charge =   0.2200 
   elif (ATOM_NAME == "CE1"):
     charge =   0.2500 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1300 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.3600 
   elif (ATOM_NAME == "HE2"):
     charge =   0.3200 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.0500 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "HSPC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0500 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD2"):
     charge =   0.1900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1300 
   elif (ATOM_NAME == "CG"):
     charge =   0.1900 
   elif (ATOM_NAME == "NE2"):
     charge =  -0.5100 
   elif (ATOM_NAME == "HE2"):
     charge =   0.4400 
   elif (ATOM_NAME == "ND1"):
     charge =  -0.5100 
   elif (ATOM_NAME == "HD1"):
     charge =   0.4400 
   elif (ATOM_NAME == "CE1"):
     charge =   0.3200 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1800 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "ILEC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0900 
   elif (ATOM_NAME == "HB"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG1"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG11"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG12"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD3"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "LEUC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0900 
   elif (ATOM_NAME == "HG"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HD11"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD12"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD13"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HD21"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD22"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD23"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "LYSC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CD"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CE"):
     charge =   0.2100 
   elif (ATOM_NAME == "HE1"):
     charge =   0.0500 
   elif (ATOM_NAME == "HE2"):
     charge =   0.0500 
   elif (ATOM_NAME == "NZ"):
     charge =  -0.3000 
   elif (ATOM_NAME == "HZ1"):
     charge =   0.3300 
   elif (ATOM_NAME == "HZ2"):
     charge =   0.3300 
   elif (ATOM_NAME == "HZ3"):
     charge =   0.3300 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "METC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1400 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "SD"):
     charge =  -0.0900 
   elif (ATOM_NAME == "CE"):
     charge =  -0.2200 
   elif (ATOM_NAME == "HE1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HE2"):
     charge =   0.0900 
   elif (ATOM_NAME == "HE3"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "PHEC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =   0.0000 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HD1"):
     charge =   0.1150 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1150 
   elif (ATOM_NAME == "CZ"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HZ"):
     charge =   0.1150 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1150 
   elif (ATOM_NAME == "CE2"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1150 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "PROC"):
   if (ATOM_NAME == "N"):
     charge =  -0.2900 
   elif (ATOM_NAME == "CD"):
     charge =   0.0000 
   elif (ATOM_NAME == "HD1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HD2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CA"):
     charge =   0.0200 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HG1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG2"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "SERC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =   0.0500 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "OG"):
     charge =  -0.6600 
   elif (ATOM_NAME == "HG1"):
     charge =   0.4300 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "THRC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =   0.1400 
   elif (ATOM_NAME == "HB"):
     charge =   0.0900 
   elif (ATOM_NAME == "OG1"):
     charge =  -0.6600 
   elif (ATOM_NAME == "HG1"):
     charge =   0.4300 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "TRPC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =  -0.0300 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1500 
   elif (ATOM_NAME == "HD1"):
     charge =   0.2200 
   elif (ATOM_NAME == "NE1"):
     charge =  -0.5100 
   elif (ATOM_NAME == "HE1"):
     charge =   0.3700 
   elif (ATOM_NAME == "CE2"):
     charge =   0.2400 
   elif (ATOM_NAME == "CD2"):
     charge =   0.1100 
   elif (ATOM_NAME == "CE3"):
     charge =  -0.2500 
   elif (ATOM_NAME == "HE3"):
     charge =   0.1700 
   elif (ATOM_NAME == "CZ3"):
     charge =  -0.2000 
   elif (ATOM_NAME == "HZ3"):
     charge =   0.1400 
   elif (ATOM_NAME == "CZ2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HZ2"):
     charge =   0.1600 
   elif (ATOM_NAME == "CH2"):
     charge =  -0.1400 
   elif (ATOM_NAME == "HH2"):
     charge =   0.1400 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "TYRC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.1800 
   elif (ATOM_NAME == "HB1"):
     charge =   0.0900 
   elif (ATOM_NAME == "HB2"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG"):
     charge =   0.0000 
   elif (ATOM_NAME == "CD1"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HD1"):
     charge =   0.1150 
   elif (ATOM_NAME == "CE1"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HE1"):
     charge =   0.1150 
   elif (ATOM_NAME == "CZ"):
     charge =   0.1100 
   elif (ATOM_NAME == "OH"):
     charge =  -0.5400 
   elif (ATOM_NAME == "HH"):
     charge =   0.4300 
   elif (ATOM_NAME == "CD2"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HD2"):
     charge =   0.1150 
   elif (ATOM_NAME == "CE2"):
     charge =  -0.1150 
   elif (ATOM_NAME == "HE2"):
     charge =   0.1150 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 elif (RES_NAME == "VALC"):
   if (ATOM_NAME == "N"):
     charge =  -0.4700 
   elif (ATOM_NAME == "HN"):
     charge =   0.3100 
   elif (ATOM_NAME == "CA"):
     charge =   0.0700 
   elif (ATOM_NAME == "HA"):
     charge =   0.0900 
   elif (ATOM_NAME == "CB"):
     charge =  -0.0900 
   elif (ATOM_NAME == "HB"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG1"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HG11"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG12"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG13"):
     charge =   0.0900 
   elif (ATOM_NAME == "CG2"):
     charge =  -0.2700 
   elif (ATOM_NAME == "HG21"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG22"):
     charge =   0.0900 
   elif (ATOM_NAME == "HG23"):
     charge =   0.0900 
   elif (ATOM_NAME == "C"):
     charge =   0.3400 
   elif (ATOM_NAME == "OT1"):
     charge =  -0.6700 
   elif (ATOM_NAME == "OT2"):
     charge =  -0.6700 
   else: 
     print ("THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s." %(ATOM_NAME,RES_NAME)) 
 else:
   print ("THE RESIDUE %s IS WRONG" %(RES_NAME)) 
 return charge

