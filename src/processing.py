#!/usr/bin/python

import math,sys,os,shutil
#
import vector as vector
import charge_generation as charge_generation
import setup as setup
import output as output

def move_output_cpc(NAME, OUTFORMAT):
    """ move output to right location """
    FILE = os.getcwd()
    if OUTFORMAT == "CHARMM":
        PATH = FILE + "/CHARMM_FORMAT_CPC"
        setup.check(PATH)
    elif OUTFORMAT == "AMBER":
        PATH =FILE + "/AMBER_FORMAT_CPC"
        setup.check(PATH)
    elif OUTFORMAT == "GAUSSIAN":
        PATH =FILE + "/GAUSSIAN_FORMAT_CPC"
        setup.check(PATH)
    else:
        print ("FATAL ERROR. WRONG INPUT FOR \"OUTFORMAT\". ")
        print (" THE %.10s FORMAT FOR UNIFORM EEF GENERATION IS UNDER DEVELOPMENT" %(OUTFORMAT))
        print ("PLEASE SET \"OUTFORMAT\" TO \"CHARMM\" OR \"AMBER\"")
        os.exit()
    
    if OUTFORMAT == "CHARMM":
        setup.movecharmm(NAME)
    elif OUTFORMAT == "AMBER":
        setup.moveamber(NAME)
    elif OUTFORMAT == "GAUSSIAN":
        setup.movegaussian_CPC(NAME)
    else:
        print ("FATAL ERROR. WRONG INPUT FOR \"OUTFORMAT\". ")
        print (" THE %.10s FORMAT FOR UNIFORM EEF GENERATION IS UNDER DEVELOPMENT" %(OUTFORMAT))
        print ("PLEASE SET \"OUTFORMAT\" TO \"CHARMM\" OR \"AMBER\"")
        os.exit()

def move_output_sl(NAME1):
    """ move output to the right location """
    FILE = os.getcwd()
    PATH = FILE + "/GUASS_FORMAT_SL"
    setup.check(PATH)
    setup.moveguass(NAME1)

def print_commandline_cpc(NAME,OUTFORMAT):
    """ print output in command line """
    print ("------------------------------------------------------------------ ")
    print (" ")
    print ("          UNIFORM EXTERNAL ELECTRIC FIEID GENERATION")
    print (" ")
    print ("------------------------------------------------------------------ ")
    print (" ")
    print (" ")
    print (" THE UNIFORM EEF IS GENERATED IN %.10s FORMAT. " %(OUTFORMAT))
    print (" ")
    print (" ")
    if OUTFORMAT == "CHARMM":
        print ("------------------------------------------------------------------ ")
        print ("                            IMPORTANT NOTE")
        print ("------------------------------------------------------------------ ")
        print (" ")
        print (" DO NOT FORGET TO ADD THE TOPOLOGY AND PARMETER OF CHARGES TO YOUR TOPOLOGICAL AND PARAMETER FILES !!!!")
        print (" ")
        print (" ")
        print ("SEE ./CHARMM_FORMAT_CPC/%.10s.info FOR THE TOPOLOGY AND PARMETER OF CHARGES. " %(NAME))
        print (" ")
        print ("------------------------------------------------------------------ ")
        print ("                        END OF IMPORTANT NOTE")
        print ("------------------------------------------------------------------ ")
        print (" ")
        print (" ")
        print (" THE PDB FILE CONTAINING THE TWO PARALLEL CIRCULAR PLATES IS ./CHARMM_FORMAT_CPC/%.10s.pdb" %(NAME))
    elif OUTFORMAT == "AMBER":
        print ("------------------------------------------------------------------ ")
        print ("                           IMPORTANT NOTE")
        print ("------------------------------------------------------------------ ")
        print (" ")
        print (" DO NOT FORGET TO ADD THE TOPOLOGY AND PARMETER OF CHARGES DURING THE SETUP OF SYSTEM !!!!")
        print (" ")
        print (" ")
        print (" SEE \"./AMBER_FORMAT_CPC/%.10s.lib\" AND \"./AMBER_FORMAT_CPC/%.10s.frcmod\"" %(NAME,NAME))
        print (" FOR THE TOPOLOGY AND PARMETER OF CHARGES. ")
        print (" ")
        print (" ")
        print ("------------------------------------------------------------------ ")
        print ("                       END OF IMPORTANT NOTE")
        print ("------------------------------------------------------------------ ")
        print (" ")
        print (" ")
        print (" USE THE COMMAND : ")
        print (" " )
        print ("       cd ./AMBER_FORMAT_CPC")
        print ("       tleap -s -f leap.in")
        print (" ")
        print (" TO GENERATE THE PDB FILE \"%.10s_amber.pdb\" IN AMBER FORMAT." %(NAME))
    elif OUTFORMAT == "GAUSSIAN":
        print (" ")
        print (" THE TXT FILE CONTAINING THE TWO PARALLEL CIRCULAR PLATES IS ./GAUSSIAN_FORMAT_CPC/%.10s.txt" %(NAME))
    else:
        print ("FATAL ERROR. WRONG INPUT FOR \"OUTFORMAT\". ")
        print (" THE %.10s FORMAT FOR UNIFORM EEF GENERATION IS UNDER DEVELOPMENT"%(OUTFORMAT))
        print ("PLEASE SET \"OUTFORMAT\" TO \"CHARMM\" , \"AMBER\" OR \"GAUSSIAN\"")
        os.exit()
    print (" ")
    print (" ")
    print (" THE ELECTRIC FIELD HAS SUCCESFULLY BEEN GENERATED.")
    print (" ")

