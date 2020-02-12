#!/usr/bin/python

import math,vector,output,charge_type
import header as header
#
#
#----------------------------------------------------------------------------
#
#  ORIENTED EXTERNAL ELECTRIC FIELD WITH UNIFORM CIRCULAR PLATE CHARGES
#
#----------------------------------------------------------------------------
def circular_plates_charge(FEX,FEY,FEZ,OX,OY,OZ,R,N,DIS,FIELD,NAME,FORMAT):
  #******************************************************************
  # CONSTANT DEFINITION
  #******************************************************************
  #
  PI = 3.1415926535897932384626433832795 # Constant PI
  INITIALCHARGE = 1.00 # intial charge
  #
  # OUTPUT THE PDB COORDINATE TO opt.pdb
  #
  if FORMAT == "GAUSSIAN":
    f1 = open(NAME+".txt","w")
    coord = []
  else:
    f1 = open(NAME+".pdb", "w")
  #
  # vector of FE=O
  #
  V_X = OX - FEX
  V_Y = OY - FEY
  V_Z = OZ - FEZ
  # Unit vector of Fe=O
  (VU_X,VU_Y,VU_Z) = vector.unit(V_X,V_Y,V_Z)
  #
  #******************************************************************
  # START CREATING THE UNIFORM CIRCULAR PLATES WITH POSITIVE CHARGES
  #******************************************************************
  X0 = (-1.00)*DIS*VU_X + FEX
  Y0 = (-1.00)*DIS*VU_Y + FEY
  Z0 = (-1.00)*DIS*VU_Z + FEZ
  COUNT = 1
  if FORMAT == "CHARMM":
    print >> f1, ("ATOM %6d  HPC CHRP %4d    %8.3f%8.3f%8.3f  1.00  0.00      SCPC" %(COUNT,COUNT,X0,Y0,Z0)) 
  elif FORMAT == "AMBER":
    print >> f1, ("ATOM %6d  HPC CRP  %4d    %8.3f%8.3f%8.3f  1.00  0.00" %(COUNT,COUNT,X0,Y0,Z0))
  elif FORMAT == "GAUSSIAN":
    coord.append([X0,Y0,Z0])
  else:
    print (" THE %.10s FORMAT FOR UNIFORM EEF GENERATION IS UNDER DEVELOPMENT"%(FORMAT))
    os.exit()
  COUNT = COUNT + 1
  #
  # EEF calculation on Fe atom
  #
  EEF1 = vector.eef_oriented(X0,Y0,Z0,FEX,FEY,FEZ,INITIALCHARGE,DIS)
  EEF2 = EEF1
  #
  # CREAT THE UNIFORM CIRCULAR PLATES 
  #
  i = 1
  j = 1
  ITER = range(1,N+1)    # 
  #
  # For Loop (x,y,z) of positive charges
  #
  for i in ITER:    # Set the number of ring
     A1 = 0.5/float(i)
     N1 = PI/(math.asin(A1))
     N2 = int(N1)+1
     THETA = 0.00;
     ITER2 = range(1,N2+1)    # 
     for j in ITER2:
       X = [[0 for m in range(j)] for n in range(i)]
       Y = [[0 for m in range(j)] for n in range(i)]
       Z = [[0 for m in range(j)] for n in range(i)]
  #
  #CONSTRUCT THE SECOND POINT
  #
       if math.fabs(VU_X) < 0.0000001:
         V_X1 = 1.000
         V_Y1 = 0.000
         V_Z1 = 0.000
       elif math.fabs(VU_Y) < 0.0000001:
         V_X1 = 0.000
         V_Y1 = 1.000
         V_Z1 = 0.000
       elif math.fabs(VU_Z) < 0.0000001:
         V_X1 = 0.000
         V_Y1 = 0.000
         V_Z1 = 1.000
       else:
         M = math.sqrt(VU_X*VU_X/(VU_Y*VU_Y+VU_Z*VU_Z))
         V_X1 = ((1.00)/M)*VU_X
         V_Y1 = (-1.00)*M*VU_Y
         V_Z1 = (-1.00)*M*VU_Z
  #
       (V_X1,V_Y1,V_Z1) = vector.unit(V_X1,V_Y1,V_Z1)
       #
       X1 = i*V_X1*R + X0
       Y1 = i*V_Y1*R + Y0
       Z1 = i*V_Z1*R + Z0
  #
       (BX,BY,BZ) = vector.rotate(X1,Y1,Z1,VU_X,VU_Y,VU_Z,X0,Y0,Z0,THETA)
       if  math.fabs(V_X) > 0.00000001 and math.fabs(V_Y) > 0.00000001 and math.fabs(V_Z) > 0.00000001:
         X[i-1][j-1] = BX; Y[i-1][j-1] = BY; Z[i-1][j-1] = -1.0*(V_X/V_Z)*(X[i-1][j-1]-X0)-1.0*(V_Y/V_Z)*(Y[i-1][j-1]-Y0)+Z0
       elif math.fabs(V_X) > 0.00000001 and math.fabs(V_Y) > 0.00000001 and math.fabs(V_Z) < 0.00000001:
         X[i-1][j-1] = BX; Y[i-1][j-1] = -1.0*(V_X/V_Y)*(X[i-1][j-1]-X0)+Y0; Z[i-1][j-1]=BZ
       elif math.fabs(V_X) > 0.00000001 and math.fabs(V_Y) < 0.00000001 and math.fabs(V_Z) > 0.00000001:
         X[i-1][j-1] = BX; Y[i-1][j-1] = BY; Z[i-1][j-1] = -1.0*(V_X/V_Z)*(X[i-1][j-1]-X0)+Z0
       elif math.fabs(V_X) < 0.00000001 and math.fabs(V_Y) > 0.00000001 and math.fabs(V_Z) > 0.00000001:
         X[i-1][j-1] = BX; Y[i-1][j-1] = BY; Z[i-1][j-1] = -1.0*(V_Y/V_Z)*(Y[i-1][j-1]-Y0)+Z0 
       elif math.fabs(V_X) < 0.00000001 and math.fabs(V_Y) < 0.00000001 and math.fabs(V_Z) > 0.00000001:
         X[i-1][j-1] = BX; Y[i-1][j-1] = BY; Z[i-1][j-1] = Z1       
       elif math.fabs(V_X) < 0.00000001 and math.fabs(V_Y) > 0.00000001 and math.fabs(V_Z) < 0.00000001:
         X[i-1][j-1] = BX; Y[i-1][j-1] = Y1; Z[i-1][j-1] = BZ    
       elif math.fabs(V_X) > 0.00000001 and math.fabs(V_Y) < 0.00000001 and math.fabs(V_Z) < 0.00000001:
         X[i-1][j-1] = X1; Y[i-1][j-1] = BY; Z[i-1][j-1] = BZ    
       else:
         print ("ERROR INPUT FOR THE COORDINATE OF \"FE\" AND \"O\". ")
         print ("\"FE\" ATOM HAS THE SAME COORDINATE WIHT \"O\" ATOM. ")
         os.exit()
       if FORMAT == "CHARMM":
         print>>f1, ("ATOM %6d  HPC CHRP %4d    %8.3f%8.3f%8.3f  1.00  0.00      SCPC" %(COUNT,COUNT,X[i-1][j-1],Y[i-1][j-1],Z[i-1][j-1])) 
       elif FORMAT == "AMBER":
         print>>f1, ("ATOM %6d  HPC CRP  %4d    %8.3f%8.3f%8.3f  1.00  0.00" %(COUNT,COUNT,X[i-1][j-1],Y[i-1][j-1],Z[i-1][j-1]))
       elif FORMAT == "GAUSSIAN":
            coord.append([X[i-1][j-1],Y[i-1][j-1],Z[i-1][j-1]])
       else:
         print (" THE %.10s FORMAT FOR UNIFORM EEF GENERATION IS UNDER DEVELOPMENT" %(FORMAT))
         os.exit()
       COUNT = COUNT + 1
       THETA = THETA + (2.0*PI)/float(N2)
  #
  # EEF CALCULATION ON FE ATOM
  #
       EEF1 = vector.eef_oriented(X[i-1][j-1],Y[i-1][j-1],Z[i-1][j-1],FEX,FEY,FEZ,INITIALCHARGE,DIS)
       EEF2 = EEF2 + EEF1
  #
       j = j + 1
     i = i + 1
  #
  # CALCULATE THE ANGLE BETWEEN (X0,Y0,Z0), FE, O
  #
  A_P = vector.angle(X0,Y0,Z0,FEX,FEY,FEZ,OX,OY,OZ)
  #******************************************************************
  # FINISH CREATING THE UNIFORM CIRCULAR PLATES WITH POSITIVE CHARGES
  #******************************************************************
  #
  #
  #******************************************************************
  # START CREATING THE UNIFORM CIRCULAR PLATES WITH NEGATIVE CHARGES
  #******************************************************************
  # COORDINATE OF (X0,Y0,Z0)
  #
  X0 = DIS*VU_X+FEX 
  Y0 = DIS*VU_Y+FEY
  Z0 = DIS*VU_Z+FEZ
  if FORMAT == "CHARMM":
    print >> f1, ("ATOM %6d  HNC CHRN %4d    %8.3f%8.3f%8.3f  1.00  0.00      SCPC" %(COUNT,COUNT,X0,Y0,Z0)) 
  elif FORMAT == "AMBER":
    print >> f1, ("ATOM %6d  HNC CRN  %4d    %8.3f%8.3f%8.3f  1.00  0.00" %(COUNT,COUNT,X0,Y0,Z0))
  elif FORMAT == "GAUSSIAN":
    coord.append([X0,Y0,Z0])
  else:
    print (" THE %.10s FORMAT FOR UNIFORM EEF GENERATION IS UNDER DEVELOPMENT" %(FORMAT))
    os.exit()
