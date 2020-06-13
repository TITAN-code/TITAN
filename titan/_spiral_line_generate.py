import titan._header as _header
from titan._charge_distribution_class_gen import ChargeDistributionSl as _ChargeDistributionSl
import os as _os
import math as _math
import datetime as _datetime

#__all__ = ['SpiralLineGenerate']

class SpiralLineGenerate():
    """
    A class to represent a spiral line charge distribution generation

    Attributes:
    ----------
    name : string
        The name of the output files (name.info, name.pdb, etc.)
    sequence: string
        The sequence of the charges in the spiral line. The sequence has to consist of a succession of "P"
        and "N" fragments (the number of "P" and "N" fragments should be equal in order to make sure that
        the net charge of the spiral line is zero)
    fatom : int
        The number of dummy atoms included in a single "P" or "N" fragment
    charge : int
        The charge of each dummy atom
    radius : float
        The radius of the spiral line distribution (in Angstrom)
    step : float
        The pitch between two neighboring atoms (in Angstrom)
    N : int
        The total numbers of atoms included in one full circle.
    chirality : string
        The chirality of the spiral line (options: "RIGHT-HAND" or "LEFT-HAND")
    point_X : float
        The x-coordinate of the point at which the electric field will be calculated
    point_Y : float
        The y-coordinate of the point at which the electric field will be calculated
    point_Z : float
        The z-coordinate of the point at which the electric field will be calculated
    unit : str
        The unit used in the calculation (angstrom = "ANS", bohr = "BOHR"; default = "ANS")

    Methods:
    --------

    create_plates : creates the plates and writes them to the respective input files
    """

    def __init__(self, sequence, fatom, charge, radius, step, N, chirality, point_X, point_Y, point_Z, name, unit="ANS"):
        self.name = name
        self.sequence = sequence
        self.fatom = fatom
        self.charge = charge
        self.radius = radius
        self.step = step
        self.N = N
        self.chirality = chirality
        self.point_X = point_X
        self.point_Y = point_Y
        self.point_Z = point_Z
        self.unit = unit

        self.charge_distribution_sl = _ChargeDistributionSl()

    def create_spiral_line_distribution(self):
        """
        Creates the spiral line charge distribution and writes it to the output files
        """
        # set the initial settings
        n_L, iter, x_sum, y_sum, z_sum, theta, X0, Y0, Z0 = self.initialize_line_settings()

        # determine the geometrical center and construct the spiral line distribution
        x_arg, y_arg, z_arg = self.determine_geometrical_center(iter, theta, Z0, x_sum, y_sum, z_sum)
        pitch = self.construct_spiral_line_distribution(n_L, iter, x_arg, y_arg, z_arg, theta)

        # write point_charge_list to output-file
        self.charge_distribution_sl.write_point_charge_list(self.name, self.fatom)

        # calculate electric field strength
        efx, efy, efz, ef_tot = self.charge_distribution_sl.calculate_electric_field(self.point_X, self.point_Y,
                                                                                   self.point_Z, self.unit)

        # write a summary of the entire calculation
        self.summary(efx, efy, efz, ef_tot, pitch, len(self.charge_distribution_sl.point_charge_list))

        # move the output to a dedicated folder
        self.move_output()

    def initialize_line_settings(self):
        """
        Sets the variables needed in the spiral line charge distribution construction
        """
        n_L = int(len(self.sequence)*self.fatom)
        iter = range(1,len(self.sequence) + 1)

        x_sum = 0.0
        y_sum = 0.0
        z_sum = 0.0

        theta = 0.0

        X0 = self.radius
        Y0 = 0.0
        Z0 = (-1.0) * n_L * self.step / 2.0

        return n_L, iter, x_sum, y_sum, z_sum, theta, X0, Y0, Z0

    def determine_geometrical_center(self, iter, theta, Z0, x_sum, y_sum, z_sum):
        """
        Determines the geometrical center of the spiral line distribution (x_arg, y_arg, z_arg) so that the
        charge distribution can be centered around this point
        """
        count = 1
        for i in iter:
            for j in range(1, self.fatom + 1):
                k = self.fatom * i + j - self.fatom - 1
                b = _math.cos(theta)
                c = _math.sin(theta)

                x = self.radius * b
                y = self.radius * c
                z = Z0 + self.step * k

                count += 1
                x_sum += x
                y_sum += y
                z_sum += z

                j += 1
                theta = self.update_theta(theta)
            i += 1

        x_arg = x_sum/float(count - 1)
        y_arg = y_sum/float(count - 1)
        z_arg = z_sum/float(count - 1)

        return x_arg, y_arg, z_arg

    def construct_spiral_line_distribution(self, n_L, iter, x_arg, y_arg, z_arg, theta):
        """
        constructs the actual spiral line charge distribution, centered around (0,0,0)
        """
        Z0 = ((-1.0) * n_L * self.step / 2.0) - z_arg
        for i in iter:
            for j in range(1,self.fatom+1):
                (type_a, type_r, charge_a) = self.frag(self.sequence[i-1], j, self.charge)
                k = self.fatom*i + j - self.fatom - 1
                b = _math.cos(theta)
                c = _math.sin(theta)

                x = self.radius * b - x_arg
                y = self.radius * c - y_arg
                z = Z0 + self.step * k

                self.charge_distribution_sl.append_point_charge(x, y, z, charge_a, type_a, type_r)

                j += 1
                theta = self.update_theta(theta)
            i += 1

        pitch = z - Z0

        return pitch

    def update_theta(self, theta):
        """
        Updates theta according to whether the spiral line is right- or left-handed
        """
        if self.chirality.upper() == "RIGHT-HAND":
            theta += (2 * _math.pi) / self.N
        elif self.chirality.upper() == "LEFT-HAND":
            theta -= (2 * _math.pi) / self.N

        return theta

    def frag(self, res, j, charge):
        """ Define the nature of the point-charge """
        if (res.upper() == "P"):
            if (j <= 1000):
                type_a = "P" + str(j - 1)
            elif (j <= 2000):
                str_j = str(j - 1)
                type_a = "O" + str_j[-3:]
            elif (j <= 3000):
                str_j = str(j - 1)
                type_a = "S" + str_j[-3:]
            else:
                str_j = str(j - 1)
                type_a = "T" + str_j[-3:]
            type_r = "PCSL"
            charge = charge
        elif (res.upper() == "N"):
            if (j <= 1000):
                type_a = "N" + str(j - 1)
            elif (j <= 2000):
                str_j = str(j - 1)
                type_a = "E" + str_j[-3:]
            elif (j <= 3000):
                str_j = str(j - 1)
                type_a = "G" + str_j[-3:]
            else:
                str_j = str(j - 1)
                type_a = "A" + str_j[-3:]
            type_r = "NCSL"
            charge = 0.00 - charge
        else:
            print("ERROR: INVALID FRAGMENT IN THE SEQUENCE! \n")
            print("FRAGMENTS SHOULD BE EITHER \"N\" OR \"P\"")
            print("ERROR TERMINATION OF TITAN AT " + str(_datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            print("\n                                                                 ")
            _os.exit()

        return (type_a, type_r, charge)

    def move_output(self):
        """ move output to the right location """
        file = _os.getcwd()
        path = file + "/GAUSSIAN_FORMAT_SL"
        self.check_directory(path)
        self.move_gauss()

    def check_directory(self, directory):
        """ creates the directory if it doesn't already exist """
        check = _os.path.exists(directory)
        if not check:
            _os.makedirs(directory)

    def move_gauss(self):
        """ moves the output to ./GAUSSIAN_FORMAT_CPC """
        info = self.name + ".info"
        pdb = self.name + ".pdb"
        txt = self.name + ".txt"
        dent_info = "./GAUSSIAN_FORMAT_SL/" + info
        dent_pdb = "./GAUSSIAN_FORMAT_SL/" + pdb
        dent_txt = "./GAUSSIAN_FORMAT_SL/" + txt
        _os.rename(info, dent_info)
        _os.rename(pdb, dent_pdb)
        _os.rename(txt, dent_txt)

    def summary(self, efx, efy, efz, ef_tot, pitch, number_of_charges):
        """
        Writes the summary of the calculation to the .info output-file
        """
        f2 = open(self.name + ".info", "w", encoding="utf-8")
        _header.header_output_file(f2)
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write("------------------------------------------------------------------ \n")
        f2.write(" \n")
        f2.write("               EXTERNAL SPIRAL LINE CHARGE GENERATION \n")
        f2.write(" \n")
        f2.write("------------------------------------------------------------------- \n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" THE EEF IS GENERATED IN GAUSSIAN FORMAT \n")
        f2.write(" WITH A COPY OF THE POSITIONS ALSO IN PDB FORMAT. \n")
        f2.write(" \n")
        if self.unit.upper() == "BOHR":
            f2.write(" THE UNIT OF LENGTH IS BOHR\n")
        elif self.unit.upper() == "ANS":
            f2.write(" THE UNIT OF LENGTH IS ANGSTROM\n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write("------------------------------------------------------------------ \n")
        f2.write("                     CHARGES OF FRAGMENT \n")
        f2.write("------------------------------------------------------------------ \n")
        f2.write(" ")
        f2.write(" THE CHARGES OF IN THE POINTS OF THE \"P\" FRAGMENT ARE %9.6f. \n" % (self.charge))
        f2.write(" THE CHARGES OF IN THE POINTS OF THE \"N\" FRAGMENT ARE %9.6f. \n" % (0.00 - self.charge))
        f2.write(" \n")
        f2.write(" \n")
        f2.write("-------------------------------- \n")
        f2.write("   FRAGMENT  | ATOM | CHARGE    \n")
        f2.write("             | TYPE |           \n")
        f2.write("-------------------------------- \n")
        f2.write("             |  P0  | %10.6f \n" % (self.charge))
        f2.write("   FRAGMENT  |  P1  | %10.6f \n" % (self.charge))
        f2.write("      P      |  P2  | %10.6f \n" % (self.charge))
        f2.write("             |  P3  | %10.6f \n" % (self.charge))
        f2.write("             |  P4  | %10.6f \n" % (self.charge))
        f2.write("             |   .  |    . \n")
        f2.write("             |   .  |    . \n")
        f2.write("             |   .  |    . \n")
        f2.write("--------------------------------- \n")
        f2.write("             |  N0  | %10.6f \n" % (0.00 - self.charge))
        f2.write("   FRAGMENT  |  N1  | %10.6f \n" % (0.00 - self.charge))
        f2.write("      N      |  N2  | %10.6f \n" % (0.00 - self.charge))
        f2.write("             |  N3  | %10.6f \n" % (0.00 - self.charge))
        f2.write("             |  N4  | %10.6f \n" % (0.00 - self.charge))
        f2.write("             |   .  |    . \n")
        f2.write("             |   .  |    . \n")
        f2.write("             |   .  |    . \n")
        f2.write("--------------------------------- \n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write("------------------------------------------------------------------ \n")
        f2.write("                           GAUSSIAN INPUT \n")
        f2.write("------------------------------------------------------------------ \n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" THE EXTERNAL CHARGES ARE AVAILABLE IN %.10s.txt FILE. \n" % (self.name))
        f2.write(" PLEASE USE \"CHARGE\" KEYWORDS IN GAUSSIAN 09 CALCULATION. \n")
        f2.write(" \n")
        f2.write(" FORMAT: \n")
        f2.write("     X_COORDINATE    Y_COORDINATE    Z_COORDINATE    CHARGE \n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" IF YOU WANT TO VISUALIZE THE SPIRAL LINE CHARGE DISTRIBUTION GENERATED, \n")
        f2.write(" PLEASE SEE %.10s.pdb FILE. \n" % (self.name))
        f2.write(" \n")
        f2.write(" \n")
        f2.write("------------------------------------------------------------------ \n")
        f2.write("                       ELECTRIC FIELD \n")
        f2.write("------------------------------------------------------------------ \n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" THE GEOMETRICAL CENTER OF THE POINT CHARGE DISTRIBUTION IS LOCATED AT (0,0,0) \n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" THE ELECTRIC FIELD (EF) AT (%9.6f, %9.6f, %9.6f) IS : \n" % (self.point_X, self.point_Y, self.point_Z))
        f2.write(" X-COMPONENT OF EF: %9.6f  A.U.; \n" % (efx))
        f2.write(" Y-COMPONENT OF EF: %9.6f  A.U.; \n" % (efy))
        f2.write(" Z-COMPONENT OF EF: %9.6f  A.U.; \n" % (efz))
        f2.write(" TOTAL VALUE OF EF: %9.6f  A.U.. \n" % (ef_tot))
        f2.write(" \n")
        f2.write("------------------------------------------------------------------ \n")
        f2.write("                       SUMMARY: \n")
        f2.write("------------------------------------------------------------------ \n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write("  The spiral line is generated in %.10sed chirality. \n" % (self.chirality))
        f2.write(" The pitch of the spiral line is %8.4f Angstrom. \n" % (pitch))
        f2.write(" The radius of the spiral line is %8.4f Angstrom. \n" % (self.radius))
        f2.write(" The line contains %6d point charges in total. \n" % (number_of_charges))
        f2.write(" The sequence is the following: \n")
        f2.write(" \" %.10000000s \". \n" % (self.sequence))
        f2.write(" \n")
        f2.write(" There are %d points in the fragment of \"P\" or \"N\". \n" % (self.fatom))
        f2.write(
                        " The charges of each points are %9.6f and %9.6f for the fragments. \n" % (
                            self.charge, 0.00 - self.charge))
        f2.write(" of \"P\" and \"N\" respectively. \n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" THE GAUSSIAN EXTERNAL CHARGE OF TWO SPIRAL LINES IS SHOWN IN %.10s.txt \n" % (self.name))
        f2.write(" THE PDB FILE FOR THE SPIRAL LINE IS %.10s.pdb \n" % (self.name))
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" THE ELECTRIC FIELD HAS BEEN SUCCESSFULLY GENERATED. \n")
        f2.write(" \n")
        _header.conclusion_output_file(f2)
        f2.close()
