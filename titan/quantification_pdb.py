from titan.quantification import Quantification
from titan.myimports import *

class QuantificationPdb(Quantification):
    """
    A class that represents a quantification calculation starting from a .pdb file

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
    n_terminal : int
        The residue number of the protein that constitutes the n-terminal; use command: "  grep "HT1" PDB_FILE    "
        to confirm the residue number
    c_terminal : int
        The residue number of the protein that constitutes the c-terminal; use command: "  grep "OT1" PDB_FILE    "
        to confirm the residue number
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
    def __init__(self, name, point_x, point_y, point_z, v1_x, v1_y, v1_z, v2_x, v2_y, v2_z,
                   n_terminal, c_terminal, charge_seq="/", charge_select="ALL", unit="ANS"):
        Quantification.__init__(self, name, point_x, point_y, point_z, v1_x, v1_y, v1_z, v2_x, v2_y, v2_z, charge_seq,
                   charge_select, unit)
        self.n_terminal = n_terminal
        self.c_terminal = c_terminal

    def import_content_from_pdb_input(self):
        """ read and extract the content of the .pdb file """
        pdb_content = []
        with open(self.name + ".pdb", "r", encoding="utf-8") as file_pdb:
            for line in file_pdb:
                pdb_content.append(list(line.split('\n')))
                if not line.split():
                    continue
        file_pdb.close()

        for line_list in pdb_content:
            while '' in line_list:
                line_list.remove('')

        return pdb_content

class QuantificationPdbAmber(QuantificationPdb):
    """
    A class that represents a quantification calculation starting from a .pdb file (amber force field)

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
    n_terminal
        The residue number of the protein that constitutes the n-terminal; use command: "  grep "HT1" PDB_FILE    "
        to confirm the residue number
    c_terminal : int
        The residue number of the protein that constitutes the c-terminal; use command: "  grep "OT1" PDB_FILE    "
        to confirm the residue number
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
    def __init__(self, name, point_x, point_y, point_z, v1_x, v1_y, v1_z, v2_x, v2_y, v2_z, n_terminal, c_terminal,
                 charge_seq="/", charge_select="ALL", unit="ANS"):
        QuantificationPdb.__init__(self, name, point_x, point_y, point_z, v1_x, v1_y, v1_z, v2_x, v2_y, v2_z,
                                   n_terminal, c_terminal, charge_seq, charge_select, unit)

    def execute(self):
        """
        executes the workflow associated to the quantification calculation
        """
        self.import_point_charges_from_pdb_file()
        efx, efy, efz, ef_tot, oef = self.quantify_selected_charge_distribution()
        self.charge_distribution_to_quantify.write_point_charge_list_to_txt_file(self.name)
        self.write_output_quantification_calculation(efx, efy, efz, ef_tot, oef)

    def import_point_charges_from_pdb_file(self):
        """ read and extract the content of the .pdb file """
        pdb_content = self.import_content_from_pdb_input()

        library_path = os.path.dirname(os.path.realpath(__file__))
        with open(str(library_path) + "/amber_library.json", "r", encoding="utf-8") as json_file:
            amber_library = json.load(json_file)

        counter = 0
        for line_list in pdb_content:
            if "ATOM" in line_list[0]:
                pdb_content[counter] = pdb_content[counter][0].split(' ')
                while '' in pdb_content[counter]:
                    pdb_content[counter].remove('')
                coordinates = [float(pdb_content[counter][5]), float(pdb_content[counter][6]),
                               float(pdb_content[counter][7])]
                if int(pdb_content[counter][4]) == self.n_terminal and "ENZY" in pdb_content[counter][10]:
                    charge = amber_library["N" + pdb_content[counter][3] + " " + pdb_content[counter][2]]
                elif int(pdb_content[counter][4]) == self.c_terminal and "ENZY" in pdb_content[counter][10]:
                    charge = amber_library["C" + pdb_content[counter][3] + " " + pdb_content[counter][2]]
                else:
                    charge = amber_library[pdb_content[counter][3] + " " + pdb_content[counter][2]]
                self.full_charge_distribution.point_charge_list.append([coordinates, float(charge)])
            counter += 1