# 
  COUNT = COUNT + 1
  # 
  # EEF CALCULATION ON FE ATOM
  #
  EEF1 = vector.eef_oriented(X0,Y0,Z0,FEX,FEY,FEZ,INITIALCHARGE,DIS)
  EEF2 = EEF2 + EEF1
  #
  # CREAT THE UNIFORM CIRCULAR PLATES 
  #
  i = 1
  j = 1
  ITER = range(1,N+1)    # 
  #
  # For Loop (x,y,z) of positive charges
  #
  for i in ITER:    # Set the number of ring
     A1 = 0.5/float(i)
     N1 = PI/(math.asin(A1))
     N2 = int(N1)+1
     THETA = 0.00;
     ITER2 = range(1,N2+1)    # 
     for j in ITER2:
       X = [[0 for m in range(j)] for n in range(i)]
       Y = [[0 for m in range(j)] for n in range(i)]
       Z = [[0 for m in range(j)] for n in range(i)]
  #
  #CONSTRUCT THE SECOND POINT
  #
       if math.fabs(VU_X) < 0.0000001:
         V_X1 = 1.000
         V_Y1 = 0.000
         V_Z1 = 0.000
       elif math.fabs(VU_Y) < 0.0000001:
         V_X1 = 0.000
         V_Y1 = 1.000
         V_Z1 = 0.000
       elif math.fabs(VU_Z) < 0.0000001:
         V_X1 = 0.000
         V_Y1 = 0.000
         V_Z1 = 1.000
       else:
         M = math.sqrt(VU_X*VU_X/(VU_Y*VU_Y+VU_Z*VU_Z))
         V_X1 = ((1.00)/M)*VU_X
         V_Y1 = (-1.00)*M*VU_Y
         V_Z1 = (-1.00)*M*VU_Z
