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
    print ("  *                    TITAN - VERSION 1.2                         * ")
    print ("  *                                                                * ")
    print ("  *           FROM THE HEBREW UNIVERISTY OF JERUSALEM              * ")
    print ("  *    THIJS STUYVER, JING HUANG, DIBYENDU MALLICK, SASON SHAIK    * ")
    print ("  *              J. COMPUT. CHEM. X, XXX-XXX (2019)                * ")
    print ("  *                                                                * ")
    print ("  ****************************************************************** ")
    print ("                                                                 ")
    print ("                                                                 ")
    print ("                     AMBER LIBRARY GENERATION                    ")
    print ("                                                                 ")
#_____________________________________________________________________________________

header_command_line()

TOP_FILE = "top_amino94.lib"

f2_top = open("library_amber_new.py", "w")
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
result_line = []
with open(TOP_FILE,"r") as file_top:
    for line in file_top:
        result_top.append(list(map(typeread,line.split())))
        if not line.split():
            continue
file_top.close()
with open(TOP_FILE,"r") as file_top1:
    result_line = file_top1.readlines()
file_top1.close()

NO_TOP = linecount1(TOP_FILE)
list_top = range(NO_TOP)

T1_TOP = range(NO_TOP)
T2_TOP = range(NO_TOP)
Q_TOP = range(NO_TOP)
#
#
print >> f2_top,("def amber_charge_resid(ATOM_NAME,RES_NAME):")
i = 0
for i in list_top:
  INITIAL = result_top[i][0]
  if INITIAL[0] == "!" :
    RESI_T = INITIAL.split('.')[1]
    T1_TOP[i]  = "RESI"
    T2_TOP[i]  = RESI_T
  elif INITIAL[0] == "\"":
    T1_TOP[i] = "ATOM"
    T2_TOP[i] = INITIAL.strip("\"")
  else:
    print  (" ")
    print  (" ")
    print  ("ERROR IN THE FILE \"top_amino94.lib\" IN LINE %d" %(i+1))
    print  ("%s" %(result_line[i]))
    print  (" PLEASE FIX IT !")
    print  (" ")
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
   Q_TOP[i] = float(result_top[i][7])
   print >> f2_top,("     charge = %8.4f " %(Q_TOP[i]))
  elif (T1_TOP[i] == "ATOM" and i != j+1):
   print >> f2_top,("   elif (ATOM_NAME == \"%s\"):" %(T2_TOP[i]))
   Q_TOP[i] = float(result_top[i][7])
   print >> f2_top,("     charge = %8.4f " %(Q_TOP[i]))
  else:
   print "return charge"
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
result_nline = []
with open("N_terminal.lib","r") as file_n:
   for line in file_n:
      result_n.append(list(map(typeread,line.split())))
      if not line.split():
           continue
file_n.close()
with open("N_terminal.lib","r") as file_n1:
   result_nline = file_n1.readlines()
file_n1.close()
#
NO_N = linecount1("N_terminal.lib")
list_n = range(NO_N)
#
T1_N = range(NO_N)
T2_N = range(NO_N)
Q_N = range(NO_N)
#
print >> f2_top,("def N_terminal_charge(ATOM_NAME,RES_NAME):")
i = 0
for i in list_n:
  INITIAL = result_n[i][0]
  if INITIAL[0] == "!" :
    RESI_T = INITIAL.split('.')[1]
    T1_N[i]  = "RESI"
    T2_N[i]  = RESI_T
  elif INITIAL[0] == "\"":
    T1_N[i] = "ATOM"
    T2_N[i] = INITIAL.strip("\"")
  else:
    print  (" ")
    print  (" ")
    print  ("ERROR IN THE FILE \"N_terminal.lib\" IN LINE %d" %(i+1))
    print  ("%s" %(result_line[i]))
    print  (" PLEASE FIX IT !")
    print  (" ")
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
   Q_N[i] = float(result_n[i][7])
   print >> f2_top,("     charge = %8.4f " %(Q_N[i]))
  elif (T1_N[i] == "ATOM" and i != j+1):
   print >> f2_top,("   elif (ATOM_NAME == \"%s\"):" %(T2_N[i]))
   Q_N[i] = float(result_n[i][7])
   print >> f2_top,("     charge = %8.4f " %(Q_N[i]))
  else:
   print "return charge"
  i = i + 1
print >> f2_top,("   else:")
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
result_cline = []
with open("C_terminal.lib","r") as file_c:
   for line in file_c:
      result_c.append(list(map(typeread,line.split())))
      if not line.split():
           continue
file_c.close()
with open("C_terminal.lib","r") as file_c1:
   result_cline = file_c1.readlines()
file_c1.close()
#
NO_C = linecount1("C_terminal.lib")
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
  INITIAL = result_c[i][0]
  if INITIAL[0] == "!" :
    RESI_T = INITIAL.split('.')[1]
    T1_C[i]  = "RESI"
    T2_C[i]  = RESI_T
  elif INITIAL[0] == "\"":
    T1_C[i] = "ATOM"
    T2_C[i] = INITIAL.strip("\"")
  else:
    print  (" ")
    print  (" ")
    print  ("ERROR IN THE FILE \"N_terminal.lib\" IN LINE %d" %(i+1))
    print  ("%s" %(result_line[i]))
    print  (" PLEASE FIX IT !")
    print  (" ")
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
   Q_C[i] = float(result_c[i][7])
   print >> f2_top,("     charge = %8.4f " %(Q_C[i]))
  elif (T1_C[i] == "ATOM" and i != j+1):
   print >> f2_top,("   elif (ATOM_NAME == \"%s\"):" %(T2_C[i]))
   Q_C[i] = float(result_c[i][7])
   print >> f2_top,("     charge = %8.4f " %(Q_C[i]))
  else:
   print "return charge"
  i = i + 1
print >> f2_top,("   else:")
print >> f2_top,("     print (\"THE ATOM TYPE %s CANNOT BE FOUND IN THE RESIDUE %s.\" %(ATOM_NAME,RES_NAME)) ")
print >> f2_top,(" else:")
print >> f2_top,("   print (\"THE RESIDUE %s IS WRONG\" %(RES_NAME)) ")
print >> f2_top,(" try:")
print >> f2_top,("   return charge")
print >> f2_top,(" except:")
print >> f2_top,("   library_warning_message()")
print >> f2_top,(" ")


os.chmod("./library_amber_new.py",stat.S_IRWXU)
f2_top.close()
print ("********************************************************************************************* ")
print (" ")
print (" THE NEW AMBER LIBRARY \"library_amber_new.py\" WITH NON-STANDARD RESIDUE HAS BEEN GENERATED ")
print (" ")
print ("********************************************************************************************* ")


