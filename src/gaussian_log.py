#!/usr/bin/python

import sys
import datetime

def determine_geometry_block(line_list):
    """ Determine start and end of the geometry block. Verify the exact ending of the geometry block """
    counter = 0
    for line in line_list:
        counter +=1
        if 'Input orientation:' in line:
            start = counter + 4
        elif 'Standard orientation:' in line:
            end = counter - 8
        elif 'Distance matrix (angstroms):' in line:
            end_alternative = counter - 2
        else:
            pass
    block_length = end - start
    try:
        block_length_alternative = end_alternative - start
    except:
        block_length_alternative = block_length + 1

    if block_length < block_length_alternative:
        return start, end
    if block_length > block_length_alternative:
        return start, end_alternative

def determine_charges_block(line_list):
    """ Determine start and end of the geometry block """
    counter = 0
    start_list = []
    end_list = []
    for line in line_list:
        counter +=1
        if 'Summary of Natural Population Analysis:' in line:
            start_list.append(counter + 5)
        elif '   Atom  No          Natural Electron Configuration' in line:
            end_list.append(counter - 12)
        else:
            pass
    return start_list, end_list

def retrieve_geometry(filename):
    """ Store the geometry """
    with open(filename,'r') as f_obj:
        contents = f_obj.read()
        line_list = contents.split("\n")
    start, end = determine_geometry_block(line_list)
    geometry_line_list = []
    element_number = []
    x_coord = []
    y_coord = []
    z_coord = []

    for number in range(start,end):
        geometry_line_list.append(line_list[number])
    for line in geometry_line_list:
        temp_list = line.split()
        element_number.append(temp_list[1])
        x_coord.append(float(temp_list[3]))
        y_coord.append(float(temp_list[4]))
        z_coord.append(float(temp_list[5]))

    element_name = element_name_conversion(element_number)

    return element_name, x_coord, y_coord, z_coord

def element_name_conversion(element_number):
    """ Convert element number to element name """
    element_name = []
    element_dictionary = {1 : 'H', 2 : 'He', 3 : 'Li', 4 : 'Be', 5 : 'B', 6 : 'C', 7 : 'N', 8 : 'O', 9 : 'F', 10 : 'Ne',
                          11 : 'Na', 12 : 'Mg', 13: 'Al', 14 : 'Si', 15 : 'P', 16: 'S', 17 : 'Cl', 18 : 'Ar', 19: 'K',
                          20 : 'Ca', 21 : 'Sc', 22 : 'Ti', 23 : 'V', 24 : 'Cr', 25 : 'Mn', 26 : 'Fe', 27 : 'Co',
                          28 : 'Ni', 29 : 'Cu', 30 : 'Zn', 31 : 'Ga', 32 : 'Ge', 33 : 'As', 34 : 'Se', 35 : 'Br', 36 : 'Kr',
                          37 : 'Rb', 38 : 'Sr', 39 : 'Y', 40 : 'Zr', 41 : 'Nb', 42 : 'Mo', 43 : 'Tc', 44 : 'Ru', 45 : 'Rh',
                          46 : 'Pd', 47 : 'Ag', 48 : 'Cd', 49 : 'In', 50: 'Sn', 51 : 'Sb', 52 : 'Te', 53 : 'I', 54 : 'Xe',
                          55 : 'Cs', 56 : 'Ba', 57 : 'La', 72 : 'Hf', 73 : 'Ta', 74 : 'W', 75 : 'Re', 76 : 'Os', 77 : 'Ir',
                          78 : 'Pt', 79 : 'Au', 80 : 'Hg', 81 : 'Tl', 82 : 'Pb', 83 : 'Bi', 84 : 'Po', 85 : 'At', 86 : 'Rn'}

    for element in element_number:
        try:
            element_name.append(element_dictionary[int(element)])
        except:
            element_name.append(element)
            print 'unknown element number!'

    return element_name