def print_commandline_sl(NAME1,CHIRALITY,CHARGETYPE):
    """ print output in command line """
    print ("------------------------------------------------------------------ ")
    print (" ")
    print ("           EXTERNAL SPIRAL LINE CHARGES GENERATION")
    print (" ")
    print ("------------------------------------------------------------------ ")
    print (" ")
    print (" ")
    print (" THE %.20sED HELIX IN THE SHAPE OF SPIRAL LINE IS GENERATED." %(CHIRALITY))
    print (" THE SPIRAL LINE IS GENERATED WITH %.20s-TYPE CHARGE DISTRIBUTION." %(CHARGETYPE))
    print (" ")
    print (" ")
    print ("------------------------------------------------------------------ ")
    print ("                            IMPORTANT NOTE")
    print ("------------------------------------------------------------------ ")
    print (" ")
    print (" ")
    print (" PLEASE USE \"CHARGE\" KEYWORKS FOR THE GUASSIAN CALCULATION. ")
    print (" ")
    print (" ")
    print (" SEE ./GUASS_FORMAT_SL/%.10s.info FOR THE DETAILS OF THE SETUP. " %(NAME1))
    print (" ")
    print (" ")
    print ("------------------------------------------------------------------ ")
    print ("                        END OF IMPORTANT NOTE")
    print ("------------------------------------------------------------------ ")
    print (" ")
    print (" ")
    print (" ")
    print (" THE EXTERNAL CHARGES IN THE SPIRAL LINE SHAPE IS GENERATED IN ./GUASS_FORMAT_SL/%.10s.txt" %(NAME1))
    print (" YOU CAN SEE THE PDB FILE FOR THE SHAPE OF CHARGES. (./GUASS_FORMAT_SL/%.10s.pdb)" %(NAME1))
    print (" ")
    print (" ")
    print (" ")
    print (" THE ELECTRIC FIELD HAS SUCCESFULLY BEEN GENERATED.")
    print (" ")

def write_command_line_amber(NAME,NAME_CHARGE_DISTRIBUTION,CHARGE):
    """ print output in command line """
    print ("------------------------------------------------------------------ ")
    print ("------------------------------------------------------------------ ")
    print (" ")
    print (" ")
    print (" THE CHARGE DISTRIBUTION %s IS GENERATED FROM THE PDB FILE %s.pdb." %(NAME_CHARGE_DISTRIBUTION,NAME))
    print (" ")
    print (" THE TOTAL CHARGE IN THE CHARGE DISTRIBUTION IS %f e." %(CHARGE))
    print (" ")
    print (" ")
    print ("------------------------------------------------------------------ ")
    print ("------------------------------------------------------------------ ")
