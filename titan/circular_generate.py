import titan.header as header
from titan.charge_distribution_class_gen import ChargeDistributionCpc
from titan.myimports import *

class CircularGenerate():
    """
    A class to represent a uniform field generation with the help of circular plates

    Attributes:
    ----------
    point1_X -> point2_Z : float
        The coordinates of the axis along which the uniform field
    R : float
        The increase in radius between each successive ring in the circular plate charge distribution (in A)
    N : int
        The total number of circular rings in the plate
    distance : float
        The distance between the center of the plate and the point at which the electric field
        should be calculated (in A)
    field_strength : float
        The desired field strength (in au)
    name : str
        The name for the output files
    unit : str
        The unit used in the calculation (angstrom = "ANS", bohr = "BOHR"; default = "ANS")

    Methods:
    --------

    create_plates : creates the plates and writes them to the respective input files
    """
    initial_charge = 1.00  # initial charge; will be updated once the charged plates have been constructed

    def __init__(self, point1_X, point1_Y, point1_Z, point2_X, point2_Y, point2_Z, R, N, distance, field_strength, name,
                 unit="ANS"):
        self.point1_X = float(point1_X)
        self.point1_Y = float(point1_Y)
        self.point1_Z = float(point1_Z)
        self.point2_X = float(point2_X)
        self.point2_Y = float(point2_Y)
        self.point2_Z = float(point2_Z)
        self.R = float(R)
        self.N = float(N)
        self.radius = float(self.R)*float(self.N)
        self.distance = float(distance)
        self.field_strength = float(field_strength)
        self.name = name
        self.unit = unit

        self.initial_oef = 0.0

        self.V_X, self.V_Y, self.V_Z, self.unit_vector = self.initialize_vector()

        self.charge_distribution_cpc = ChargeDistributionCpc()

    def initialize_vector(self):
        """
        Initializes the vector from point1 -> point2

        :returns

        V_X,V_Y,V_Z : float
            The vector components
        unit vector : tuple
            The unit vector
        """
        V_X = self.point2_X - self.point1_X
        V_Y = self.point2_Y - self.point1_Y
        V_Z = self.point2_Z - self.point1_Z

        unit_vector = self.normalize_vector(V_X, V_Y, V_Z)

        return V_X, V_Y, V_Z, unit_vector

    def create_and_write_plates(self, out_format):
        """
        Creates the positive and negative plates and writes them to output files
        """
        # create the plates
        self.create_plate("pos")
        self.create_plate("neg")

        # determine the final field strengths
        self.initial_oef = self.charge_distribution_cpc.calculate_oriented_electric_field(
            self.point1_X, self.point1_Y, self.point1_Z, self.V_X, self.V_Y, self.V_Z, self.unit)

        final_charge = self.field_strength / self.initial_oef

        # update charge and write charge_distribution
        self.charge_distribution_cpc.update_charges(final_charge)
        self.charge_distribution_cpc.write_point_charge_list(out_format, self.name)

        # write a summary of the entire calculation
        self.summary(out_format, final_charge, len(self.charge_distribution_cpc.point_charge_list))

        # move the output to a dedicated folder
        self.move_output(out_format)

    def create_plate(self, charge):
        """
        Create a single plate
        """
        if charge == "pos":
            factor = -1.0
        else:
            factor = 1.0

        # Set center of plate
        X0 = factor * self.distance * self.unit_vector[0] + self.point1_X
        Y0 = factor * self.distance * self.unit_vector[1] + self.point1_Y
        Z0 = factor * self.distance * self.unit_vector[2] + self.point1_Z

        # Store point-charge in charge-distribution
        self.charge_distribution_cpc.append_point_charge(X0, Y0, Z0, - factor * self.initial_charge)

        # generate direction vector to construct circular plates
        (V_X1, V_Y1, V_Z1) = self.generate_direction_vector_to_construct_plate()

        iter = range(1, int(self.N) + 1)  # ring_index

        for i in iter:  # Construct every subsequent ring of point_charges
            A1 = 0.5 / float(i)
            N1 = math.pi / (math.asin(A1))  # Number of point_charges in ring i
            N2 = int(N1) + 1
            theta = 0.00
            iter2 = range(1, N2 + 1)
            X = [0 for m in range(1, N2 + 1)]
            Y = [0 for m in range(1, N2 + 1)]
            Z = [0 for m in range(1, N2 + 1)]

            # Second point definition; first point on new ring
            X1 = i * V_X1 * self.R + X0
            Y1 = i * V_Y1 * self.R + Y0
            Z1 = i * V_Z1 * self.R + Z0

            for j in iter2:  # Construct the individual point_charges on ring i
                # Rotate vector so that you end up at the second point in the ring
                (BX, BY, BZ) = self.rotate(X1, Y1, Z1, X0, Y0, Z0, theta)

                # Determine the coordinates of point-charge j on ring i
                X[j - 1], Y[j - 1], Z[j - 1] = \
                    self.determine_point_charge_positions_on_ring(j, X, Y, Z, BX, BY, BZ, X0, Y0, Z0, X1, Y1, Z1)

                # Update the angle
                theta += (2.0 * math.pi) / float(N2)

                # Store point in charge distribution
                self.charge_distribution_cpc.append_point_charge(X[j - 1], Y[j - 1], Z[j - 1],
                                                                    - factor * self.initial_charge)

    def generate_direction_vector_to_construct_plate(self):
        """
        Generate a direction vector along which to set the first point of each subsequent ring of point-charges that
        make up the plate. The first three cases are the numerically difficult cases, the final one is the regular case.
        """

        if math.fabs(self.unit_vector[0]) < 0.0000001:
            V_X1 = 1.000
            V_Y1 = 0.000
            V_Z1 = 0.000
        elif math.fabs(self.unit_vector[1]) < 0.0000001:
            V_X1 = 0.000
            V_Y1 = 1.000
            V_Z1 = 0.000
        elif math.fabs(self.unit_vector[2]) < 0.0000001:
            V_X1 = 0.000
            V_Y1 = 0.000
            V_Z1 = 1.000
        else:
            M = math.sqrt(self.unit_vector[0] ** 2 / (self.unit_vector[1] ** 2 + self.unit_vector[2] ** 2))
            V_X1 = ((1.00) / M) * self.unit_vector[0]
            V_Y1 = (-1.00) * M * self.unit_vector[1]
            V_Z1 = (-1.00) * M * self.unit_vector[2]

        (V_X1, V_Y1, V_Z1) = self.normalize_vector(V_X1, V_Y1, V_Z1)

        return (V_X1, V_Y1, V_Z1)

    def determine_point_charge_positions_on_ring(self, j, X, Y, Z, BX, BY, BZ, X0, Y0, Z0, X1, Y1, Z1):
        """
        Determine the position of point charge j on ring i. The first conditional statement treats the regular case,
        the subsequent conditionals treat numerically problematic cases.
        """

        if math.fabs(self.V_X) > 0.00000001 and math.fabs(self.V_Y) > 0.00000001 \
                and math.fabs(self.V_Z) > 0.00000001:
            X[j - 1] = BX;
            Y[j - 1] = BY;
            Z[j - 1] = -1.0 * (self.V_X / self.V_Z) * (X[j - 1] - X0) - 1.0 * \
                              (self.V_Y / self.V_Z) * (Y[j - 1] - Y0) + Z0
        elif math.fabs(self.V_X) > 0.00000001 and math.fabs(self.V_Y) > 0.00000001 \
                and math.fabs(self.V_Z) < 0.00000001:
            X[j - 1] = BX;
            Y[j - 1] = -1.0 * (self.V_X / self.V_Y) * (X[j - 1] - X0) + Y0;
            Z[j - 1] = BZ
        elif math.fabs(self.V_X) > 0.00000001 and math.fabs(self.V_Y) < 0.00000001 \
                and math.fabs(self.V_Z) > 0.00000001:
            X[j - 1] = BX;
            Y[j - 1] = BY;
            Z[j - 1] = -1.0 * (self.V_X / self.V_Z) * (X[j - 1] - X0) + Z0
        elif math.fabs(self.V_X) < 0.00000001 and math.fabs(self.V_Y) > 0.00000001 \
                and math.fabs(self.V_Z) > 0.00000001:
            X[j - 1] = BX;
            Y[j - 1] = BY;
            Z[j - 1] = -1.0 * (self.V_Y / self.V_Z) * (Y[j - 1] - Y0) + Z0
        elif math.fabs(self.V_X) < 0.00000001 and math.fabs(self.V_Y) < 0.00000001 \
                and math.fabs(self.V_Z) > 0.00000001:
            X[j - 1] = BX;
            Y[j - 1] = BY;
            Z[j - 1] = Z1
        elif math.fabs(self.V_X) < 0.00000001 and math.fabs(self.V_Y) > 0.00000001 \
                and math.fabs(self.V_Z) < 0.00000001:
            X[j - 1] = BX;
            Y[j - 1] = Y1;
            Z[j - 1] = BZ
        elif math.fabs(self.V_X) > 0.00000001 and math.fabs(self.V_Y) < 0.00000001 \
                and math.fabs(self.V_Z) < 0.00000001:
            X[j - 1] = X1;
            Y[j - 1] = BY;
            Z[j - 1] = BZ
        else:
            print ("ERROR INPUT FOR THE COORDINATES OF \"POINT1\" AND \"POINT2\". ")
            print ("\"POIN1\" AND \"POINT2\" ARE THE SAME. ")
            os.exit()

        return X[j - 1], Y[j - 1], Z[j - 1]

    def normalize_vector(self, u, v, w):
        """ Generates a unit vector from an unnormalized (u, v, w) vector """
        l = math.sqrt(u**2 + v**2 + w**2)
        u_normalized = u/l
        v_normalized = v/l
        w_normalized = w/l

        return (u_normalized, v_normalized, w_normalized)

    def rotate(self, X1, Y1, Z1, X0, Y0, Z0, theta):
        """
        rotates the point (X1, Y1, Z1) by theta radians perpendicular to self.unit_vector around point (X0, Y0, Z0)
        """
        #set some intermediate values
        u = self.unit_vector[0]
        v = self.unit_vector[1]
        w = self.unit_vector[2]
        cost = math.cos(theta)
        sint = math.sin(theta)
        onemcost = 1.0 - cost

        # construct rotation matrix m
        m11 = u**2 + (v**2 + w**2) * cost
        m12 = u * v * onemcost - w * sint
        m13 = u * w * onemcost + v * sint
        m14 = (X0 * (v**2 + w**2) - u * (Y0 * v + Z0 * w)) * onemcost + (Y0 * w - Z0 * v) * sint

        m21 = u * v * onemcost + w * sint
        m22 = v**2 + (u**2 + w**2) * cost
        m23 = v * w * onemcost - u * sint
        m24 = (Y0 * (u**2 + w**2) - v * (X0 * u + Z0 * w)) * onemcost + (Z0 * u - X0 * w) * sint

        m31 = u * w * onemcost - v * sint
        m32 = v * w * onemcost + u * sint
        m33 = w**2 + (u**2 + v**2) * cost
        m34 = (Z0 * (u**2 + v**2) - w * (X0 * u + Y0 * v)) * onemcost + (X0 * v - Y0 * u) * sint

        # multiply with the point (X1, Y1, Z1, 1)

        x_new = m11 * X1 + m12 * Y1 + m13 * Z1 + m14
        y_new = m21 * X1 + m22 * Y1 + m23 * Z1 + m24
        z_new = m31 * X1 + m32 * Y1 + m33 * Z1 + m34

        return x_new, y_new, z_new

    def move_output(self, outformat):
        """ move output to right location """
        file = os.getcwd()
        if outformat == "CHARMM":
            path = file + "/CHARMM_FORMAT_CPC"
            self.check_directory(path)
            self.move_charmm()
        elif outformat == "AMBER":
            path = file + "/AMBER_FORMAT_CPC"
            self.check_directory(path)
            self.move_amber()
        elif outformat == "GAUSSIAN":
            path = file + "/GAUSSIAN_FORMAT_CPC"
            self.check_directory(path)
            self.move_gaussian_cpc()
        else:
            print ("FATAL ERROR. WRONG INPUT FOR \"OUTFORMAT\". ")
            print (" THE %.10s FORMAT FOR UNIFORM EEF GENERATION IS UNDER DEVELOPMENT" % (outformat))
            print ("PLEASE SET \"OUTFORMAT\" TO \"CHARMM\" OR \"AMBER\"")
            os.exit()

    def check_directory(self, directory):
        """ creates the directory if it doesn't already exist """
        check = os.path.exists(directory)
        if not check:
            os.makedirs(directory)

    def move_charmm(self):
        """ moves the output to ./CHARMM_FORMAT_CPC """
        info = self.name + ".info"
        pdb = self.name + ".pdb"
        dent_info = "./CHARMM_FORMAT_CPC/" + info
        dent_pdb = "./CHARMM_FORMAT_CPC/" + pdb
        os.rename(info, dent_info)
        os.rename(pdb, dent_pdb)

    def move_amber(self):
        """ moves the output to ./AMBER_FORMAT_CPC """
        info = self.name + ".info"
        pdb = self.name + ".pdb"
        lib = self.name + ".lib"
        frcmod = self.name + ".frcmod"
        leapin = "leap.in"
        dent_info = "./AMBER_FORMAT_CPC/" + info
        dent_pdb = "./AMBER_FORMAT_CPC/" + pdb
        dent_lib = "./AMBER_FORMAT_CPC/" + lib
        dent_frcmod = "./AMBER_FORMAT_CPC/" + frcmod
        dent_leapin = "./AMBER_FORMAT_CPC/" + leapin
        #
        os.rename(info, dent_info)
        os.rename(pdb, dent_pdb)
        os.rename(lib, dent_lib)
        os.rename(frcmod, dent_frcmod)
        os.rename(leapin, dent_leapin)

    def move_gaussian_cpc(self):
        """ moves the output to ./GAUSSIAN_FORMAT_CPC """
        info = self.name + ".info"
        txt = self.name + ".txt"
        dent_info = "./GAUSSIAN_FORMAT_CPC/" + info
        dent_txt = "./GAUSSIAN_FORMAT_CPC/" + txt
        os.rename(info, dent_info)
        os.rename(txt, dent_txt)

    def summary(self, out_format, final_charge, count):
        """
        Writes the summary of the calculation to the .info output-file
        """
        f2 = open(self.name +".info", "w")
        header.header_output_file(f2)
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write("------------------------------------------------------------------ \n")
        f2.write(" \n")
        f2.write("          UNIFORM EXTERNAL ELECTRIC FIELD GENERATION \n")
        f2.write(" \n")
        f2.write("------------------------------------------------------------------- \n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" THE UNIFORM EEF IS GENERATED IN %.10s FORMAT. \n" % (out_format))
        f2.write(" \n")
        if self.unit.upper() == "BOHR":
            f2.write(" THE UNIT OF LENGTH IS BOHR\n")
        elif self.unit.upper() == "ANS":
            f2.write(" THE UNIT OF LENGTH IS ANGSTROM\n")
        f2.write(" \n")
        f2.write(" \n")
        f2.write("------------------------------------------------------------------ \n")
        f2.write("                       CHARGE IN EACH PARTICLE \n")
        f2.write("------------------------------------------------------------------ ")
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" IN ORDER FOR THE FIELD TO BE %10.6f A.U., THE CHARGE SHOULD BE %8.4f e. \n" % (self.field_strength,
                                                                                               final_charge))
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" \n")
        #
        if out_format == "CHARMM":
            f2.write("------------------------------------------------------------------ \n")
            f2.write("                     TOPOLOGY FOR CHARGE \n")
            f2.write("------------------------------------------------------------------ \n")
            f2.write(" \n")
            f2.write(" \n")
            f2.write(" MASS  66  DUM    0.00000 H  ! DUMMY ATOM \n")
            f2.write(" \n")
            f2.write(" \n")
            f2.write(" RESI CHRP   %8.4f \n" % (final_charge))
            f2.write(" GROUP \n")
            f2.write(" ATOM HPC  DUM  %8.4f \n" % (final_charge))
            f2.write(" PATCHING FIRS NONE LAST NONE \n")
            f2.write(" \n")
            f2.write(" \n")
            f2.write(" RESI CHRN         %8.4f \n" % ((-1.00) * final_charge))
            f2.write(" GROUP \n")
            f2.write(" ATOM HNC  DUM   %8.4f \n" % ((-1.00) * final_charge))
            f2.write(" PATCHING FIRST ONE LAST NONE \n")
            f2.write(" \n")
            f2.write(" \n")
            f2.write("------------------------------------------------------------------ \n")
            f2.write("                     PARAMETER FOR CHARGE \n")
            f2.write("------------------------------------------------------------------ \n")
            f2.write(" \n")
            f2.write(" \n")
            f2.write(" DUM    0.000000  -0.000000     0.000000 ! ADD TO THE NONBOND SECTION \n")
            f2.write(" \n")
        elif out_format == "AMBER":
            f2.write("------------------------------------------------------------------ \n")
            f2.write("                TOPOLOGY AND PARAMETER FOR CHARGES \n")
            f2.write("------------------------------------------------------------------ \n")
            f2.write(" \n")
            f2.write(" \n")
            f2.write(" SEE \"%.10s.lib\" IN \"AMBER_FORMAT/\" FOLDER \n" % (self.name))
            f2.write(" SEE \"%.10s.frcmod\" IN \"AMBER_FORMAT/\" FOLDER \n" % (self.name))
            f2.write(" \n")
            f2.write(" \n")
            f2.write("------------------------------------------------------------------ \n")
            f2.write("                         PDB in AMBER FORMAT \n")
            f2.write("------------------------------------------------------------------ \n")
            f2.write(" \n")
            f2.write(" USE THE COMMAND in \"AMBER_FORMAT/\" FOLDER: \n")
            f2.write(" \n")
            f2.write("      tleap -s -f leap.in \n")
            f2.write(" \n")
            f2.write(" THE PDB FILE OF EEF IS \"%.10s_amber.pdb\". \n" % (self.name))
            f2.write(" \n")
            f2.write(" \n")
        elif out_format == "GAUSSIAN":
            pass
        else:
            print (" THE %.10s FORMAT FOR UNIFORM EEF GENERATION IS UNDER DEVELOPMENT" % (out_format))
            os.exit()
        f2.write(" \n")
        f2.write("------------------------------------------------------------------ \n")
        f2.write("                              SUMMARY: \n")
        f2.write("------------------------------------------------------------------ \n")
        f2.write(" \n")
        f2.write("   The plates have been aligned with the defined vector (POINT1 -> POINT2) \n")
        f2.write(" and positioned %8.4f Angstrom from POINT1. The two \n" % (self.distance))
        f2.write(" plates contain %6d point charges, each with an \n" % (count))
        f2.write(" absolute magnitude of %8.4f e per point. These parameters \n" % (final_charge))
        f2.write(" are the settings of the charged plates with %8.4f Angstrom \n" % (self.radius))
        f2.write(" radius \n")
        f2.write(" \n")
        f2.write(" \n")
        if out_format == "AMBER":
            f2.write(" THE PDB FILE OF TWO PARALLEL CIRCULAR PLATES IS  %10s.pdb \n" % (self.name))
        if out_format == "CHARMM":
            f2.write(" THE PDB FILE OF TWO PARALLEL CIRCULAR PLATES IS  %10s.pdb \n" % (self.name))
        if out_format == "GAUSSIAN":
            f2.write(" THE TXT FILE OF TWO PARALLEL CIRCULAR PLATES IS  %10s.txt \n" % (self.name))
        f2.write(" \n")
        f2.write(" \n")
        f2.write(" THE ELECTRIC FIELD HAS BEEN SUCCESSFULLY GENERATED. \n")
        f2.write(" \n")
        header.conclusion_output_file(f2)
        f2.close()