#
       (V_X1,V_Y1,V_Z1) = vector.unit(V_X1,V_Y1,V_Z1)
         #
       X1 = i*V_X1*R + X0
       Y1 = i*V_Y1*R + Y0
       Z1 = i*V_Z1*R + Z0
  #
       (BX,BY,BZ) = vector.rotate(X1,Y1,Z1,VU_X,VU_Y,VU_Z,X0,Y0,Z0,THETA)

       if math.fabs(V_X) > 0.00000001 and math.fabs(V_Y) > 0.00000001 and math.fabs(V_Z) > 0.00000001:
         X[i-1][j-1] = BX; Y[i-1][j-1] = BY; Z[i-1][j-1] = -1.0*(V_X/V_Z)*(X[i-1][j-1]-X0)-1.0*(V_Y/V_Z)*(Y[i-1][j-1]-Y0)+Z0
       elif math.fabs(V_X) > 0.00000001 and math.fabs(V_Y) > 0.00000001 and math.fabs(V_Z) < 0.00000001:
         X[i-1][j-1] = BX; Y[i-1][j-1] = -1.0*(V_X/V_Y)*(X[i-1][j-1]-X0)+Y0; Z[i-1][j-1]=BZ
       elif math.fabs(V_X) > 0.00000001 and math.fabs(V_Y) < 0.00000001 and math.fabs(V_Z) > 0.00000001:
         X[i-1][j-1] = BX; Y[i-1][j-1] = BY; Z[i-1][j-1] = -1.0*(V_X/V_Z)*(X[i-1][j-1]-X0)+Z0
       elif math.fabs(V_X) < 0.00000001 and math.fabs(V_Y) > 0.00000001 and math.fabs(V_Z) > 0.00000001:
         X[i-1][j-1] = BX; Y[i-1][j-1] = BY; Z[i-1][j-1] = -1.0*(V_Y/V_Z)*(Y[i-1][j-1]-Y0)+Z0 
       elif math.fabs(V_X) < 0.00000001 and math.fabs(V_Y) < 0.00000001 and math.fabs(V_Z) > 0.00000001:
         X[i-1][j-1] = BX; Y[i-1][j-1] = BY; Z[i-1][j-1] = Z1       
       elif math.fabs(V_X) < 0.00000001 and math.fabs(V_Y) > 0.00000001 and math.fabs(V_Z) < 0.00000001:
         X[i-1][j-1] = BX; Y[i-1][j-1] = Y1; Z[i-1][j-1] = BZ    
       elif math.fabs(V_X) > 0.00000001 and math.fabs(V_Y) < 0.00000001 and math.fabs(V_Z) < 0.00000001:
         X[i-1][j-1] = X1; Y[i-1][j-1] = BY; Z[i-1][j-1] = BZ    
       else:
         print ("ERROR INPUT FOR THE COORDINATE OF \"FE\" AND \"O\". ")
         print ("\"FE\" ATOM HAS THE SAME COORDINATE WIHT \"O\" ATOM. ")
         os.exit()