def retrieve_charge(filename):
    """ Store the charge """
    with open(filename, 'r') as f_obj:
        contents = f_obj.read()
        line_list = contents.split("\n")
    start_list, end_list = determine_charges_block(line_list)
    total_prints = len(start_list)
    start = start_list[total_prints - 3]
    end = end_list[total_prints - 3]
    NPA_list = []
    charge = []
    for number in range(start,end):
        NPA_list.append(line_list[number])
    for line in NPA_list:
        temp_list = line.split()
        charge.append(float(temp_list[2]))
    return charge

def align_numbers(list,number_of_digits):
    """ Align all numbers nicely """
    list_aligned = []
    for number in list:
        if '-' in str(number):
            list_aligned.append(str(number)[:number_of_digits+1])
        else:
            list_aligned.append(' ' + str(number)[:number_of_digits])
    return list_aligned

def assemble_output(filename):
    """ Extract all the needed information from the .log file """

    element_name, x_coord, y_coord, z_coord = retrieve_geometry(filename)
    charge = retrieve_charge(filename)

    x_coord_aligned = align_numbers(x_coord,7)
    y_coord_aligned = align_numbers(y_coord,7)
    z_coord_aligned = align_numbers(z_coord,7)
    charge_aligned = align_numbers(charge,5)

    return element_name, x_coord_aligned, y_coord_aligned, z_coord_aligned, charge_aligned

def write_output_NBO(filename,NAME_CHARGE_DISTRIBUTION,ATOM_SELECT,ATOM_SEQ):
    """ Write the output """
    element_name, x_coord, y_coord, z_coord, charge = assemble_output(filename)
    f1 = open(NAME_CHARGE_DISTRIBUTION + '.txt','w')
    NAME = filename.strip(".log")
    f2 = open(NAME + "_atom_list" + ".save", "w")
    if ATOM_SELECT == "ALL":
        for atom in range(len(element_name)):
            f1.write(' %s \t %s \t %s \t %s \n' % (x_coord[atom], y_coord[atom], z_coord[atom], charge[atom]))
            f2.write(' %s \t %s \t %s \t %s \t %s \n' % (element_name[atom], x_coord[atom], y_coord[atom], z_coord[atom], charge[atom]))
    if ATOM_SELECT == "PART":
        atom_N = 0
        for atom in range(len(element_name)):
            atom_N += 1
            if atom_N in ATOM_SEQ:
                f1.write(' %s \t %s \t %s \t %s \n' % (x_coord[atom], y_coord[atom], z_coord[atom], charge[atom]))
                f2.write(' %s \t %s \t %s \t %s \t %s \n' % (element_name[atom], x_coord[atom], y_coord[atom], z_coord[atom], charge[atom]))
    f1.close()
    f2.close()

def convert_atom_seq(ATOM_SEQ):
    "in case of ATOM_SELECT = SELECT, the read-in ATOM_SEQ-string has to be converted into a list, i.e. an actual selection"
    string = ATOM_SEQ
    ATOM_SEQ = []
    seq_list = string.split("+")
    seq_list2 = []
    for element in seq_list:
        seq_list2.append(element.split("("))
    for i in range(len(seq_list2)):
        if seq_list2[i][0] == "P":
            ATOM_SEQ += P(int(seq_list2[i][1].strip(")")))
        if seq_list2[i][0] == "R":
            boundaries = seq_list2[i][1].split(",")
            left_boundary = int(boundaries[0])
            right_boundary = int(boundaries[1].strip(")"))
            ATOM_SEQ += R(left_boundary,right_boundary)
    return ATOM_SEQ

def R(i,j):
    """define range of atoms to be read"""
    L = []
    L = range(i,j+1)
    return L

def P(i):
    """ define a single atom to be read"""
    L = [i]
    return L

def charge_distribution_generation(NAME, NAME_CHARGE_DISTRIBUTION, ATOM_SELECT, ATOM_SEQ, TYPE_OF_CHARGES):
    """ Generate the charge distribution from the GAUSSIAN log-file """
    if ATOM_SELECT == "PART":
        ATOM_SEQ = convert_atom_seq(ATOM_SEQ)
    filename = NAME + '.log'
    if TYPE_OF_CHARGES == "NBO":
        write_output_NBO(filename,NAME_CHARGE_DISTRIBUTION,ATOM_SELECT,ATOM_SEQ)
