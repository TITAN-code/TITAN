#!/usr/bin/python
# script_generate.py
# Author: Jing Huang; Date: AUG 5, 2016
#
import math,os,stat

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

def typeread(x):
    y = x
    return y

def header_command_line():
    print ("                                                                 ")
    print ("  ****************************************************************** ")
    print ("  *                                                                * ")
    print ("  *                    TITAN - VERSION 1.1                         * ")
    print ("  *                                                                * ")
    print ("  *           FROM THE HEBREW UNIVERISTY OF JERUSALEM              * ")
    print ("  *            JING HUANG, THIJS STUYVER, SASON SHAIK              * ")
    print ("  *              J. COMPUT. CHEM. X, XXX-XXX (2019)                * ")
    print ("  *                                                                * ")
    print ("  ****************************************************************** ")
    print ("                                                                 ")
    print ("                    CHARMM LIBRARY GENERATION                    ")
    print ("                                                                 ")

#_____________________________________________________________________________________

header_command_line()

# NON-STANDARD RESIDUE CAN BE ADDED INTO "top_protein.txt" WITH THE CHARGE SECTION FROM CHARMM-TYPE TOPOLOGICAL FILE.
# FOR EXAMPLE: 
#  RESI TAUR         +0.000 ! type from CHARMM
#  ATOM   C1  CT2     +0.160  ! type from CHARMM
#  ATOM   H1   HB     +0.040  ! type from CHARMM
#  ATOM   H2   HB     +0.040  ! type from CHARMM
#  ATOM   C2  CT2     -0.350  ! type from CHARMM
#  ATOM   H3   HB     +0.090  ! type from CHARMM
#  ATOM   H4   HB     +0.090  ! type from CHARMM
#  ATOM   N1  NH2     -0.340  ! type from CHARMM
#  ATOM   H5   HC     +0.320  ! type from CHARMM
#  ATOM   H6   HC     +0.320  ! type from CHARMM
#  ATOM   H7   HC     +0.320  ! type from CHARMM
#  ATOM   S1   SO     +1.320  ! type from CHARMM
#  ATOM   O1  OSS     -0.670  ! type from CHARMM
#  ATOM   O2  OSS     -0.670  ! type from CHARMM
#  ATOM   O3  OSS     -0.670  ! type from CHARMM
#
TOP_FILE = "top_protein.txt"

f2_top = open("library_charmm_new.py", "w")
print >> f2_top, ("#!/usr/bin/python")
print >> f2_top,(" ")
print >> f2_top,(" ")
print >> f2_top,("import sys ")
print >> f2_top,("import datetime ")
print >> f2_top,(" ")
print >> f2_top,("def library_warning_message():")
print >> f2_top,("    \"\"\" Message shown in the terminal in case the assignment of a point charge to an atom was not succesfull \"\"\"")
print >> f2_top,("    print (\"AN ERROR HAS OCCURED!\")")
print >> f2_top,("    print (\" \")")
print >> f2_top,("    print (\"PLEASE CONFIRM THE CORRECT ASSIGNMENT OF N_TERMINAL & C_TERMINAL IN THE INPUT FILE\")")
print >> f2_top,("    print (\" \")")
print >> f2_top,("    print (\"OTHERWISE:\")")
print >> f2_top,("    print (\" \")")
print >> f2_top,("    print (\"THE ERROR IS MOST LIKELY DUE TO THE PRESENCE OF NON-STANDARD RESIDUES IN THE .pdb-FILE.\")")
print >> f2_top,("    print (\"CONSIDER COMPILING AN ALTERNATIVE AMBER-LIBRARY WITH THE NON-STANDARD RESIDUES INCLUDED.\")")
print >> f2_top,("    print (\" ----- ERROR TERMINATION OF TITAN AT \" + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + \" -----\") ")
print >> f2_top,("    sys.exit()")

result_top = []
with open(TOP_FILE,"r") as file_top:
    for line in file_top:
        result_top.append(list(map(typeread,line.split())))
        if not line.split():
            continue
file_top.close()

NO_TOP = linecount1(TOP_FILE)
list_top = range(NO_TOP)
#
T1_TOP = range(NO_TOP)
T2_TOP = range(NO_TOP)
Q_TOP = range(NO_TOP)
#
#
print >> f2_top,("def charmm_charge_resid(ATOM_NAME,RES_NAME):")
i = 0
for i in list_top:
  T1_TOP[i]  = result_top[i][0]  
  T2_TOP[i]  = result_top[i][1]  
  if (i == 0):
   print >> f2_top,(" if (RES_NAME == \"%s\"): " %(T2_TOP[i]))
   j = i
  elif (T1_TOP[i] == "RESI" and i != 0): 
   print >> f2_top,("   else: ")
   print >> f2_top,("     print (\"THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s.\" %(ATOM_NAME,RES_NAME)) ")
   print >> f2_top,(" elif (RES_NAME == \"%s\"):" %(T2_TOP[i]))
   j = i
  elif (T1_TOP[i] == "ATOM" and i == j+1):
   print >> f2_top,("   if (ATOM_NAME == \"%s\"):" %(T2_TOP[i]))
   Q_TOP[i] = float(result_top[i][3])
   print >> f2_top,("     charge = %8.4f " %(Q_TOP[i]))
  elif (T1_TOP[i] == "ATOM" and i != j+1):
   print >> f2_top,("   elif (ATOM_NAME == \"%s\"):" %(T2_TOP[i]))
   Q_TOP[i] = float(result_top[i][3])
   print >> f2_top,("     charge = %8.4f " %(Q_TOP[i]))
  else:
   print "return charge"
   print i
  i = i + 1
