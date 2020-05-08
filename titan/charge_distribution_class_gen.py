import titan.output as output
from titan.general_charge_distribution_class import ChargeDistribution
from titan.myimports import *

class ChargeDistributionGenerate(ChargeDistribution):
    """
     An abstract class that represents a charge distribution constructed during a generation calculation.

     Attributes:
     ----------
     point_charge_list : list
         The list containing the coordinates and charge values associated to the point-charges
         which make up the point-charge distribution
     """

    def __init__(self):
        ChargeDistribution.__init__(self)

    def update_charges(self,new_charge):
        for point_charge in self.point_charge_list:
            if point_charge[1] > 0:
                point_charge[1] = new_charge
            if point_charge[1] < 0:
                point_charge[1] = - new_charge

    def gaussian_write_point_charges(self, output_file):
        """
        Write the point to output_file in the Gaussian format
        """
        for i in range(int(len(self.point_charge_list))):
            output_file.write("%10.6f     %10.6f      %10.6f       %10.6f \n" % (
            self.point_charge_list[i][0][0], self.point_charge_list[i][0][1],
            self.point_charge_list[i][0][2], self.point_charge_list[i][1]))

class ChargeDistributionCpc(ChargeDistributionGenerate):
    """
    A class that represents a charge distribution constructed during a circular plate generation calculation.

    Attributes:
    ----------
    point_charge_list : list
        The list containing the coordinates and charge values associated to the point-charges
        which make up the point-charge distribution
    """
    def __init__(self):
        ChargeDistributionGenerate.__init__(self)

    def append_point_charge(self, x, y, z, charge):
        """ adds point-charges to the point_charge_list """
        point_charge = []
        point_charge.append([float(x), float(y), float(z)])
        point_charge.append(float(charge))
        self.point_charge_list.append(point_charge)

    def write_point_charge_list(self, output_format, name):
        if output_format.upper() == "GAUSSIAN":
            output_file = open(name + ".txt", "w")
            self.gaussian_write_point_charges(output_file)
        elif output_format.upper() == "AMBER":
            output_file = open(name + ".pdb", "w")
            self.amber_write_point_charges(output_file, name)
        elif output_format.upper() == "CHARMM":
            output_file = open(name + ".pdb", "w")
            self.charmm_write_point_charges(output_file)

        output_file.close()

    def amber_write_point_charges(self, output_file, name):
        """
        Write the point to output_file in the amber format and construct auxiliary files needed to execute
        amber calculations
        """
        for i in range(len(self.point_charge_list)):
            if self.point_charge_list[i][1] > 0.0:
                output_file.write("ATOM %6d  HPC CRP  %4d    %8.3f%8.3f%8.3f  1.00  0.00 \n" % (i + 1, i + 1,
                    self.point_charge_list[i][0][0], self.point_charge_list[i][0][1], self.point_charge_list[i][0][2]))
            elif self.point_charge_list[i][1] < 0.0:
                output_file.write("ATOM %6d  HNC CRN  %4d    %8.3f%8.3f%8.3f  1.00  0.00 \n" % (i + 1, i + 1,
                    self.point_charge_list[i][0][0], self.point_charge_list[i][0][1], self.point_charge_list[i][0][2]))
        output_file.write("END")

        output.amberlib_cpc(name, self.point_charge_list[0][1])
        output.amberfrcmod_cpc(name)
        output.amberleapin_cpc(name)

    def charmm_write_point_charges(self, output_file):
        """
        Write the point to output_file in the charmm format
        """
        for i in range(len(self.point_charge_list)):
            if self.point_charge_list[i][1] > 0.0:
                output_file.write("ATOM %6d  HPC CHRP %4d    %8.3f%8.3f%8.3f  1.00  0.00      SCPC \n" % (i + 1, i + 1,
                    self.point_charge_list[i][0][0], self.point_charge_list[i][0][1], self.point_charge_list[i][0][2]))
            elif self.point_charge_list[i][1] < 0.0:
                output_file.write("ATOM %6d  HNC CHRN  %4d    %8.3f%8.3f%8.3f  1.00  0.00 \n" % (i + 1, i + 1,
                    self.point_charge_list[i][0][0], self.point_charge_list[i][0][1], self.point_charge_list[i][0][2]))
        output_file.write("END")

class ChargeDistributionSl(ChargeDistributionGenerate):
    """
    A class that represents a charge distribution constructed during a spiral line generation calculation.

    Attributes:
    ----------
    point_charge_list : list
        The list containing the coordinates and charge values associated to the point-charges
        which make up the point-charge distribution
    """
    def __init__(self):
        ChargeDistributionGenerate.__init__(self)

    def append_point_charge(self, x, y, z, charge, type_a, type_r):
        """ adds point-charges to the point_charge_list """
        point_charge = []
        point_charge.append([float(x), float(y), float(z)])
        point_charge.append(float(charge))
        point_charge.append(type_a)
        point_charge.append(type_r)
        self.point_charge_list.append(point_charge)

    def write_point_charge_list(self, name, fragment_size):
        gauss = open(name + ".txt", "w")
        self.gaussian_write_point_charges(gauss)
        gauss.close()

        pdb = open(name + ".pdb", "w")
        for i in range(len(self.point_charge_list)):
            pdb.write("ATOM %6d%5s %.4s %4d    %8.3f%8.3f%8.3f  1.00  0.00      SLDC \n" % (
                i + 1, self.point_charge_list[i][2], self.point_charge_list[i][3], int(float(i) / fragment_size) + 1, self.point_charge_list[i][0][0],
                self.point_charge_list[i][0][1], self.point_charge_list[i][0][2]))
        pdb.write("END")
        pdb.close()
