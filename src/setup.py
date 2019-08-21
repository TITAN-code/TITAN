#!/usr/bin/python
import os
#
def check(DIR):
#
# create directory if it doesn't exist 
#
  CHECK = os.path.exists(DIR)
  if not CHECK:
    os.makedirs(DIR)
#
def movecharmm(NAME):
#
# MOVE THE EEF IN CHARMM FORMAT TO ./CHARMM_FORMAT_CPC
#
  INFO = NAME + ".info"
  PDB = NAME + ".pdb"
  DENT_INFO = "./CHARMM_FORMAT_CPC/" + INFO
  DENT_PDB = "./CHARMM_FORMAT_CPC/" + PDB
  os.rename(INFO,DENT_INFO)
  os.rename(PDB,DENT_PDB)
#
def moveamber(NAME):
#
# MOVE THE EEF IN AMBER FORMAT TO ./AMBER_FORMAT_CPC
#
  INFO = NAME + ".info"
  PDB = NAME + ".pdb"
  LIB = NAME + ".lib"
  FRCMOD = NAME + ".frcmod"
  LEAPIN = "leap.in"
  DENT_INFO = "./AMBER_FORMAT_CPC/" + INFO
  DENT_PDB = "./AMBER_FORMAT_CPC/" + PDB
  DENT_LIB = "./AMBER_FORMAT_CPC/" + LIB 
  DENT_FRCMOD = "./AMBER_FORMAT_CPC/" + FRCMOD
  DENT_LEAPIN = "./AMBER_FORMAT_CPC/" + LEAPIN
#
  os.rename(INFO,DENT_INFO)
  os.rename(PDB,DENT_PDB)
  os.rename(LIB,DENT_LIB)
  os.rename(FRCMOD,DENT_FRCMOD)
  os.rename(LEAPIN,DENT_LEAPIN)

def movegaussian_CPC(NAME):
    #
    # MOVE THE EEF IN GAUSSIAN FORMAT TO ./GAUSSIAN_FORMAT_CPC
    #
    INFO = NAME + ".info"
    TXT = NAME + ".txt"
    DENT_INFO = "./GAUSSIAN_FORMAT_CPC/" + INFO
    DENT_TXT = "./GAUSSIAN_FORMAT_CPC/" + TXT
    os.rename(INFO,DENT_INFO)
    os.rename(TXT,DENT_TXT)
#
#
def moveguass(NAME):
#
# MOVE THE EEF IN GAUSSIAN FORMAT TO ./GUASSIAN_FORMAT_SL
#
  INFO = NAME + ".info"
  PDB = NAME + ".pdb"
  TXT = NAME + ".txt"
  DENT_INFO = "./GAUSS_FORMAT_SL/" + INFO
  DENT_PDB = "./GAUSS_FORMAT_SL/" + PDB
  DENT_TXT = "./GAUSS_FORMAT_SL/" + TXT
  os.rename(INFO,DENT_INFO)
  os.rename(PDB,DENT_PDB)
  os.rename(TXT,DENT_TXT)
#
def checkchargetype(CHARGETYPE,SEQUENCE):
#
#
 L = len(SEQUENCE)
 ITER = range(1,L+1)
 I = 1
 P_NO = 0
 N_NO = 0
 if (CHARGETYPE == "DNA"):
  for I in ITER:
   if not ((SEQUENCE[I-1] == "T") or (SEQUENCE[I-1] == "A") or (SEQUENCE[I-1] == "G") or (SEQUENCE[I-1] == "C")):
    print (" ")
    print (" ")
    print (" ERROR IN THE %d th \" %s \" NUCLEOTIDES IN THE \"SEQUENCE\" " %(I, SEQUENCE[I-1]))
    print (" WITH THE CHARGETYPE =\"DNA\"")
    print (" ")
    print (" PLEASE USE A , T , G OR C ONLY")
    print (" ")
    print (" ")
    os.exit()
  I = I + 1
 elif (CHARGETYPE == "FRAGMENT"):
  for I in ITER:
   if (SEQUENCE[I-1] == "P"):
    P_NO = P_NO + 1
   elif (SEQUENCE[I-1] == "N"):
    N_NO = N_NO + 1
   else:
    print (" ")
    print (" ")
    print (" ERROR IN THE %d th \" %s \" NUCLEOTIDES IN THE \"SEQUENCE\" " %(I, SEQUENCE[I-1]))
    print (" WITH THE CHARGETYPE =\"FRAGMENT\"")
    print (" ")
    print (" ")
    print (" PLEASE USE P OR N ONLY")
    print (" ")
    print (" ")
    os.exit()
  if (P_NO > N_NO):
   N = P_NO - N_NO
   print ("")
   print ("")
   print ("THE NUMBER OF POSTIVE CHARGES IS LARGER THAN THAT OF NEGATIVE CHARGE.")
   print ("")
   print ("PLEASE ADD %5d MORE NEGATIVE FRAGMENTS TO \"SEQUENCE\"."%(N))
   print ("")
   print ("")
   print ("")
   os.exit()
  elif (P_NO < N_NO): 
   N = N_NO - P_NO
   print ("")
   print ("")
   print ("THE NUMBER OF NEGATIVE CHARGES IS LARGER THAN THAT OF POSTIVE CHARGE.")
   print ("")
   print ("PLEASE ADD %5d MORE POSTIVE FRAGMENTS TO \"SEQUENCE\"."%(N))
   print ("")
   print ("")
   print ("")
   os.exit()
  else:
   print ("CONGRATULATIONS!")
   print ("THE \"SEQUENCE\"= %.10000000s IS CORRECT FOR \"CHARGETYPE\" = %.20s."%(SEQUENCE, CHARGETYPE))
   print (" ")
 else:
  print ("")
  print ("")
  print ("THE %.20s CHARGETYPE IS UNDERDEVELOPMENT."%(CHARGETYPE))
  print ("PLEASE SET \"CHARGETYPE\" AS \"FRAGMENT\" ")
  print ("")
  print ("")
  os.exit()