#
       if FORMAT == "CHARMM":
         print >> f1, ("ATOM %6d  HNC CHRN %4d    %8.3f%8.3f%8.3f  1.00  0.00      SCPC" %(COUNT,COUNT,X[i-1][j-1],Y[i-1][j-1],Z[i-1][j-1])) 
       elif FORMAT == "AMBER":
         print >> f1, ("ATOM %6d  HNC CRN  %4d    %8.3f%8.3f%8.3f  1.00  0.00" %(COUNT,COUNT,X[i-1][j-1],Y[i-1][j-1],Z[i-1][j-1]))
       elif FORMAT == "GAUSSIAN":
         coord.append([X[i-1][j-1],Y[i-1][j-1],Z[i-1][j-1]])
       else:
         print (" THE %.10s FORMAT FOR UNIFORM EEF GENERATION IS UNDER DEVELOPMENT" %(FORMAT))
         os.exit()
       COUNT = COUNT + 1
       THETA = THETA + (2.0*PI)/float(N2)
  #
  # EEF CALCULATION ON FE
  #
       EEF1 = vector.eef_oriented(X[i-1][j-1],Y[i-1][j-1],Z[i-1][j-1],FEX,FEY,FEZ,INITIALCHARGE,DIS)
       EEF2 = EEF2 +  EEF1
  #
       j = j + 1
     i = i + 1
  #
  # CALCULATE THE ANGLE BETWEEN (X0,Y0,Z0), FE, O
  #
  A_N = vector.angle(X0,Y0,Z0,FEX,FEY,FEZ,OX,OY,OZ)
  #******************************************************************
  # FINISH CREATING THE UNIFORM CIRCULAR PLATES WITH NEGATIVE CHARGES
  #******************************************************************
  #
  # CALCULATE THE NUMBER OF CHARGES IN TWO PLATES
  #
  TOTAL = COUNT - 1
  #
  # CALCULATE THE RADIUS OF CHARGES IN EACH PLATES
  #
  RADIUS = float(R)*float(N)
  #
# print >> f1, ("ATOM %6d   FE FEOA %4d     %7.3f %7.3f %7.3f  1.00  0.00      FEOA" %(COUNT,2,FEX,FEY,FEZ)) 
  COUNT = COUNT + 1
