from titan.myimports import *

def header_command_line():
    print ("                                                                 ")
    print ("  ****************************************************************** ")
    print ("  *                                                                * ")
    print ("  *                    TITAN - VERSION 2.0                         * ")
    print ("  *                                                                * ")
    print ("  *           FROM THE HEBREW UNIVERSITY OF JERUSALEM              * ")
    print ("  *    THIJS STUYVER, JING HUANG, DIBYENDU MALLICK, SASON SHAIK    * ")
    print ("  *              J. COMPUT. CHEM. 41, 74-81 (2020)                 * ")
    print ("  *                                                                * ")
    print ("  ****************************************************************** ")
    print ("                                                                 ")

def conclusion_command_line():
    print ("****************************************************************** ")
    print ("                                                                 ")
    print ("NORMAL TERMINATION OF TITAN AT " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print ("                                                                 ")

def error_command_line():
    print ("****************************************************************** ")
    print ("                                                                 ")
    print ("ERROR TERMINATION OF TITAN AT " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print ("                                                                 ")

def header_output_file(f1):

    f1.write("                                                                \n")
    f1.write("  ****************************************************************** \n")
    f1.write("  *                                                                * \n")
    f1.write("  *                    TITAN - VERSION 2.0                         * \n")
    f1.write("  *                                                                * \n")
    f1.write("  *           FROM THE HEBREW UNIVERSITY OF JERUSALEM              * \n")
    f1.write("  *    THIJS STUYVER, JING HUANG, DIBYENDU MALLICK, SASON SHAIK    * \n")
    f1.write("  *              J. COMPUT. CHEM. 41, 74-81 (2020)                 * \n")
    f1.write("  *                                                                * \n")
    f1.write("  ****************************************************************** \n")
    f1.write("                                                                \n")


def conclusion_output_file(f1):
    f1.write("****************************************************************** \n")
    f1.write("                                                                \n")
    f1.write("NORMAL TERMINATION OF TITAN AT " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    f1.write("                                                                \n")

def error_output_file(f1):
    f1.write("****************************************************************** \n")
    f1.write("                                                                \n")
    f1.write("ERROR TERMINATION OF TITAN AT " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    f1.write("                                                                 \n")