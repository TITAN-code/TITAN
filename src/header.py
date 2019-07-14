#!/usr/bin/python
 
import math,sys,os,shutil
import datetime

def header_command_line():
    print ("                                                                 ")
    print ("  ****************************************************************** ")
    print ("  *                                                                * ")
    print ("  *                    TITAN - VERSION 1.1                         * ")
    print ("  *                                                                * ")
    print ("  *           FROM THE HEBREW UNIVERISTY OF JERUSALEM              * ")
    print ("  *    JING HUANG, THIJS STUYVER, DIBYENDU MALLICK, SASON SHAIK    * ")
    print ("  *              J. COMPUT. CHEM. X, XXX-XXX (2019)                * ")
    print ("  *                                                                * ")
    print ("  ****************************************************************** ")
    print ("                                                                 ")

def conclusion_command_line():
    print ("****************************************************************** ")
    print ("                                                                 ")
    print ("NORMAL TERMINATION OF TITAN AT " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    print ("                                                                 ")

def header_output_file(f1):
    print >> f1, "                                                                "
    print >> f1, "  ****************************************************************** "
    print >> f1, "  *                                                                * "
    print >> f1, "  *                    TITAN - VERSION 1.1                         * "
    print >> f1, "  *                                                                * "
    print >> f1, "  *           FROM THE HEBREW UNIVERISTY OF JERUSALEM              * "
    print >> f1, "  *    JING HUANG, THIJS STUYVER,DIBYENDU MALLICK, SASON SHAIK     * "
    print >> f1, "  *              J. COMPUT. CHEM. X, XXX-XXX (2019)                * "
    print >> f1, "  *                                                                * "
    print >> f1, "  ****************************************************************** "
    print >> f1, "                                                                "


def conclusion_output_file(f1):
    print >> f1, "****************************************************************** "
    print >> f1, "                                                                "
    print >> f1, "NORMAL TERMINATION OF TITAN AT " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    print >> f1, "                                                                "