# print >> f1, ("ATOM %6d   O  FEOA %4d     %7.3f %7.3f %7.3f  1.00  0.00      FEOA" %(COUNT,2,OX,OY,OZ)) # Print the (x,y,z) of the center of a circ
  #
  if FORMAT == "AMBER":
    print >> f1, ("END")
  if FORMAT == "CHARMM":
    print >> f1, ("END")
  #
  CHARGE = FIELD/EEF2
  #
  if FORMAT == "GAUSSIAN":
    for i in range(len(coord)/2):
      print >> f1, ("%10.6f     %10.6f      %10.6f       %10.6f" %(coord[i][0],coord[i][1],coord[i][2],CHARGE))
    for i in range(len(coord)/2):
        print >> f1, ("%10.6f     %10.6f      %10.6f       %10.6f" %(coord[len(coord)/2+i][0],coord[len(coord)/2+i][1],coord[len(coord)/2+i][2], -CHARGE))

  f1.close()
  # SUMMARY AND OUTPUT
  #
  f2 = open(NAME+".info", "w")
  header.header_output_file(f2)
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, (" ")
  print >> f2, ("          UNIFORM EXTERNAL ELECTRIC FIELD GENERATION")
  print >> f2, (" ")
  print >> f2, ("------------------------------------------------------------------- ")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" THE UNIFORM EEF IS GENERATED IN %.10s FORMAT. " %(FORMAT))
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, ("                          P/N-POINT1-POINT2 ANGLE ")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, ("   SET P -> THE CENTRE OF CIRCLE PLATE WITH POSITIVE CHARGES ")
  print >> f2, ("   SET N -> THE CENTRE OF CIRCLE PLATE WITH NEGATIVE CHARGES ")
  print >> f2, (" ")
  print >> f2, ("   P-POINT1-POINT2 ANGLES :   %7.2f DEGREE" %(A_P))
  print >> f2, ("   N-POINT1-POINT2 ANGLES :   %7.2f DEGREE" %(A_N))
  print >> f2, (" ")
  print >> f2, ("   PLEASE CHECK WHETHER THE PLATES ARE ALIGNED WITH THE VECTOR ")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, ("                       CHARGE IN EACH PARTCLE")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" IN ORDER FOR THE FIELD TO BE %10.6f A.U., THE CHARGE SHOULD BE %8.4f e."%(FIELD,CHARGE))
  #print >> f2, (" FIELD OF %10.6f e." %(EEF2))
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" ")
#
  if FORMAT == "CHARMM":
    print >> f2, ("------------------------------------------------------------------ ")
    print >> f2, ("                     TOPOLOGY FOR CHARGE")
    print >> f2, ("------------------------------------------------------------------ ")
    print >> f2, (" ")
    print >> f2, (" ")
    print >> f2, (" MASS  66  DUM    0.00000 H  ! DUMMY ATOM ")
    print >> f2, (" ")
    print >> f2, (" ")
    print >> f2, (" RESI CHRP   %8.4f" %(CHARGE))
    print >> f2, (" GROUP")
    print >> f2, (" ATOM HPC  DUM  %8.4f" %(CHARGE))
    print >> f2, (" PATCHING FIRS NONE LAST NONE")
    print >> f2, (" ")
    print >> f2, (" ")
    print >> f2, (" RESI CHRN         %8.4f"%((-1.00)*CHARGE))
    print >> f2, (" GROUP")
    print >> f2, (" ATOM HNC  DUM   %8.4f" %((-1.00)*CHARGE))
    print >> f2, (" PATCHING FIRST ONE LAST NONE")
    print >> f2, (" ")
    print >> f2, (" ")
    print >> f2, ("------------------------------------------------------------------ ")
    print >> f2, ("                     PARAMETER FOR CHARGE")
    print >> f2, ("------------------------------------------------------------------ ")
    print >> f2, (" ")
    print >> f2, (" ")
    print >> f2, (" DUM    0.000000  -0.000000     0.000000 ! ADD TO THE NONBOND SECTION")
    print >> f2, (" ")
  elif FORMAT == "AMBER":
    output.amberlib_cpc(NAME,CHARGE)   
    output.amberfrcmod_cpc(NAME)   
    output.amberleapin_cpc(NAME)   
    print >> f2, ("------------------------------------------------------------------ ")
    print >> f2, ("                TOPOLOGY AND PARAMETER FOR CHARGES")
    print >> f2, ("------------------------------------------------------------------ ")
    print >> f2, (" ")
    print >> f2, (" ")
    print >> f2, (" SEE \"%.10s.lib\" IN \"AMBER_FORMAT/\" FOLDER " %(NAME))
    print >> f2, (" SEE \"%.10s.frcmod\" IN \"AMBER_FORMAT/\" FOLDER "%(NAME))
    print >> f2, (" ")
    print >> f2, (" ")
    print >> f2, ("------------------------------------------------------------------ ")
    print >> f2, ("                         PDB in AMBER FORMAT")
    print >> f2, ("------------------------------------------------------------------ ")
    print >> f2, (" ")
    print >> f2, (" USE THE COMMAND in \"AMBER_FORMAT/\" FOLDER:")
    print >> f2, (" ")
    print >> f2, ("      tleap -s -f leap.in ")
    print >> f2, (" ")
    print >> f2, (" THE PDB FILE OF EEF IS \"%.10s_amber.pdb\"."%(NAME))
    print >> f2, (" ")
    print >> f2, (" ")
  elif FORMAT == "GAUSSIAN":
    pass
  else:
    print (" THE %.10s FORMAT FOR UNIFORM EEF GENERATION IS UNDER DEVELOPMENT" %(FORMAT))
    os.exit()
  print >> f2, (" ")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, ("                              SUMMARY: ")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, (" ")
  print >> f2, ("   The plates have been aligned with the defined vector (POINT1 -> POINT2)")
  print >> f2, (" and positioned %8.4f Angstrom from POINT1. The two "%(DIS))
  print >> f2, (" plates contain %6d point charges, each with an "%(TOTAL))
  print >> f2, (" absolute magnitude of %8.4f e per point. These parameters "%(CHARGE))
  print >> f2, (" are the settings of the charged plates with %8.4f Angstrom"%(RADIUS))
  print >> f2, (" radius")
  print >> f2, (" ")
  print >> f2, (" ")
  if FORMAT == "AMBER":
    print >> f2, (" THE PDB FILE OF TWO PARALLEL CIRCULAR PLATES IS  %10s.pdb" %(NAME))
  if FORMAT == "CHARMM":
    print >> f2, (" THE PDB FILE OF TWO PARALLEL CIRCULAR PLATES IS  %10s.pdb" %(NAME))
  if FORMAT == "GAUSSIAN":
    print >> f2, (" THE TXT FILE OF TWO PARALLEL CIRCULAR PLATES IS  %10s.txt" %(NAME))
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" THE ELECTRIC FIELD HAS BEEN SUCCESFULLY GENERATED. ")
  print >> f2, (" ")
  header.conclusion_output_file(f2)
  f2.close()
    #
 # 
