from titan import _processing as processing
from titan import _circular_generate as circ
from titan import _spiral_line_generate as sl
from titan import _quantification_txt as quant_txt
from titan import _quantification_pdb as quant_pdb
from titan import _quantification_log as quant_log
from titan import _header as header
from titan import _input as input
import sys

def titan(filename):
    """ The main function """
    input_reader = setup_input_reader(filename)

    if input_reader.type == "CPC":
        cpc_execute(input_reader)
    elif input_reader.type == "SL":
        sl_execute(input_reader)
    elif input_reader.type == "QUANT":
        quant_execute(input_reader)
    header.conclusion_command_line()

def setup_input_reader(filename):
    """ sets up an instance of the input_reader """
    header.header_command_line()
    input_reader = input.InputReader(filename)
    input_reader.determine_type()

    return input_reader

def cpc_execute(input_reader):
    """ executes the workflow for a CPC calculation """
    R, N, distance, field_strength, name, out_format, point1_X, point1_Y, point1_Z, point2_X, point2_Y, point2_Z, \
    unit = input_reader.read_input_cpc()
    circular = circ.CircularGenerate(point1_X, point1_Y, point1_Z, point2_X, point2_Y, point2_Z, R, N,
                                     distance, field_strength, name, unit)
    circular.create_and_write_plates(out_format)

def sl_execute(input_reader):
    """ executes the workflow for a SL calculation """
    radius, N, step, chirality, name, fatom, sequence, charge, point_X, point_Y, point_Z, unit = \
        input_reader.read_input_sl()
    spiral_line = sl.SpiralLineGenerate(sequence, fatom, charge, radius, step, N, chirality, point_X, point_Y,
                                        point_Z, name, unit)
    spiral_line.create_spiral_line_distribution()

def quant_execute(input_reader):
    """ executes the workflow for a quant calculation """
    unit, file_type, name, charge_select, charge_seq, direction, v1x, v1y, v1z, v2x, v2y, v2z, \
    point_x, point_y, point_z = input_reader.read_input_quantification()
    if file_type.upper() == "TXT":
        quantification_txt = quant_txt.QuantificationTxt(name, point_x, point_y, point_z, v1x, v1y, v1z, v2x, v2y, v2z,
                                                         charge_seq, charge_select, unit)
        quantification_txt.execute()
        processing.write_command_line_quant_txt(name)
    if file_type == "PDB":
        force_field, n_terminal, c_terminal = input_reader.read_input_pdb()
        if force_field.upper() == "AMBER":
            quantification_amber = quant_pdb.QuantificationPdbAmber(name, point_x, point_y, point_z, v1x, v1y, v1z,
                                v2x, v2y, v2z, n_terminal, c_terminal, charge_seq, charge_select, unit)
            quantification_amber.execute()
            processing.write_command_line_quant_pdb(name)
        if force_field.upper() == "CHARMM":
            aspp, glup, disu = input_reader.read_input_charmm()
            quantification_charmm = quant_pdb.QuantificationPdbCharmm(name, point_x, point_y, point_z, v1x, v1y, v1z,
                        v2x, v2y, v2z, n_terminal, c_terminal, charge_seq, charge_select, unit, aspp, glup, disu)
            quantification_charmm.execute()
            processing.write_command_line_quant_pdb(name)
    if file_type == "LOG":
        quantification_log = quant_log.QuantificationLog(name, point_x, point_y, point_z, v1x, v1y, v1z, v2x,
                                                         v2y, v2z, charge_seq, charge_select, unit)
        quantification_log.execute()
        processing.write_command_line_quant_log(name)
# ----------------------------------------------------
# Main
if __name__ == '__main__':
    
    # Get Input
    if len(sys.argv[1:]) == 1:
        filename = sys.argv[1]
        titan(filename)
    else:
        print('ERROR: WRONG INPUT')
        print('USAGE:')
        print('python titan.py filename.inp')