class QuantificationPdbCharmm(QuantificationPdb):
    """
    A class that represents a quantification calculation starting from a .pdb file (amber force field)

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
    n_terminal : int
        The residue number of the protein that constitutes the n-terminal; use command: "  grep "HT1" PDB_FILE    "
        to confirm the residue number
    c_terminal : int
        The residue number of the protein that constitutes the c-terminal; use command: "  grep "OT1" PDB_FILE    "
        to confirm the residue number
    charge_seq : string
        The charge sequence, in which the range from charge/atom x to y is denoted by R(x,y) and individual
        charges/atoms are denoted by P, i.e. P(x); "+" signs are used to catenate ranges and points (default = "/")
    charge_select: string
        Keyword indicating whether all charges/atoms or only part are considered during the quantification
        (2 options: "ALL" or "PART"; default = "ALL")
    unit : string
        The unit used in the calculation (angstrom = "ANS", bohr = "BOHR"; default = "ANS")
    aspp : list
        The list of protonated aspartate residues (default = None); use command: "  grep "HD2 ASP" PDB_FILE    "
        to confirm the residue numbers
    glup : list
        The list of protonated glutamate residues (default = None); use command: "  grep "HE2 GLU" PDB_FILE    "
        to confirm the residue numbers
    disu : list
        The list of cysteine residues linked through a disulfide bond (default = None); if e.g. CYS 300 is bonded with
        CYS 340 this way, then set this keyword to [300, 340]. Use commands: "  grep "SG  CYS" PDB_FILE    " and
        "  grep "HG1 CYS" PDB_FILE    " to confirm the residue numbers

    Methods:
    -------
    execute : executes the workflow associated to the quantification calculation
    """
    def __init__(self, name, point_x, point_y, point_z, v1_x, v1_y, v1_z, v2_x, v2_y, v2_z, n_terminal, c_terminal,
                 charge_seq="/", charge_select="ALL", unit="ANS", aspp=None, glup=None, disu=None):
        QuantificationPdb.__init__(self, name, point_x, point_y, point_z, v1_x, v1_y, v1_z, v2_x, v2_y, v2_z,
                                   n_terminal, c_terminal, charge_seq, charge_select, unit)
        if aspp is None:
            aspp = []
        if glup is None:
            glup = []
        if disu is None:
            disu = []

        self.aspp = aspp
        self.glup = glup
        self.disu = disu

    def execute(self):
        """
        executes the workflow associated to the quantification calculation
        """
        self.import_point_charges_from_pdb_file()
        efx, efy, efz, ef_tot, oef = self.quantify_selected_charge_distribution()
        self.charge_distribution_to_quantify.write_point_charge_list_to_txt_file(self.name)
        self.write_output_quantification_calculation(efx, efy, efz, ef_tot, oef)

    def import_point_charges_from_pdb_file(self):
        """ read and extract the content of the .pdb file """
        pdb_content = self.import_content_from_pdb_input()

        library_path = os.path.dirname(os.path.realpath(__file__))
        with open(str(library_path) + "/charmm_library.json", "r", encoding="utf-8") as json_file:
            charmm_library = json.load(json_file)

        counter = 0
        for line_list in pdb_content:
            if "ATOM" in line_list[0]:
                pdb_content[counter] = pdb_content[counter][0].split(' ')
                while '' in pdb_content[counter]:
                    pdb_content[counter].remove('')
                coordinates = (float(pdb_content[counter][5]), float(pdb_content[counter][6]),
                               float(pdb_content[counter][7]))
                if int(pdb_content[counter][4]) == self.n_terminal and pdb_content[counter][10] == "ENZY":
                    charge = charmm_library[pdb_content[counter][3] + "N " + pdb_content[counter][2]]
                elif int(pdb_content[counter][4]) == self.c_terminal and pdb_content[counter][10] == "ENZY":
                    charge = charmm_library[pdb_content[counter][3] + "C " + pdb_content[counter][2]]
                elif int(pdb_content[counter][4]) in self.aspp and pdb_content[counter][10] == "ENZY":
                    charge = charmm_library["ASPP " + pdb_content[counter][2]]
                elif int(pdb_content[counter][4]) in self.glup and pdb_content[counter][10] == "ENZY":
                    charge = charmm_library["GLUP " + pdb_content[counter][2]]
                elif int(pdb_content[counter][4]) in self.disu and pdb_content[counter][10] == "ENZY":
                    charge = charmm_library["DISU " + pdb_content[counter][2]]
                else:
                    charge = charmm_library[pdb_content[counter][3] + " " + pdb_content[counter][2]]
                self.full_charge_distribution.point_charge_list.append([coordinates, float(charge)])
            counter += 1