#
#
#-------------------------------------
#
#  END OF EEF GENERATION
#  
#-------------------------------------
#
#
#---------------------------------------------------------------
#
#  EXTERNAL ELECTRIC FIELD WITH THE CHARGES IN THE SPIRAL LINE
#
#---------------------------------------------------------------
def spiral_lines_charge(NAME,CHARGETYPE,SEQUENCE,FATOM,CHARGE,RADII,STEP,N,CHIRALITY,XP,YP,ZP):
#
# NAME : The name of output files.
#        For example, NAME = chrg; output files: chrg.pdb chrg.txt
# SEQUENCE : The sequence of DNA sequence.
# RADII : The radius of the circle (Angstrom)
# STEP : The step between two atoms nearly orientally. (Angstrom)
# N : The number of atoms in one circle.
# 
#
#
# 
  PI = 3.1415926535897932384626433832795 # Constant PI

  pdb = open(NAME+".pdb", "w")
  guass = open(NAME+".txt", "w")
#
# THE NUMBERS OF ATOMS ACCORDING TO THE SEQUENCE
#
  if (CHARGETYPE == "DNA"):
    FATOM = 7
  N_L = int(len(SEQUENCE)*FATOM)  
#
  R = RADII
  i = 1
  j = 1
  ITER = range(1,len(SEQUENCE)+1)    # 
  COUNT = 1
  EFX2 = 0.00
  EFY2 = 0.00
  EFZ2 = 0.00
  #
  XSUM = 0.00
  YSUM = 0.00
  ZSUM = 0.00
  #
  Theta = 0.00;
  X0= R; Y0= 0.000; Z0= (-1.0)*N_L*STEP/2.0
  #
  for i in ITER:    # Set the number of ring
    for j in range(1,FATOM+1):
      k = FATOM*i + j - FATOM -1
      b = math.cos(Theta); c = math.sin(Theta)
      X = R*b; Y = R*c; Z = Z0+STEP*k              # The charge in each ring
      XSUM = XSUM + X
      YSUM = YSUM + Y
      ZSUM = ZSUM + Z
      j = j + 1
      if (CHIRALITY == "RIGHT-HAND"):
        Theta = Theta + (2*PI)/N
      else:
        Theta = Theta - (2*PI)/N
      COUNT = COUNT + 1
    i = i + 1
  #
  XARG = XSUM/float(COUNT - 1)
  YARG = YSUM/float(COUNT - 1)
  ZARG = ZSUM/float(COUNT - 1)
  #
  # RESET THE ITER
  #
  i = 1
  j = 1
  COUNT = 1
  XSUM = 0.00
  YSUM = 0.00
  ZSUM = 0.00
  Theta = 0.00;
  X0= R - XARG; Y0= 0.000 - YARG; Z0= ((-1.0)*N_L*STEP/2.0) - ZARG
  for i in ITER:    # Set the number of ring
    for j in range(1,FATOM+1):
      if (CHARGETYPE == "FRAGMENT"):
        (TYPEA,TYPER,CHARGE_A) = charge_type.frag(SEQUENCE[i-1],j,CHARGE)
      #
      k = FATOM*i + j - FATOM -1
      b = math.cos(Theta); c = math.sin(Theta)
      X = R*b - XARG; Y = R*c - YARG; Z = Z0+STEP*k               # The charge in each ring
      XSUM = XSUM + X
      YSUM = YSUM + Y
      ZSUM = ZSUM + Z
      print >> pdb, ("ATOM %6d%5s %.4s %4d    %8.3f%8.3f%8.3f  1.00  0.00      SLDC" %(COUNT,TYPEA,TYPER,i,X,Y,Z)) 
      print >> guass, ("%10.6f     %10.6f      %10.6f       %10.6f" %(X,Y,Z,CHARGE_A))
      #
      # Electric Field Calculation
      #
      (EFX1,EFY1,EFZ1) = vector.eef_xyz(X,Y,Z,XP,YP,ZP,CHARGE_A)
      EFX2 = EFX2 + EFX1 
      EFY2 = EFY2 + EFY1 
      EFZ2 = EFZ2 + EFZ1 
      COUNT = COUNT + 1
      j = j + 1
      if (CHIRALITY == "RIGHT-HAND"):
        Theta = Theta + (2*PI)/N
      else:
        Theta = Theta - (2*PI)/N
    i = i + 1
  EFTOT = math.sqrt(EFX2*EFX2+EFY2*EFY2+EFZ2*EFZ2) 
  PITCH = Z - Z0 
  TOTAL = COUNT - 1
  # 
  #
  XARG = XSUM/float(COUNT - 1)
  YARG = YSUM/float(COUNT - 1)
  ZARG = ZSUM/float(COUNT - 1)
  #  The end of for Loop
  # 
  print >> pdb, ("END")
  pdb.close()
  guass.close()
  # 
  # SUMMARY AND OUTPUT
  #
  f2 = open(NAME+".info", "w")
  header.header_output_file(f2)
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, (" ")
  print >> f2, ("               EXTERNAL SPIRAL LINE CHARGE GENERATION")
  print >> f2, (" ")
  print >> f2, ("------------------------------------------------------------------- ")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" THE EEF IS GENERATED IN GUASSIAN FORMAT ")
  print >> f2, (" WITH A COPY OF THE POSITIONS ALSO IN PDB FORMAT. ")
  print >> f2, (" ")
  print >> f2, (" ")
  if (CHARGETYPE == "DNA"):
    print >> f2, ("------------------------------------------------------------------ ")
    print >> f2, ("                         CHARGES OF DNA ")
    print >> f2, ("------------------------------------------------------------------ ")
    print >> f2, (" ")
    print >> f2, (" THE CHARGES OF DEOXYRIBOSE NUCLEOTIDES ARE TAKEN FROM THE SIRAH FORCE FIELD ")
    print >> f2, (" ---A COARSE GRAINED FORCE FIELD FOR DNA MOLECULES. ")
    print >> f2, (" See http://www.sirahff.com/ ")
    print >> f2, (" ")
    print >> f2, (" ")
    print >> f2, ("       IN THIS SCRIPT                SIRAH FORCE FIELD--AMBER")
    print >> f2, ("------------------------------    ------------------------------")
    print >> f2, (" DEOXYRIBOSE | ATOM |              DEOXYRIBOSE | ATOM |         ")
    print >> f2, (" NUCLEOTIDES | TYPE | CHARGE       NUCLEOTIDES | TYPE | CHARGE")
    print >> f2, ("------------------------------    ------------------------------")
    print >> f2, ("  Adenine    |  A1  | 1.0000         Adenine   |      |       ")
    print >> f2, ("             |  A2  |-1.0000         (DAX)     |  PX  |-1.0000")
    print >> f2, (" (ADD \"A1\"   |  A3  | 0.0000                   |  KX  | 0.0000")
    print >> f2, (" TO NETURAL  |  A4  | 0.0000         -1.0000   |  KN  | 0.0000")
    print >> f2, (" THE         |  A5  | 0.2000                   |  NX  | 0.2000")
    print >> f2, (" NUCLEOTIDES)|  A6  |-0.2000                   |  NW  |-0.2000")
    print >> f2, ("             |  A7  | 0.0000                   |  CX  | 0.0000")
    print >> f2, ("------------------------------     ----------------------------- ")
    print >> f2, ("  Thymine    |  T1  | 1.0000         Thymine   |      |       ")
    print >> f2, ("             |  T2  |-1.0000          (DTX)    |  PX  |-1.0000")
    print >> f2, (" (ADD \"T1\"   |  T3  | 0.0000                   |  KX  | 0.0000")
    print >> f2, (" TO NETURAL  |  T4  | 0.0000         -1.0000   |  KN  | 0.0000")
    print >> f2, (" THE         |  T5  |-0.2000                   |  OX  |-0.2000")
    print >> f2, (" NUCLEOTIDES)|  T6  | 0.4000                   |  NL  | 0.4000")
    print >> f2, ("             |  T7  |-0.2000                   |  OY  |-0.2000")
    print >> f2, ("------------------------------     ----------------------------- ")
    print >> f2, ("  Guanine    |  G1  | 1.0000         Guanine   |      |       ")
    print >> f2, ("             |  G2  |-1.0000          (DGX)    |  PX  |-1.0000")
    print >> f2, (" (ADD \"G1\"   |  G3  | 0.0000                   |  KX  | 0.0000")
    print >> f2, (" TO NETURAL  |  G4  | 0.0000         -1.0000   |  KN  | 0.0000")
    print >> f2, (" THE         |  G5  |-0.4000                   |  OZ  |-0.4000")
    print >> f2, (" NUCLEOTIDES)|  G6  | 0.2000                   |  NR  | 0.2000")
    print >> f2, ("             |  G7  | 0.2000                   |  NS  | 0.2000")
    print >> f2, ("------------------------------     ----------------------------- ")
    print >> f2, ("  Cytosine   |  C1  | 1.0000         Cytosine  |      |       ")
    print >> f2, ("             |  C2  |-1.0000          (DCX)    |  PX  |-1.0000")
    print >> f2, (" (ADD \"C1\"   |  C3  | 0.0000                   |  KX  | 0.0000")
    print >> f2, (" TO NETURAL  |  C4  | 0.0000         -1.0000   |  KN  | 0.0000")
    print >> f2, (" THE         |  C5  | 0.4000                   |  NF  | 0.4000")
    print >> f2, (" NUCLEOTIDES)|  C6  |-0.2000                   |  NU  |-0.2000")
    print >> f2, ("             |  C7  |-0.2000                   |  OV  |-0.2000")
    print >> f2, ("------------------------------     ----------------------------- ")
    print >> f2, (" ")
    print >> f2, (" ")
  else:
    print >> f2, ("------------------------------------------------------------------ ")
    print >> f2, ("                     CHARGES OF FRAGMENT ")
    print >> f2, ("------------------------------------------------------------------ ")
    print >> f2, (" ")
    print >> f2, (" THE CHARGES OF IN THE POINTS OF THE \"P\" FRAGMENT ARE %9.6f."%(CHARGE))
    print >> f2, (" THE CHARGES OF IN THE POINTS OF THE \"N\" FRAGMENT ARE %9.6f."%(0.00-CHARGE))
    print >> f2, (" ")
    print >> f2, (" ")
    print >> f2, ("--------------------------------")
    print >> f2, ("   FRAGMENT  | ATOM | CHARGE    ")
    print >> f2, ("             | TYPE |           ")
    print >> f2, ("-------------------------------- ")
    print >> f2, ("             |  P0  | %10.6f"%(CHARGE))
    print >> f2, ("   FRAGMENT  |  P1  | %10.6f"%(CHARGE))
    print >> f2, ("      P      |  P2  | %10.6f"%(CHARGE))
    print >> f2, ("             |  P3  | %10.6f"%(CHARGE))
    print >> f2, ("             |  P4  | %10.6f"%(CHARGE))
    print >> f2, ("             |   .  |    .")
    print >> f2, ("             |   .  |    .")
    print >> f2, ("             |   .  |    .")
    print >> f2, ("---------------------------------")
    print >> f2, ("             |  N0  | %10.6f"%(0.00-CHARGE))
    print >> f2, ("   FRAGMENT  |  N1  | %10.6f"%(0.00-CHARGE))
    print >> f2, ("      N      |  N2  | %10.6f"%(0.00-CHARGE))
    print >> f2, ("             |  N3  | %10.6f"%(0.00-CHARGE))
    print >> f2, ("             |  N4  | %10.6f"%(0.00-CHARGE))
    print >> f2, ("             |   .  |    . ")
    print >> f2, ("             |   .  |    . ")
    print >> f2, ("             |   .  |    . ")
    print >> f2, ("---------------------------------")
    print >> f2, " "
    print >> f2, " "
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, ("                           GUASSIAN INPUT")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" THE EXTERNAL CHARGES ARE AVAIABLE IN %.10s.txt FILE." %(NAME))
  print >> f2, (" PLEASE USE \"CHARGE\" KEYWORDS IN GUASSIAN 09 CALCULATION.")
  print >> f2, (" ")
  print >> f2, (" FORMAT: ")
  print >> f2, ("     X_COORDINATE    Y_COORDINATE    Z_COORDINATE    CHARGE")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" IF YOU WANTED TO CHECK THE SHAPE OF THE CHARGES GENERATED,")
  print >> f2, (" PLEASE SEE %.10s.pdb FILE."%(NAME))
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, ("                       ELECTRIC FIELD ")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" THE GEOMETRICAL CENTER OF THE POINT CHARGE IS LOCALIZED AT ( %9.6f, %9.6f, %9.6f ) :"%(XARG,YARG,ZARG))
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" THE ELECTRIC FIELD (EF) AT (%9.6f, %9.6f, %9.6f) IS :"%(XP,YP,ZP))
  print >> f2, (" X-COMPONENT OF EF: %9.6f  A.U.;"%(EFX2))
  print >> f2, (" Y-COMPONENT OF EF: %9.6f  A.U.;"%(EFY2))
  print >> f2, (" Z-COMPONENT OF EF: %9.6f  A.U.;"%(EFZ2))
  print >> f2, (" TOTAL VALUE OF EF: %9.6f  A.U.."%(EFTOT))
  print >> f2, (" ")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, ("                       SUMMARY: ")
  print >> f2, ("------------------------------------------------------------------ ")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, ("  The spiral line is generated in %.10sed chirality."%(CHIRALITY))
  print >> f2, (" The pitch of the spiral line is %8.4f Angstrom. "%(PITCH))
  print >> f2, (" The radius of the spiral line is %8.4f Angstrom. "%(RADII))
  print >> f2, (" The line contains %6d point charges with a %.10s-type charge."%(TOTAL,CHARGETYPE))
  print >> f2, (" The sequence is the following: ")
  print >> f2, (" \" %.10000000s \". "%(SEQUENCE))
  print >> f2, (" ")
  if (CHARGETYPE == "DNA"):
    print >> f2, (" The charges of atoms in the DNA nanotube are taken from:")
    print >> f2, (" sirah force field. ")
  else: 
    print >> f2, (" There are %d points in the fragment of \"P\" or \"N\"."%(FATOM))
    print >> f2, (" The charges of each points are %9.6f and %9.6f for the fragments."%(CHARGE,0.00-CHARGE))
    print >> f2, (" of \"P\" and \"N\" respectively.")
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" THE GUASSIAN EXTERNAL CHARGE OF TWO SPIRAL LINES IS SHOWN IN %.10s.txt" %(NAME))
  print >> f2, (" THE PDB FILE FOR THE SPIRAL LINE IS %.10s.pdb" %(NAME))
  print >> f2, (" ")
  print >> f2, (" ")
  print >> f2, (" THE ELECTRIC FIELD HAS BEEN SUCCESFULLY GENERATED. ")
  print >> f2, (" ")
  header.conclusion_output_file(f2)
  f2.close()
