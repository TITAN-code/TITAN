import titan.general_charge_distribution_class as general
import titan.header as header
from titan.myimports import *

class Quantification():
    """
    A class that represents a quantification calculation

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
        self.name = name
        self.point_x = point_x
        self.point_y = point_y
        self.point_z = point_z
        self.v1_x = v1_x
        self.v1_y = v1_y
        self.v1_z = v1_z
        self.v2_x = v2_x
        self.v2_y = v2_y
        self.v2_z = v2_z
        self.charge_seq = charge_seq
        self.charge_select = charge_select
        self.unit = unit

        self.vector_x, self.vector_y, self.vector_z = self.construct_vector()

        self.charge_distribution_to_quantify = general.ChargeDistribution()
        self.full_charge_distribution = general.ChargeDistribution()

    def execute(self):
        """
        executes the workflow associated to the quantification calculation
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def quantify_selected_charge_distribution(self):
        """
        quantifies the electric field exerted by the selected charge distribution, starting from the full one
        """
        self.charge_distribution_to_quantify.construct_point_charge_list(
            self.full_charge_distribution.point_charge_list, self.charge_seq, self.charge_select)
        efx, efy, efz, ef_tot = self.charge_distribution_to_quantify.calculate_electric_field(self.point_x, self.point_y,
                            self.point_z, self.unit)
        oef = self.charge_distribution_to_quantify.calculate_oriented_electric_field(self.point_x, self.point_y,
                            self.point_z, self.vector_x, self.vector_y, self.vector_z, self.unit)

        return efx, efy, efz, ef_tot, oef

    def construct_vector(self):
        """ constructs the direction vector """
        vector_x = self.v2_x - self.v1_x
        vector_y = self.v2_y - self.v1_y
        vector_z = self.v2_z - self.v1_z

        return vector_x, vector_y, vector_z

    def write_output_quantification_calculation(self, efx, efy, efz, ef_tot, oef):
        """ write output of quantification calculation to .ef file """
        f1 = open(self.name + ".ef", "w")
        header.header_output_file(f1)
        f1.write(" \n")
        f1.write(" \n")
        f1.write("-----------------------------------------------------------\n")
        f1.write(" \n")
        f1.write("          ELECTRIC FIELD STRENGTH QUANTIFICATION\n")
        f1.write(" \n")
        f1.write("-----------------------------------------------------------\n")
        f1.write(" \n")
        f1.write(" \n")
        if self.unit.upper() == "BOHR":
            f1.write(" THE UNIT OF LENGTH IS BOHR\n")
        elif self.unit.upper() == "ANS":
            f1.write(" THE UNIT OF LENGTH IS ANGSTROM\n")
        f1.write(" \n")
        f1.write(" \n")
        f1.write("-----------------------------------------------------------\n")
        f1.write(" \n")
        f1.write("                      CHARGE DISTRIBUTION\n")
        f1.write(" \n")
        f1.write("-----------------------------------------------------------\n")
        f1.write(" \n")
        f1.write(" THE CHARGE DISTRIBUTION IS SHOWN IN THE FILE %s.txt. \n" % (self.name))
        f1.write(" \n")
        f1.write(" THERE ARE %d POINT CHARGES IN THIS CHARGE DISTRIBUTION. \n" % (
            len(self.charge_distribution_to_quantify.point_charge_list)))
        f1.write(" \n")
        f1.write(" \n")
        f1.write("-----------------------------------------------------------\n")
        f1.write(" \n")
        f1.write("             THE STRENGTH OF THE ELECTRIC FIELD\n")
        f1.write(" \n")
        f1.write("-----------------------------------------------------------\n")
        f1.write(" \n")
        f1.write(" THE STRENGTH OF THE ELECTRIC FIELD AT POINT (%.10f, %.10f, %.10f) : \n" % (
            self.point_x, self.point_y, self.point_z))
        f1.write(" \n")
        f1.write(" X-COMPONENT OF THE EF: %.10f  A.U.;\n" % (efx))
        f1.write(" Y-COMPONENT OF THE EF: %.10f  A.U.;\n" % (efy))
        f1.write(" Z-COMPONENT OF THE EF: %.10f  A.U.;\n" % (efz))
        f1.write(" TOTAL STRENGTH OF THE EF: %.10f  A.U..\n" % (ef_tot))
        f1.write(" \n")
        f1.write(" \n")
        f1.write(" \n")
        f1.write("--------------------------------------------------------------\n")
        f1.write(" \n")
        f1.write("  THE STRENGTH OF THE ELECTRIC FIELD ALONG DIRECTION VECTOR V\n")
        f1.write(" \n")
        f1.write( "--------------------------------------------------------------\n")
        f1.write(" \n")
        f1.write(" \n")
        f1.write(" THE DIRECTION VECTOR  V  (%.10f,  %.10f,  %.10f), \n" % (self.vector_x, self.vector_y, self.vector_z))
        f1.write(" DEFINED FROM POINT V1(%.10f,  %.10f,  %.10f)\n" % (self.v1_x, self.v1_y, self.v1_z))
        f1.write(" TO V2(%.10f,  %.10f,  %.10f)\n" % (self.v2_x, self.v2_y, self.v2_z))
        f1.write(" \n")
        f1.write(" \n")
        f1.write(" THE STRENGTH OF THE EF ORIENTED ALONG THE DIRECTION VECTOR V IS %.10f A.U.\n" % (oef))
        f1.write(" \n")
        f1.write(" \n")
        f1.write(" THE ELECTRIC FIELD HAS SUCCESSFULLY BEEN QUANTIFIED\n")
        f1.write(" \n")
        f1.write(" \n")
        header.conclusion_output_file(f1)
        f1.close()