from titan.myimports import *

class ChargeDistribution():
    """
    A class that represents a charge distribution

    Attributes:
    ----------
    point_charge_list : list
        The list containing the coordinates and charge values associated to the point-charges
        which make up the point-charge distribution
    """
    def __init__(self):
        self.point_charge_list = []

    def construct_point_charge_list(self, all_charge_list, charge_seq, charge_select = "ALL"):
        """ select point-charges from the all_charge_list to be included in the electric field calculation """
        self.reset_point_charge_list()
        number_of_point_charges = len(all_charge_list)
        if charge_select.upper() == "PART":
            charge_seq = self.convert_charge_seq(charge_seq)
        elif charge_select.upper() == "ALL":
            charge_seq = range(number_of_point_charges)

        for i in range(number_of_point_charges):
            if i in charge_seq:
                self.point_charge_list.append(all_charge_list[i])

    def reset_point_charge_list(self):
        """ resets the point_charge_list """
        self.point_charge_list = []

    def write_point_charge_list_to_txt_file(self, name):
        """ writes the point_charge_list to an output-file """
        with open(name + ".txt", "w") as output_file:
            for point_charge in self.point_charge_list:
                output_file.write(" %8.5f     %8.5f     %8.5f     %8.5f \n" %(
                    point_charge[0][0], point_charge[0][1], point_charge[0][2], point_charge[1]))
        output_file.close()

    def calculate_oriented_electric_field(self, point_x, point_y, point_z, vector_x, vector_y, vector_z, unit):
        """
        calculates the electric field exerted along (vector_x, vector_y, vector_z)-direction at
        (point_x, point_y, point_z)
        """
        efx, efy, efz, ef_tot = self.calculate_electric_field(point_x, point_y, point_z, unit)
        oef = self.projvU(efx, efy, efz, vector_x, vector_y, vector_z)

        return oef

    def calculate_electric_field(self, point_x, point_y, point_z, unit):
        """ calculates the electric field exerted by the charge distribution at position (x, y, z) """
        efx_tot = 0.0
        efy_tot = 0.0
        efz_tot = 0.0

        for point_charge in self.point_charge_list:
            if unit.upper() == "ANS":
                efx, efy, efz = self.ef_xyz_ans(point_charge[0][0], point_charge[0][1], point_charge[0][2],
                                                   point_charge[1], point_x, point_y, point_z)
            elif unit.upper() == "BOHR":
                efx, efy, efz = self.ef_xyz_bohr(point_charge[0][0], point_charge[0][1], point_charge[0][2],
                                                   point_charge[1], point_x, point_y, point_z)
            else:
                print("error")
                os.exit()

            efx_tot += efx
            efy_tot += efy
            efz_tot += efz

        ef_tot = math.sqrt(efx_tot**2 + efy_tot**2 + efz_tot**2)

        return efx_tot, efy_tot, efz_tot, ef_tot

    def ef_xyz_ans(self, x, y, z, charge, point_x, point_y, point_z):
        """
        calculates the value of the electric field at (point_x, point_y, point_z) exerted by the charge at (x, y, z)
        """
        k = 1.00  # the coulomb force constant
        distance = math.sqrt((x - point_x) ** 2 + (y - point_y) ** 2 + (z - point_z) ** 2)
        distance = distance / 0.529177249

        dx = (x - point_x) / 0.529177249
        dy = (y - point_y) / 0.529177249
        dz = (z - point_z) / 0.529177249

        cosxt = (-1.0) * dx / distance
        cosyt = (-1.0) * dy / distance
        coszt = (-1.0) * dz / distance

        efx = (k * charge / (distance ** 2)) * cosxt
        efy = (k * charge / (distance ** 2)) * cosyt
        efz = (k * charge / (distance ** 2)) * coszt

        return efx, efy, efz

    def ef_xyz_bohr(self, x, y, z, charge, point_x, point_y, point_z):
        """
        calculates the value of the electric field at (point_x, point_y, point_z)  exerted by the charge at (x, y, z)
        """
        k = 1.00  # the coulomb force constant
        distance = math.sqrt((x - point_x) ** 2 + (y - point_y) ** 2 + (z - point_z) ** 2)

        dx = (x - point_x)
        dy = (y - point_y)
        dz = (z - point_z)

        cosxt = (-1.0) * dx / distance
        cosyt = (-1.0) * dy / distance
        coszt = (-1.0) * dz / distance

        efx = (k * charge / (distance ** 2)) * cosxt
        efy = (k * charge / (distance ** 2)) * cosyt
        efz = (k * charge / (distance ** 2)) * coszt

        return efx, efy, efz

    def projvU(self, efx, efy, efz, vector_x, vector_y, vector_z):
        """ projects efx, efy, efz on the (vector_x, vector_y, vector_z)-direction """
        vU = vector_x * efx + vector_y * efy + vector_z * efz
        mag_v = math.sqrt(vector_x ** 2 + vector_y ** 2 + vector_z ** 2)
        proj = vU / mag_v

        return proj

    def convert_charge_seq(self,charge_seq):
        """
        in case of charge_select = "PART", the read-in charge_seq-string has to be converted into a list,
        i.e. an actual selection of point_charges to be added to the charge distribution
        """
        string = charge_seq
        charge_seq = []
        seq_list = string.split("+")
        seq_list2 = []
        for element in seq_list:
            seq_list2.append(element.split("("))
        for i in range(len(seq_list2)):
            if seq_list2[i][0] == "P":
                charge_seq.append(int(seq_list2[i][1].strip(")")) - 1)
            if seq_list2[i][0] == "R":
                boundaries = seq_list2[i][1].split(",")
                left_boundary = int(boundaries[0])
                right_boundary = int(boundaries[1].strip(")"))
                charge_seq += range(left_boundary - 1, right_boundary)

        return charge_seq

    def ans_to_bohr(self):
        """ converts the spatial unit of the coordinates of the charge distribution from angstrom to bohr """
        for point_charge in self.point_charge_list:
            point_charge[0][0] = point_charge[0][0] / 0.529177249
            point_charge[0][1] = point_charge[0][1] / 0.529177249
            point_charge[0][2] = point_charge[0][2] / 0.529177249

    def bohr_to_ans(self):
        """ converts the spatial unit of the coordinates of the charge distribution from bohr to angstrom """
        for point_charge in self.point_charge_list:
            point_charge[0][0] = point_charge[0][0] * 0.529177249
            point_charge[0][1] = point_charge[0][1] * 0.529177249
            point_charge[0][2] = point_charge[0][2] * 0.529177249