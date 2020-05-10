import titan.general_charge_distribution_class as general
import titan.header as header
from titan.myimports import *

class DifferentialDistributionCalculation:
    """
    A class that represents a differential charge distribution calculation

    Attributes:
    ----------
    distribution1 : ChargeDistribution
        The charge distribution object associated to distribution 1
    distribution2 : ChargeDistribution
        The charge distribution object associated to distribution 2
    differential_distribution : ChargeDistribution
        The charge distribution object associated to the differential distribution

    Methods:
    -------
    execute : executes the workflow associated to the quantification calculation
    """
    def __init__(self, distribution1, distribution2):
        self.distribution1 = distribution1
        self.distribution2 = distribution2

        self.differential_distribution = general.ChargeDistribution()

    def construct_differential_distribution(self):
        """ constructs the differential distribution from distribution1 and distribution2 """
        self.reset_differential_distribution()
        self.differential_distribution.point_charge_list = self.distribution1.point_charge_list
        self.append_differential()

    def reset_differential_distribution(self):
        """ resets the point_charge_list in the differential distribution object """
        self.differential_distribution.point_charge_list = []

    def append_differential(self):
        """
        checks whether points of distribution 1 and 2 overlap; if so: subtract charges; if not: append point-charge
        form distribution 2
        """

        for i in range(len(self.distribution2.point_charge_list)):
            counter = 0
            for j in range(len(self.distribution1.point_charge_list)):
                counter += 1
                distance = self.determine_distance(i,j)
                if distance < 0.001:
                    break
            if counter > 0 and counter < len(self.distribution1.point_charge_list) + 1:
                self.differential_distribution.point_charge_list[counter - 1][1] += \
                    -  self.distribution2.point_charge_list[i][1]
            else:
                self.differential_distribution.point_charge_list.append(self.distribution2.point_charge_list[i])

    def determine_distance(self, i, j):
        distance = math.sqrt(
            (self.distribution2.point_charge_list[i][0][0] -
             self.differential_distribution.point_charge_list[j][0][0])**2 + \
             (self.distribution2.point_charge_list[i][0][1] -
              self.differential_distribution.point_charge_list[j][0][1]) ** 2 + \
             (self.distribution2.point_charge_list[i][0][2] -
              self.differential_distribution.point_charge_list[j][0][2]) ** 2)

        return distance

    def import_point_charges_from_txt_file(self, charge_distribution, name):
        """
        reads coordinates and charges for all the point-charges from a .txt file and stores them in an auxiliary list
        """
        content = self.read_coordinates_and_charges_from_txt(name)
        number_of_point_charges = len(content)
        for i in range(number_of_point_charges):
             charge_distribution.point_charge_list.append(
                [[content[i][0], content[i][1], content[i][2]], content[i][3]])

    def read_coordinates_and_charges_from_txt(self, name):
        """ reads coordinates and charges from .txt file to quantify local electric field """
        content = []
        with open(name + ".txt", "r", encoding="utf-8") as input_file:
            for line in input_file:
                content.append(list(map(float, line.split())))
                if not line.split():
                    continue
        input_file.close()

        return content

# ----------------------------------------------------
# Main
if __name__ == '__main__':

    # Get Input
    if len(sys.argv[1:]) == 3:
        txt_name1 = sys.argv[1]
        txt_name2 = sys.argv[2]
        output_name = sys.argv[3]

        #execute the stand-alone calculation
        header.header_command_line()
        try:
            distribution1 = general.ChargeDistribution()
            distribution2 = general.ChargeDistribution()
            differential = DifferentialDistributionCalculation(distribution1, distribution2)
            differential.import_point_charges_from_txt_file(distribution1, txt_name1)
            differential.import_point_charges_from_txt_file(distribution2, txt_name2)
        except:
            print("AN ERROR OCCURRED WHILE CONSTRUCTING THE TWO INPUT DISTRIBUTIONS")
            print("MAKE SURE THE RESPECTIVE FILE NAMES WERE CORRECTLY PROVIDED IN THE INPUT LINE")
            print("(WITHOUT THE .txt EXTENSION)")
            print(" ")
            header.error_command_line()
            sys.exit()

        try:
            differential.construct_differential_distribution()
            differential.differential_distribution.write_point_charge_list_to_txt_file(output_name)
        except:
            print("AN ERROR OCCURRED WHILE CONSTRUCTING THE DIFFERENTIAL DISTRIBUTION")
            print(" ")
            header.error_command_line()
            sys.exit()
        print(" THE DIFFERENTIAL CHARGE DISTRIBUTION HAS BEEN CONSTRUCTED SUCCESSFULLY")
        print(" ")
        header.conclusion_command_line()

    else:
        print('ERROR: Wrong input')
        print('Usage:')
        print('python differential_charge_distribution.py name_distribution1 name_distribution2 name_output_file (no .txt extension')