print >> f2_top,("   else: ")
print >> f2_top,("     print (\"THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s.\" %(ATOM_NAME,RES_NAME)) ")
print >> f2_top,(" else:")
print >> f2_top,("   print (\"THE RESIDUE %s IS WRONG\" %(RES_NAME)) ")
print >> f2_top,(" try:")
print >> f2_top,("   return charge")
print >> f2_top,(" except:")
print >> f2_top,("   library_warning_message()")
print >> f2_top,(" ")
#
#
result_n = []
with open("N_terminal.txt","r") as file_n:
   for line in file_n:
      result_n.append(list(map(typeread,line.split())))
      if not line.split():
           continue
file_n.close()
#
NO_N = linecount1("N_terminal.txt")
list_n = range(NO_N)
#
T1_N = range(NO_N)
T2_N = range(NO_N)
Q_N = range(NO_N)
#
#
print >> f2_top,("def N_terminal_charge(ATOM_NAME,RES_NAME):")
i = 0
for i in list_n:
  T1_N[i]  = result_n[i][0]  
  T2_N[i]  = result_n[i][1]  
  if (i == 0):
   print >> f2_top,(" if (RES_NAME == \"%s\"): " %(T2_N[i]))
   j = i
  elif (T1_N[i] == "RESI" and i != 0): 
   print >> f2_top,("   else: ")
   print >> f2_top,("     print (\"THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s.\" %(ATOM_NAME,RES_NAME)) ")
   print >> f2_top,(" elif (RES_NAME == \"%s\"):" %(T2_N[i]))
   j = i
  elif (T1_N[i] == "ATOM" and i == j+1):
   print >> f2_top,("   if (ATOM_NAME == \"%s\"):" %(T2_N[i]))
   Q_N[i] = float(result_n[i][3])
   print >> f2_top,("     charge = %8.4f " %(Q_N[i]))
  elif (T1_N[i] == "ATOM" and i != j+1):
   print >> f2_top,("   elif (ATOM_NAME == \"%s\"):" %(T2_N[i]))
   Q_N[i] = float(result_n[i][3])
   print >> f2_top,("     charge = %8.4f " %(Q_N[i]))
  else:
   print "return charge"
   print i
  i = i + 1
print >> f2_top,("   else: ")
print >> f2_top,("     print (\"THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s.\" %(ATOM_NAME,RES_NAME)) ")
print >> f2_top,(" else:")
print >> f2_top,("   print (\"THE RESIDUE %s IS WRONG\" %(RES_NAME)) ")
print >> f2_top,(" try:")
print >> f2_top,("   return charge")
print >> f2_top,(" except:")
print >> f2_top,("   library_warning_message()")
print >> f2_top,(" ")
#
#
result_c = []
with open("C_terminal.txt","r") as file_c:
   for line in file_c:
      result_c.append(list(map(typeread,line.split())))
      if not line.split():
           continue
file_c.close()
#
NO_C = linecount1("C_terminal.txt")
list_c = range(NO_C)
#
T1_C = range(NO_C)
T2_C = range(NO_C)
Q_C = range(NO_C)
#
#
print >> f2_top,("def C_terminal_charge(ATOM_NAME,RES_NAME):")
i = 0
for i in list_c:
  T1_C[i]  = result_c[i][0]  
  T2_C[i]  = result_c[i][1]  
  if (i == 0):
   print >> f2_top,(" if (RES_NAME == \"%s\"): " %(T2_C[i]))
   j = i
  elif (T1_C[i] == "RESI" and i != 0): 
   print >> f2_top,("   else: ")
   print >> f2_top,("     print (\"THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s.\" %(ATOM_NAME,RES_NAME)) ")
   print >> f2_top,(" elif (RES_NAME == \"%s\"):" %(T2_C[i]))
   j = i
  elif (T1_C[i] == "ATOM" and i == j+1):
   print >> f2_top,("   if (ATOM_NAME == \"%s\"):" %(T2_C[i]))
   Q_C[i] = float(result_c[i][3])
   print >> f2_top,("     charge = %8.4f " %(Q_C[i]))
  elif (T1_C[i] == "ATOM" and i != j+1):
   print >> f2_top,("   elif (ATOM_NAME == \"%s\"):" %(T2_C[i]))
   Q_C[i] = float(result_c[i][3])
   print >> f2_top,("     charge = %8.4f " %(Q_C[i]))
  else:
   print "return charge"
   print i
  i = i + 1
print >> f2_top,("   else: ")
print >> f2_top,("     print (\"THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s.\" %(ATOM_NAME,RES_NAME)) ")
print >> f2_top,(" else:")
print >> f2_top,("   print (\"THE RESIDUE %s IS WRONG\" %(RES_NAME)) ")
print >> f2_top,(" try:")
print >> f2_top,("   return charge")
print >> f2_top,(" except:")
print >> f2_top,("   library_warning_message()")
print >> f2_top,(" ")


os.chmod("./library_charmm_new.py",stat.S_IRWXU)
f2_top.close()
print ("************************************************************************************************ ")
print (" ")
print (" THE NEW CHARMM LIBRARY \"library_charmm_new.py\" WITH NON-STANDARD RESIDUE HAS BEEN GENERATED ")
print (" ")
print ("************************************************************************************************ ")
