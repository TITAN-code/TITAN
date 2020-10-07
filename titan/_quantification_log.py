from titan._quantification import Quantification as _Quantification

#__all__ = ['QuantificationLog']

class QuantificationLog(_Quantification):
    """
    A class that represents a quantification calculation starting from a .log file

    Attributes:
    ----------
    name : string
        The name of the input and output files
    point_x : float
        The x-coordinate of the point at which the electric field will be quantified
    point_y : float
        The y-coordinate of the point at which the electric field will be quantified
    point_z : float
        The z-coordinate of the point at which the electric field will be quantified
    v1_x : float
        The x-coordinate of the first point making up the direction vector
    v1_y : float
        The y-coordinate of the first point making up the direction vector
    v1_z : float
        The z-coordinate of the first point making up the direction vector
    v2_x : float
        The x-coordinate of the second point making up the direction vector
    v2_y : float
        The y-coordinate of the second point making up the direction vector
    v2_z : float
        The z-coordinate of the second point making up the direction vector
    charge_seq : string
        The charge sequence, in which the range from charge/atom x to y is denoted by R(x,y) and individual
        charges/atoms are denoted by P, i.e. P(x); "+" signs are used to catenate ranges and points (default = "/")
    charge_select: string
        Keyword indicating whether all charges/atoms or only part are considered during the quantification
        (2 options: "ALL" or "PART"; default = "ALL")
    unit : string
        The unit used in the calculation (angstrom = "ANS", bohr = "BOHR"; default = "ANS")

    Methods:
    -------
    execute : executes the workflow associated to the quantification calculation
    """
    def __init__(self, name, point_x, point_y, point_z, v1_x, v1_y, v1_z, v2_x, v2_y, v2_z, charge_seq="/",
                 charge_select="ALL", unit="ANS"):
        _Quantification.__init__(self, name, point_x, point_y, point_z, v1_x, v1_y, v1_z, v2_x, v2_y, v2_z, charge_seq,
                   charge_select, unit)

    def execute(self):
        """
        executes the workflow associated to the quantification calculation
        """
        elements = self.import_point_charges_from_log_file()
        self.write_save_file(elements)
        efx, efy, efz, ef_tot, oef = self.quantify_selected_charge_distribution()
        self.charge_distribution_to_quantify.write_point_charge_list_to_txt_file(self.name)
        self.write_output_quantification_calculation(efx, efy, efz, ef_tot, oef)

    def import_point_charges_from_log_file(self):
        """ constructs the charges_list_from_log """
        line_list = self.obtain_line_list()
        charges = self.retrieve_charges(line_list)
        coordinates, elements = self.retrieve_coordinates_and_element_list(line_list)

        for i in range(len(coordinates)):
            self.full_charge_distribution.point_charge_list.append([coordinates[i], charges[i]])

        return elements

    def write_save_file(self, elements):
        """ constructs the .save file containing the element names as well as the point-charges """
        i = 0
        with open(self.name + ".save", "w", encoding="utf-8") as save_file:
            for point_charge in self.full_charge_distribution.point_charge_list:
                save_file.write("%3s   %8.5f     %8.5f     %8.5f     %8.3f \n" % (
                    elements[i], point_charge[0][0], point_charge[0][1], point_charge[0][2], point_charge[1]))
                i += 1
        save_file.close()

    def retrieve_charges(self, line_list):
        """ extracts charges from line_list and returns the charges-list """
        start_list, end_list = self.determine_charges_block(line_list)
        total_number_of_blocks = len(start_list)
        start = start_list[total_number_of_blocks - 3]
        end = end_list[total_number_of_blocks - 3]

        charges = []

        for i in range(start, end):
            charges.append(float(line_list[i].split()[2]))

        return charges

    def retrieve_coordinates_and_element_list(self, line_list):
        """
        extracts coordinates and element names from line_list and returns the coordinates-list and the elements-list
        """
        start, end = self.determine_geometry_block(line_list)

        coordinates = []
        elements = []

        for i in range(start, end):
            coordinates.append([float(line_list[i].split()[3]), float(line_list[i].split()[4]),
                                float(line_list[i].split()[5])])
            elements.append(self.element_name_conversion(line_list[i].split()[1]))

        return coordinates, elements

    def element_name_conversion(self, element_number):
        """ converts element number to element name """
        element_dictionary = {1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne',
                              11: 'Na', 12: 'Mg', 13: 'Al', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K',
                              20: 'Ca', 21: 'Sc', 22: 'Ti', 23: 'V', 24: 'Cr', 25: 'Mn', 26: 'Fe', 27: 'Co',
                              28: 'Ni', 29: 'Cu', 30: 'Zn', 31: 'Ga', 32: 'Ge', 33: 'As', 34: 'Se', 35: 'Br', 36: 'Kr',
                              37: 'Rb', 38: 'Sr', 39: 'Y', 40: 'Zr', 41: 'Nb', 42: 'Mo', 43: 'Tc', 44: 'Ru', 45: 'Rh',
                              46: 'Pd', 47: 'Ag', 48: 'Cd', 49: 'In', 50: 'Sn', 51: 'Sb', 52: 'Te', 53: 'I', 54: 'Xe',
                              55: 'Cs', 56: 'Ba', 57: 'La', 72: 'Hf', 73: 'Ta', 74: 'W', 75: 'Re', 76: 'Os', 77: 'Ir',
                              78: 'Pt', 79: 'Au', 80: 'Hg', 81: 'Tl', 82: 'Pb', 83: 'Bi', 84: 'Po', 85: 'At', 86: 'Rn'}

        try:
            element_name = element_dictionary[int(element_number)]
        except:
            element_name = element_number
            print('UNKNOWN ELEMENT NUMBER!')

        return element_name

    def obtain_line_list(self):
        """ construct line_list from .log file """
        with open(self.name + ".log", "r", encoding="utf-8") as input_file:
            content = input_file.read()
            line_list = content.split("\n")
        input_file.close()

        return line_list

    def determine_geometry_block(self, line_list):
        """ Determine start and end of the geometry block. Verify the exact ending of the geometry block """
        counter = 0
        for line in line_list:
            counter += 1
            if 'Input orientation:' in line:
                start = counter + 4
            elif 'Standard orientation:' in line:
                end = counter - 8
            elif 'Distance matrix (angstroms):' in line:
                end_alternative = counter - 2
            else:
                pass

        # in case end has not yet been assigned, look for
        try:
            end
        except:
            counter2 = 0
            for line in line_list:
                counter2 += 1
                if 'Rotational constants (GHZ)' in line:
                    end = counter2 - 2

        block_length = end - start
        try:
            block_length_alternative = end_alternative - start
        except:
            block_length_alternative = block_length + 1

        if block_length < block_length_alternative:
            return start, end
        else:
            return start, end_alternative

    def determine_charges_block(self, line_list):
        """ Determine start and end positions of the geometry blocks """
        start_list = []
        end_list = []

        counter = 0
        for line in line_list:
            counter += 1
            if 'Summary of Natural Population Analysis:' in line:
                start_list.append(counter + 5)
            elif '   Atom  No          Natural Electron Configuration' in line:
                if "   Effective Core  " in line_list[counter-8]:
                    end_list.append(counter - 13)
                else:
                    end_list.append(counter - 12)
            else:
                pass

        return start_list, end_list