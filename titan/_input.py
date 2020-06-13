import sys as _sys
import datetime as _datetime

class InputReader:
    def __init__(self, filename):
        self.filename = filename

        self.line_list = self.generate_line_list()
        self.type = self.determine_type()

    def generate_line_list(self):
        """ read the content of the file into a line_list"""
        with open(self.filename, 'r', encoding="utf-8") as f_obj:
            contents = f_obj.read()
            line_list = contents.split("\n")
        for i in range(len(line_list)):
            line_list[i] = line_list[i].split(" ")
        return line_list

    def determine_type(self):
        """ determine type of calculation """
        for line in self.line_list:
            if line[0].upper() == "TYPE":
                type = line[2]
        try:
            return str(type)
        except:
            print("INVALID TYPE PARAMETER \n \n")
            self.exception_message()

    def read_input_cpc(self):
        """ read parameters for cpc calculation """
        for line in self.line_list:
            if line[0].upper() == "R":
                R = line[2]
            if line[0].upper() == "N":
                N = line[2]
            if line[0].upper() == "DIS":
                distance = line[2]
            if line[0].upper() == "FIELD_STRENGTH":
                field_strength = line[2]
            if line[0].upper() == "NAME":
                name = line[2]
            if line[0].upper() == "OUTFORMAT":
                out_format = line[2]
            if line[0].upper() == "POINT1_X":
                point1_X = line[2]
            if line[0].upper() == "POINT1_Y":
                point1_Y = line[2]
            if line[0].upper() == "POINT1_Z":
                point1_Z = line[2]
            if line[0].upper() == "POINT2_X":
                point2_X = line[2]
            if line[0].upper() == "POINT2_Y":
                point2_Y = line[2]
            if line[0].upper() == "POINT2_Z":
                point2_Z = line[2]
            if line[0].upper() == "UNIT":
                unit = line[2]

        try:
            return float(R), int(N), float(distance), float(field_strength), name, out_format, float(point1_X), \
                   float(point1_Y), float(point1_Z), float(point2_X), float(point2_Y), float(point2_Z), str(unit)
        except:
            print("INVALID/MISSING PARAMETER ENCOUNTERED DURING CPC INPUT READ \n \n")
            self.exception_message()

    def read_input_sl(self):
        """ read parameters for SL calculation. """
        for line in self.line_list:
            if line[0].upper() == "RADIUS":
                radius = line[2]
            if line[0].upper() == "N":
                N = line[2]
            if line[0].upper() == "STEP":
                step = line[2]
            if line[0].upper() == "CHIRALITY":
                chirality = line[2]
            if line[0].upper() == "NAME":
                name = line[2]
            if line[0].upper() == "FATOM":
                fatom = line[2]
            if line[0].upper() == "SEQUENCE":
                sequence = line[2]
            if line[0].upper() == "CHARGE":
                charge = line[2]
            if line[0].upper() == "POINT_X":
                point_X = line[2]
            if line[0].upper() == "POINT_Y":
                point_Y = line[2]
            if line[0].upper() == "POINT_Z":
                point_Z = line[2]
            if line[0].upper() == "UNIT":
                unit = line[2]

        try:
            return float(radius), int(N), float(step), str(chirality), str(name), int(fatom), str(sequence), \
                   float(charge), float(point_X), float(point_Y), float(point_Z), str(unit)
        except:
            print("INVALID/MISSING PARAMETER ENCOUNTERED DURING SL INPUT READ \n \n")
            self.exception_message()

    def read_input_quantification(self):
        """ read parameters for EF quantification """
        for line in self.line_list:
            if line[0].upper() == "UNIT":
                unit = line[2]
            if line[0].upper() == "FILE_TYPE":
                file_type = line[2]
            if line[0].upper() == "NAME":
                name = line[2]
            if line[0].upper() == "CHARGE_SELECT":
                charge_select = line[2]
            if line[0].upper() == "CHARGE_SEQ":
                charge_seq = line[2]
            if line[0].upper() == "DIRECTION":
                direction = line[2]

        if charge_select == "ALL":
            charge_seq = "/"

        if direction.upper() == "MANUAL":
            v1x, v1y, v1z, v2x, v2y, v2z, point_x, point_y, point_z = self.read_input_quantification_manual()
        elif direction.upper() == "SELECT":
            v1x, v1y, v1z, v2x, v2y, v2z, point_x, point_y, point_z = self.read_input_quantification_select()

        try:
            return str(unit), str(file_type), str(name), str(charge_select), str(charge_seq), str(direction), \
                   float(v1x), float(v1y), float(v1z), float(v2x), float(v2y), float(v2z), float(point_x), \
                   float(point_y), float(point_z)
        except:
            print("INVALID/MISSING PARAMETER ENCOUNTERED DURING QUANT INPUT READ \n \n")
            self.exception_message()

    def read_input_quantification_manual(self):
        """ in case DIRECTION = MANUAL was selected, the direction vector parameters have to be read """
        for line in self.line_list:
            if line[0].upper() == "V1X":
                v1x = line[2]
            if line[0].upper() == "V1Y":
                v1y = line[2]
            if line[0].upper() == "V1Z":
                v1z = line[2]
            if line[0].upper() == "V2X":
                v2x = line[2]
            if line[0].upper() == "V2Y":
                v2y = line[2]
            if line[0].upper() == "V2Z":
                v2z = line[2]
            if line[0].upper() == "POINT_X":
                point_x = line[2]
            if line[0].upper() == "POINT_X":
                point_y = line[2]
            if line[0].upper() == "POINT_Z":
                point_z = line[2]
        try:
            return float(v1x), float(v1y), float(v1z), float(v2x), float(v2y), float(v2z), float(point_x), \
                   float(point_y), float(point_z)
        except:
            print("INVALID/MISSING PARAMETER ENCOUNTERED DURING QUANT(MANUAL) INPUT READ \n \n")
            self.exception_message()

    def read_input_quantification_select(self):
        """
        in case DIRECTION = SELECT was selected, the coordination file and atom numbers determining the direction vector
        parameters have to be read
        """
        for line in self.line_list:
            if line[0].upper() == "DIRECTION_FILE":
                direction_file = line[2]
            if line[0].upper() == "ATOM1":
                atom1 = line[2]
            if line[0].upper() == "ATOM2":
                atom2 = line[2]
            if line[0].upper() == "ATOM_CENTER":
                atom_center = line[2]

        v1x, v1y, v1z, v2x, v2y, v2z, point_x, point_y, point_z = \
            self.determine_direction(direction_file, atom1, atom2, atom_center)

        try:
            return float(v1x), float(v1y), float(v1z), float(v2x), float(v2y), float(v2z), float(point_x), \
                   float(point_y), float(point_z)
        except:
            print("INVALID/MISSING PARAMETER ENCOUNTERED DURING QUANT(SELECT) INPUT READ \n \n")
            self.exception_message()

    def determine_direction(self, direction_file, atom1, atom2, atom_center):
        """ Determine direction from atom positions in DIRECTION_FILE """
        content_list = self.read_direction_file(direction_file)
        for i in range(len(content_list)):
            if (i == int(atom1) - 1):
                v1x = content_list[i][1]
                v1y = content_list[i][2]
                v1z = content_list[i][3]
            elif (i == int(atom2) - 1):
                v2x = content_list[i][1]
                v2y = content_list[i][2]
                v2z = content_list[i][3]
            else:
                pass
            if (i == int(atom_center) - 1):
                point_x = content_list[i][1]
                point_y = content_list[i][2]
                point_z = content_list[i][3]
            else:
                pass

        try:
            return float(v1x), float(v1y), float(v1z), float(v2x), float(v2y), float(v2z), float(point_x), \
                   float(point_y), float(point_z)
        except:
            print("INVALID/MISSING PARAMETER ENCOUNTERED DURING QUANT(SELECT - DIRECTION DETERMINATION) INPUT READ \n \n")
            self.exception_message()

    def read_direction_file(self, direction_file):
        """ Read the DIRECTION_FILE """
        content_list = []
        with open(direction_file + ".txt", "r", encoding="utf-8") as file_point:
            for line in file_point:
                content_list.append(list(line.split()))
                if not line.split():
                    continue
        file_point.close()

        return content_list

    def read_input_log(self):
        """ reads the additional parameters in case the starting point for EF quantification is a .log file """
        for line in self.line_list:
            if line[0].upper() == "TYPE_OF_CHARGES":
                type_of_charges = line[2]

        try:
            return str(type_of_charges)
        except:
            print("INVALID/MISSING PARAMETER ENCOUNTERED DURING QUANT(LOG) INPUT READ \n \n")
            self.exception_message()

    def read_input_pdb(self):
        """ reads the additional parameters in case the starting point for EF quantification is a .pdb file """
        for line in self.line_list:
            if line[0].upper() == "FORCE_FIELD":
                force_field = line[2]
            if line[0].upper() == "N_TERMINAL":
                n_terminal = line[2]
            if line[0].upper() == "C_TERMINAL":
                c_terminal = line[2]

        try:
            return str(force_field), int(n_terminal), int(c_terminal)
        except:
            print("INVALID/MISSING PARAMETER ENCOUNTERED DURING QUANT(PDB) INPUT READ \n \n")
            self.exception_message()

    def read_input_charmm(self):
        """
        read the additional parameters in case the selected force field for the charge distribution to be extracted
        from the .pdb file is CHARMM
        """
        for line in self.line_list:
            if line[0].upper() == "ASPP":
                try:
                    aspp = line[2].split(",")
                except:
                    aspp = []
            if line[0].upper() == "GLUP":
                try:
                    glup = line[2].split(",")
                except:
                    glup = []
            if line[0].upper() == "DISU":
                try:
                    disu = line[2].split(",")
                except:
                    disu = []
        try:
            return list(map(int, aspp)), list(map(int, glup)), list(map(int, disu))
        except:
            print("INVALID/MISSING PARAMETER ENCOUNTERED DURING QUANT(PDB - CHARMM) INPUT READ \n \n")
            self.exception_message()

    def exception_message(self):
        """ message shown in terminal in case keywords were not retrieved correctly. """
        print ("ERROR: INVALID/INSUFFICIENT KEYWORDS in " + self.filename)
        print (" ")
        print (" ----- ERROR TERMINATION OF TITAN AT " + str(_datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " -----")
        _sys.exit()