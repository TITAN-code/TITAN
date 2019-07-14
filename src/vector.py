#!/usr/bin/python
from decimal import *
import math
#
PI = 3.1415926535897932384626433832795 # Constant Pi = 3.14159265358979
# Function definition  
# print(getcontext())
getcontext().prec = 50

def unit(U,V,W):
#
# CONVERT THE VECTOR TO UNIT VECTOR
#
  L = math.sqrt(U*U + V*V + W*W)
  UU = U/L
  VU = V/L
  WU = W/L
  return (UU,VU,WU)

def rotate(X,Y,Z,U,V,W,A,B,C,THETA):
#
# A x-coordinate of a point on the line of rotation.
# B y-coordinate of a point on the line of rotation.
# C z-coordinate of a point on the line of rotation.
# U x-coordinate of the unit line's direction vector (normalized).
# V y-coordinate of the unit line's direction vector (normalized).
# W z-coordinate of the unit line's direction vector (normalized).
# theta The angle of rotation, in radians.
#
# Define constant
#
# SET SOME IMTERMEDIATE VALUE
#
  U2 = U*U
  V2 = V*V
  W2 = W*W
  COST = math.cos(THETA)
  SINT = math.sin(THETA)
  ONEMCOST = 1.00-COST
#
# ELEMENT OF ROTATION MATRIX
#
  M11 = U2 + (V2+W2)*COST
  M12 = U*V*ONEMCOST - W*SINT
  M13 = U*W*ONEMCOST + V*SINT
  M14 = (A*(V2+W2) - U*(B*V+C*W))*ONEMCOST + (B*W-C*V)*SINT
#
  M21 = U*V*ONEMCOST + W*SINT
  M22 = V2 + (U2+W2)*COST
  M23 = V*W*ONEMCOST - U*SINT
  M24 = (B*(U2+W2) - V*(A*U+C*W))*ONEMCOST + (C*U-A*W)*SINT
#
  M31 = U*W*ONEMCOST - V*SINT
  M32 = V*W*ONEMCOST + U*SINT
  M33 = W2 + (U2+V2)*COST
  M34 = (C*(U2+V2) - W*(A*U+B*V))*ONEMCOST + (A*V-B*U)*SINT
#
# ROTATED COORDINATE
#
# Multiply this {@link RotationMatrix} times the point (x, y, z, 1),
# representing a point P(x, y, z) in homogeneous coordinates.  The final
# coordinate, 1, is assumed.
# 
# x The point's x-coordinate.
# y The point's y-coordinate.
# z The point's z-coordinate.
# 
  X_NEW  = M11 * X + M12 * Y + M13 * Z + M14
  Y_NEW  = M21 * X + M22 * Y + M23 * Z + M24
  Z_NEW  = M31 * X + M32 * Y + M33 * Z + M34
#
  return (X_NEW,Y_NEW,Z_NEW)
#
#
def angle(X1,Y1,Z1,OX,OY,OZ,X2,Y2,Z2):
  V_X1 = X1 - OX
  V_Y1 = Y1 - OY
  V_Z1 = Z1 - OZ
  V_X2 = X2 - OX
  V_Y2 = Y2 - OY
  V_Z2 = Z2 - OZ
  V1V2 = V_X1*V_X2+V_Y1*V_Y2+V_Z1*V_Z2
  L1 = (V_X1*V_X1+V_Y1*V_Y1+V_Z1*V_Z1)**0.5
  L2 = (V_X2*V_X2+V_Y2*V_Y2+V_Z2*V_Z2)**0.5
  COST = V1V2/(L1*L2) 
  CHECK = math.fabs(COST) - 1.00000000
  if COST > 0.00 and CHECK < 0.000001 and CHECK > 0.0000000000000001:
    COST = 1.00000000000000 
  elif COST < 0.00 and CHECK < 0.000001 and CHECK > 0.0000000000000001:
    COST = -1.00000000000000
  else:
    COST = COST
  THETA = math.acos(COST)*180.000/PI
  return THETA
#
#
def eef_oriented(X,Y,Z,X0,Y0,Z0,Q,DIS):
#
# Calculate oriented electric field (OEF) at (X0, Y0, Z0)
# in presence of the charges Q at (X, Y, Z)
#
#********************************************************
#
#        --  q(i)*(r(i)(->)) --
# EEF =  |  --------------    |                              
#        |      r(i)**2       |                  
#        --                  --           
# Unit: a.u.                                       
#
#********************************************************                                       
#
  K = 1.00                 # The Coulomb force constant (a.u.)
#
  R = math.sqrt((X-X0)*(X-X0)+(Y-Y0)*(Y-Y0)+(Z-Z0)*(Z-Z0)) 
  R = R/0.5291772         # Bohr
  DIS = DIS/0.5291772     # Bohr
  COST =  DIS/R
  EEF1 = (K*Q/(R**2))*COST
  EEF2 = math.fabs(EEF1)
#
  return EEF2
#
def eef_xyz(X,Y,Z,X0,Y0,Z0,Q):
#
# Calculate the value of electric field (EF) at (X0, Y0, Z0)
# The X-component of EF is "EEFX"
# The Y-component of EF is "EEFY"
# The Z-component of EF is "EEFZ"
#
  K = 1.00                 # The Coulomb force constant (a.u.)
#
  R = math.sqrt((X-X0)*(X-X0)+(Y-Y0)*(Y-Y0)+(Z-Z0)*(Z-Z0)) 
  R = R/0.5291772         # Bohr
  DX = (X-X0)/0.5291772     # Bohr
  DY = (Y-Y0)/0.5291772     # Bohr
  DZ = (Z-Z0)/0.5291772     # Bohr
  COSXT =  (-1.0)*DX/R
  COSYT =  (-1.0)*DY/R
  COSZT =  (-1.0)*DZ/R
  EEFX = (K*Q/(R**2))*COSXT
  EEFY = (K*Q/(R**2))*COSYT
  EEFZ = (K*Q/(R**2))*COSZT
#
  return (EEFX,EEFY,EEFZ)
#
#
