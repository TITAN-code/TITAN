#!/usr/bin/python

import math,sys,os,shutil

import charge_generation as charge_generation
import input as input
import processing as processing
import setup as setup
import quantification as quantification
import pdb_amber as pdb_amber
import pdb_charmm as pdb_charmm
import direction as direction
import header as header

def titan(filename):
    """ The main function """
    header.header_command_line()
    TYPE = input.determine_type(filename)
    if TYPE == "CPC":
        POINT1_X,POINT1_Y,POINT1_Z,POINT2_X,POINT2_Y,POINT2_Z,R,N,DIS,FIELD,NAME,OUTFORMAT = input.read_input_cpc(filename)
        circular_generate(POINT1_X,POINT1_Y,POINT1_Z,POINT2_X,POINT2_Y,POINT2_Z,R,N,DIS,FIELD,NAME,OUTFORMAT)
    elif TYPE == "SL":
        RADIUS,N,STEP,CHIRALITY,NAME,CHARGETYPE,FATOM,SEQUENCE,CHARGE,XP,YP,ZP = input.read_input_sl(filename)
        sl_generate(RADIUS,N,STEP,CHIRALITY,NAME,CHARGETYPE,FATOM,SEQUENCE,CHARGE,XP,YP,ZP)
    elif TYPE == "QUANT":
        process_quantification_request(filename)
    header.conclusion_command_line()

def process_quantification_request(filename):
    """ The process in case TYPE == QUANT """
    UNIT, FILE,NAME, CHARGE_SELECT,CHARGE_SEQ,DIRECTION = input.read_input_quantification(filename)
    if DIRECTION == "MANUAL":
        V1X, V1Y, V1Z, V2X, V2Y, V2Z, XP, YP, ZP = input.read_input_quantification_manual(filename)
    elif DIRECTION == "SELECT":
        DIRECTION_FILE,ATOM1,ATOM2,ATOM_CENTER = input.read_input_quantification_select(filename)
        V1X, V1Y, V1Z, V2X, V2Y, V2Z, XP, YP, ZP = direction.determine_direction(DIRECTION_FILE,ATOM1,ATOM2,ATOM_CENTER)
    if FILE == "TXT":
        quant(UNIT,NAME,CHARGE_SELECT,CHARGE_SEQ,V1X,V1Y,V1Z,V2X,V2Y,V2Z,XP,YP,ZP)
        print " "
        print "THE ELECTRIC FIELD HAS SUCCESFULLY BEEN QUANTIFIED"
        print " "
    elif FILE == "PDB":
        NAME_CHARGE_DISTRIBUTION,ATOM_SELECT,ATOM_SEQ,FORCE,N_TERMINAL,C_TERMINAL = input.read_input_pdb(filename)
        if FORCE == "AMBER":
            pdb_amber.charge_distribution_generation_amber(NAME,NAME_CHARGE_DISTRIBUTION,ATOM_SELECT,ATOM_SEQ,N_TERMINAL,C_TERMINAL)
        elif FORCE == "CHARMM":
            ASPP,GLUP,DISU = input.read_input_charmm(filename)
            pdb_charmm.charge_distribution_generation_charmm(NAME,NAME_CHARGE_DISTRIBUTION,ATOM_SELECT,ATOM_SEQ,N_TERMINAL,C_TERMINAL,ASPP,GLUP,DISU)
        quant(UNIT,NAME_CHARGE_DISTRIBUTION,CHARGE_SELECT,CHARGE_SEQ,V1X,V1Y,V1Z,V2X,V2Y,V2Z,XP,YP,ZP)
        print " "
        print "THE CHARGE DISTRIBUTION HAS BEEN WRITTEN "
        print "& THE ELECTRIC FIELD HAS SUCCESFULLY BEEN QUANTIFIED"
        print " "
    else:
        print "ERROR! TYPE NOT RECOGNIZED"

def quant(UNIT, NAME, CHARGE_SELECT, CHARGE_SEQ, V1X, V1Y, V1Z, V2X, V2Y, V2Z, XP, YP, ZP):
    """ Quantification of the local electric field """
    content = quantification.read_coordinates_and_charges(NAME)
    VX,VY,VZ = quantification.calculate_direction_vector(V1X, V1Y, V1Z, V2X, V2Y, V2Z)
    EFX,EFY,EFZ,OEF,EFTOT,NO_CHA,COUNT = quantification.calculate_field(NAME,list,content,CHARGE_SEQ,CHARGE_SELECT,UNIT,XP,YP,ZP,VX,VY,VZ)
    quantification.write_output_quant(UNIT,NAME,NO_CHA,EFX,EFY,EFZ,OEF,EFTOT,XP,YP,ZP,V1X,V1Y,V1Z,V2X,V2Y,V2Z,VX,VY,VZ)

def circular_generate(POINT1_X,POINT1_Y,POINT1_Z,POINT2_X,POINT2_Y,POINT2_Z,R,N,DIS,FIELD,NAME,OUTFORMAT):
    """ Generate a circular plate charge """
    charge_generation.circular_plates_charge(POINT1_X,POINT1_Y,POINT1_Z,POINT2_X,POINT2_Y,POINT2_Z,R,N,DIS,FIELD,NAME,OUTFORMAT)
    processing.move_output_cpc(NAME,OUTFORMAT)
    processing.print_commandline_cpc(NAME,OUTFORMAT)

def sl_generate(RADIUS,N,STEP,CHIRALITY,NAME,CHARGETYPE,FATOM,SEQUENCE,CHARGE,XP,YP,ZP):
    """ Generate a spiral line charge """
    setup.checkchargetype(CHARGETYPE,SEQUENCE)
    if (CHIRALITY == "RIGHT-HAND"):
        NAME1 =NAME + "_right"
    else:
        NAME1 =NAME + "_left"
    charge_generation.spiral_lines_charge(NAME1,CHARGETYPE,SEQUENCE,FATOM,CHARGE,RADIUS,STEP,N,CHIRALITY,XP,YP,ZP)
    processing.move_output_sl(NAME1)
    processing.print_commandline_sl(NAME1,CHIRALITY,CHARGETYPE)


# ----------------------------------------------------
# Main
if __name__ == '__main__':
    
    # Get Input
    if len(sys.argv[1:]) == 1:
        filename = sys.argv[1]
        titan(filename)
    else:
        print 'ERROR: Wrong input'
        print 'Usage:'
        print 'python titan.py filename.inp'
