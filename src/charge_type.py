#!/usr/bin/python
#
def dna(RES,J):
#
 if (RES == "A"):
   if (J == 1):
    TYPEA = "A1"
    TYPER = "ADEC"
    CHARGE = 1.000000
   elif (J == 2):
    TYPEA = "A2"
    TYPER = "ADEC"
    CHARGE = -1.000000
   elif (J == 3):
    TYPEA = "A3"
    TYPER = "ADEC"
    CHARGE = 0.000000
   elif (J == 4):
    TYPEA = "A4"
    TYPER = "ADEC"
    CHARGE = 0.000000
   elif (J == 5):
    TYPEA = "A5"
    TYPER = "ADEC"
    CHARGE = 0.200000
   elif (J == 6):
    TYPEA = "A6"
    TYPER = "ADEC"
    CHARGE = -0.200000
   else:
    TYPEA = "A7"
    TYPER = "ADEC"
    CHARGE = 0.000000
 elif (RES == "T"):
   if (J == 1):
    TYPEA = "T1"
    TYPER = "THYC"
    CHARGE = 1.000000
   elif (J == 2):
    TYPEA = "T2"
    TYPER = "THYC"
    CHARGE = -1.000000
   elif (J == 3):
    TYPEA = "T3"
    TYPER = "THYC"
    CHARGE = 0.000000
   elif (J == 4):
    TYPEA = "T4"
    TYPER = "THYC"
    CHARGE = 0.000000
   elif (J == 5):
    TYPEA = "T5"
    TYPER = "THYC"
    CHARGE = -0.200000
   elif (J == 6):
    TYPEA = "T6"
    TYPER = "THYC"
    CHARGE = 0.400000
   else:
    TYPEA = "T7"
    TYPER = "THYC"
    CHARGE = -0.200000
 elif (RES == "G"):
   if (J == 1):
    TYPEA = "G1"
    TYPER = "GUAC"
    CHARGE = 1.000000
   elif (J == 2):
    TYPEA = "G2"
    TYPER = "GUAC"
    CHARGE = -1.000000
   elif (J == 3):
    TYPEA = "G3"
    TYPER = "GUAC"
    CHARGE = 0.000000
   elif (J == 4):
    TYPEA = "G4"
    TYPER = "GUAC"
    CHARGE = 0.000000
   elif (J == 5):
    TYPEA = "G5"
    TYPER = "GUAC"
    CHARGE = -0.400000
   elif (J == 6):
    TYPEA = "G6"
    TYPER = "GUAC"
    CHARGE = 0.200000
   else:
    TYPEA = "G7"
    TYPER = "GUAC"
    CHARGE = 0.200000
 elif (RES == "C"):
   if (J == 1):
    TYPEA = "C1"
    TYPER = "CYTC"
    CHARGE = 1.000000
   elif (J == 2):
    TYPEA = "C2"
    TYPER = "CYTC"
    CHARGE = -1.000000
   elif (J == 3):
    TYPEA = "C3"
    TYPER = "CYTC"
    CHARGE = 0.000000
   elif (J == 4):
    TYPEA = "C4"
    TYPER = "CYTC"
    CHARGE = 0.000000
   elif (J == 5):
    TYPEA = "C5"
    TYPER = "CYTC"
    CHARGE = 0.400000
   elif (J == 6):
    TYPEA = "C6"
    TYPER = "CYTC"
    CHARGE = -0.200000
   elif (J == 7):
    TYPEA = "C7"
    TYPER = "CYTC"
    CHARGE = -0.200000
   else:
    print (" ")
    print (" ")
    print ("\"FATOM\" SHOULD BE 7 WITH THE \"SEQUENCE\" OF \"DNA\"")  
    print (" ")
    print (" ")
    os.exit()
 return (TYPEA,TYPER,CHARGE)
#
def frag(RES,J,CHARGE):
 if (RES == "P"):
   if (J <= 1000):
    TYPEA = "P"+str(J-1)
    TYPER = "PCSL"
    CHARGE = CHARGE
   elif (J <= 2000):
    STRJ = str(J-1)
    TYPEA = "O"+STRJ[-3:]
    TYPER = "PCSL"
    CHARGE = CHARGE
   elif (J <= 3000):
    STRJ = str(J-1)
    TYPEA = "S"+STRJ[-3:]
    TYPER = "PCSL"
    CHARGE = CHARGE
   else:
    STRJ = str(J-1)
    TYPEA = "T"+STRJ[-3:]
    TYPER = "PCSL"
    CHARGE = CHARGE
 else:
   if (J <= 1000):
    TYPEA = "N"+str(J-1)
    TYPER = "NCSL"
    CHARGE = 0.00 - CHARGE
   elif (J <= 2000):
    STRJ = str(J-1)
    TYPEA = "E"+STRJ[-3:]
    TYPER = "NCSL"
    CHARGE = 0.00 - CHARGE
   elif (J <= 3000):
    STRJ = str(J-1)
    TYPEA = "G"+STRJ[-3:]
    TYPER = "NCSL"
    CHARGE = 0.00 - CHARGE
   else:
    STRJ = str(J-1)
    TYPEA = "A"+STRJ[-3:]
    TYPER = "NCSL"
    CHARGE = 0.00 - CHARGE
# 
 return (TYPEA,TYPER,CHARGE)
#
#
