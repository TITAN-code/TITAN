#!/usr/bin/python
#

def amberlib_cpc(NAME,CHARGE):
  """ generate *.lib for amber output """
  libfile = open(NAME+".lib", "w")
  print >> libfile, ("!!index array str")
  print >> libfile, (" \"CRP\"")
  print >> libfile, (" \"CRN\"")
  print >> libfile, ("!entry.CRP.unit.atoms table  str name  str type  int typex  int resx  int flags  int seq  int elmnt  dbl chg")
  print >> libfile, (" \"HPC\" \"DP\" 0 1 131075 1 1 %9.8f}" %(CHARGE))
  print >> libfile, ("!entry.CRP.unit.atomspertinfo table  str pname  str ptype  int ptypex  int pelmnt  dbl pchg")
  print >> libfile, (" \"HPC\" \"DP\" 0 -1 0.0")
  print >> libfile, ("!entry.CRP.unit.boundbox array dbl")
  print >> libfile, (" -1.000000")
  print >> libfile, (" 0.0")
  print >> libfile, (" 0.0") 
  print >> libfile, (" 0.0")
  print >> libfile, (" 0.0")
  print >> libfile, ("!entry.CRP.unit.childsequence single int")
  print >> libfile, (" 2")
  print >> libfile, ("!entry.CRP.unit.connect array int")
  print >> libfile, (" 0")
  print >> libfile, (" 0")
  print >> libfile, ("!entry.CRP.unit.hierarchy table  str abovetype  int abovex  str belowtype  int belowx")
  print >> libfile, (" \"U\" 0 \"R\" 1") 
  print >> libfile, (" \"R\" 1 \"A\" 1")
  print >> libfile, ("!entry.CRP.unit.name single str")
  print >> libfile, (" \"default_name\"")
  print >> libfile, ("!entry.CRP.unit.positions table  dbl x  dbl y  dbl z")
  print >> libfile, (" 0.0 0.0 0.0")
  print >> libfile, ("!entry.CRP.unit.residueconnect table  int c1x  int c2x  int c3x  int c4x  int c5x  int c6x")
  print >> libfile, (" 0 0 0 0 0 0")
  print >> libfile, ("!entry.CRP.unit.residues table  str name  int seq  int childseq  int startatomx  str restype  int imagingx")
  print >> libfile, (" \"CRP\" 1 2 1 \"?\" 0")
  print >> libfile, ("!entry.CRP.unit.residuesPdbSequenceNumber array int")
  print >> libfile, (" 1")
  print >> libfile, ("!entry.CRP.unit.solventcap array dbl")
  print >> libfile, (" -1.000000")
  print >> libfile, (" 0.0") 
  print >> libfile, (" 0.0")
  print >> libfile, (" 0.0")
  print >> libfile, (" 0.0")
  print >> libfile, ("!entry.CRP.unit.velocities table  dbl x  dbl y  dbl z")
  print >> libfile, (" 0.0 0.0 0.0")
  print >> libfile, ("!entry.CRN.unit.atoms table  str name  str type  int typex  int resx  int flags  int seq  int elmnt  dbl chg")
  CHARGE = (-1.0000)*CHARGE
  print >> libfile, (" \"HNC\" \"DN\" 0 1 131075 1 1 %10.8f"%(CHARGE))
  print >> libfile, ("!entry.CRN.unit.atomspertinfo table  str pname  str ptype  int ptypex  int pelmnt  dbl pchga")
  print >> libfile, (" \"HNC\" \"DN\" 0 -1 0.0")
  print >> libfile, ("!entry.CRN.unit.boundbox array dbl")
  print >> libfile, (" -1.000000")
  print >> libfile, (" 0.0") 
  print >> libfile, (" 0.0")
  print >> libfile, (" 0.0")
  print >> libfile, (" 0.0")
  print >> libfile, ("!entry.CRN.unit.childsequence single int")
  print >> libfile, (" 2")
  print >> libfile, ("!entry.CRN.unit.connect array int")
  print >> libfile, (" 0")
  print >> libfile, (" 0")
  print >> libfile, ("!entry.CRN.unit.hierarchy table  str abovetype  int abovex  str belowtype  int belowx")
  print >> libfile, (" \"U\" 0 \"R\" 1")
  print >> libfile, (" \"R\" 1 \"A\" 1")
  print >> libfile, ("!entry.CRN.unit.name single str")
  print >> libfile, (" \"default_name\"")
  print >> libfile, ("!entry.CRN.unit.positions table  dbl x  dbl y  dbl z")
  print >> libfile, (" 0.0 0.0 0.0")
  print >> libfile, ("!entry.CRN.unit.residueconnect table  int c1x  int c2x  int c3x  int c4x  int c5x  int c6x")
  print >> libfile, (" 0 0 0 0 0 0")
  print >> libfile, ("!entry.CRN.unit.residues table  str name  int seq  int childseq  int startatomx  str restype  int imagingx")
  print >> libfile, (" \"CRN\" 1 2 1 \"?\" 0")
  print >> libfile, ("!entry.CRN.unit.residuesPdbSequenceNumber array int")
  print >> libfile, (" 1")
  print >> libfile, ("!entry.CRN.unit.solventcap array dbl")
  print >> libfile, (" -1.000000")
  print >> libfile, (" 0.0") 
  print >> libfile, (" 0.0")
  print >> libfile, (" 0.0")
  print >> libfile, (" 0.0")
  print >> libfile, ("!entry.CRN.unit.velocities table  dbl x  dbl y  dbl z")
  print >> libfile, (" 0.0 0.0 0.0")
  libfile.close()
#
def amberfrcmod_cpc(NAME):
#
# generate *.frcmod for amber output 
#

  frcmodfile = open(NAME+".frcmod", "w")
  print >> frcmodfile, ("DUMMY ATOM WITH POSITIVE AND NEGATIVE CHARGES")
  print >> frcmodfile, ("MASS")
  print >> frcmodfile, ("DP        0.0000   0.0000")
  print >> frcmodfile, ("DN        0.0000   0.0000")                              
  print >> frcmodfile, ("")
  print >> frcmodfile, ("BOND")
  print >> frcmodfile, ("")
  print >> frcmodfile, ("ANGLE")
  print >> frcmodfile, ("")
  print >> frcmodfile, ("DIHE")
  print >> frcmodfile, ("")
  print >> frcmodfile, ("IMPROPER")
  print >> frcmodfile, ("")
  print >> frcmodfile, ("NONBON")
  print >> frcmodfile, ("DP        0.0000   0.0000")                              
  print >> frcmodfile, ("DN        0.0000   0.0000")                            
  frcmodfile.close()
#
def amberleapin_cpc(NAME):
#
# generate *.in for amber output 
#
  leap = open("leap.in", "w")
  print >> leap, ("source leaprc.ff99SB")
  print >> leap, ("lib = loadoff %.10s.lib"%(NAME))
  print >> leap, ("check lib")
  print >> leap, ("frcmod = loadamberparams %.10s.frcmod"%(NAME))
  print >> leap, ("SCPC = loadpdb %.10s.pdb"%(NAME))
  print >> leap, ("saveamberparm SCPC %.10s.prmtop %.10s.inpcrd" %(NAME,NAME))
  print >> leap, ("savepdb SCPC %.10s_amber.pdb" %(NAME))
  print >> leap, ("quit")
  leap.close()