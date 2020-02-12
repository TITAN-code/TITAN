#!/usr/bin/python
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
