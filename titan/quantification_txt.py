from titan.quantification import Quantification
from titan.myimports import *

class QuantificationTxt(Quantification):
    """
    A class that represents a quantification calculation starting from a .txt file

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
        Quantification.__init__(self, name, point_x, point_y, point_z, v1_x, v1_y, v1_z, v2_x, v2_y, v2_z, charge_seq,
                   charge_select, unit)

    def execute(self):
        """
        executes the workflow associated to the quantification calculation
        """
        self.import_point_charges_from_txt_file()
        efx, efy, efz, ef_tot, oef = self.quantify_selected_charge_distribution()
        self.write_output_quantification_calculation(efx, efy, efz, ef_tot, oef)

    def import_point_charges_from_txt_file(self):
        """
        reads coordinates and charges for all the point-charges from a .txt file and stores them in an auxiliary list
        """
        content = self.read_coordinates_and_charges_from_txt()
        number_of_point_charges = len(content)
        for i in range(number_of_point_charges):
            self.full_charge_distribution.point_charge_list.append(
                [[content[i][0], content[i][1], content[i][2]], content[i][3]])

    def read_coordinates_and_charges_from_txt(self):
        """ reads coordinates and charges from .txt file to quantify local electric field """
        content = []
        with open(self.name + ".txt", "r", encoding="utf-8") as input_file:
            for line in input_file:
                content.append(list(map(float, line.split())))
                if not line.split():
                    continue
        input_file.close()

        return content