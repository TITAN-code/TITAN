import json
from titan.myimports import *

class Library():
    """
    A class that represents an abstract charge library

    Attributes:
    ----------
    charge_dictionary : dictionary
        The dictionary containing the names of the charged particle as keys and the corresponding charges as values
    """
    def __init__(self):
        self.charge_dictionary = {}

    def append_charge_dictionary(self, name):
        """ adds (key,value) couples to the library """
        raise NotImplementedError("Subclass must implement abstract method")

    def store_charge_dictionary(self, name):
        """ stores the charge dictionary in a .json file """
        with open(name + ".json", "w") as json_file:
            json.dump(self.charge_dictionary, json_file)

    def load_charge_dictionary(self, name):
        """ loads the charge dictionary from a .json file """
        with open(name + ".json", "r") as json_file:
            self.charge_dictionary = json.load(json_file)

    def reset_charge_dictionary(self):
        """ reset the charge dictionary by replacing with an empty one """
        self.charge_dictionary = {}

class AmberLibrary(Library):
    """
    A class that represents an amber library
    """
    def __init__(self):
        Library.__init__(self)

    def append_charge_dictionary(self, name):
        """ adds (key,value) couples to the library from an amber-library file """
        content = []
        with open(name, "r") as lib_file:
            for line in lib_file:
                content.append(line.split(" "))
                if not line.split():
                    continue
        lib_file.close()

        for line in content:
            if len(line) == 1:
                continue
            elif "!" in line[0]:
                resi_t = line[0].split(".")[1]
            elif "\"" in line[0]:
                atom_name = line[0].strip("\"")
                charge = line[-1].strip("\n")
                self.charge_dictionary[resi_t + " " + atom_name] = float(charge)
            elif "\"" in line[1]:
                atom_name = line[1].strip("\"")
                charge = line[-1].strip("\n")
                self.charge_dictionary[resi_t + " " + atom_name] = float(charge)

class CharmmLibrary(Library):
    """
    A class that represents a charmm library
    """
    def __init__(self):
        Library.__init__(self)

    def append_charge_dictionary(self, name):
        """ adds (key,value) couples to the library from a charmm-library file """
        content = []
        with open(name, "r") as lib_file:
            for line in lib_file:
                content.append(line.strip(" \n").split(" "))
                if not line.split():
                    continue
        lib_file.close()

        for line in content:
            while '' in line:
                line.remove('')
            if line[0] == "RESI" :
                resi_t = line[1].strip("\t")
            elif line[0] == "ATOM":
                atom_name = line[1].strip("\t")
                charge = line[3].strip("\n")
                self.charge_dictionary[resi_t + " " + atom_name] = float(charge)

#+++++++++++++++++++++++++++
if __name__ == '__main__':
    if len(sys.argv[1:]) == 1:
        library_type = sys.argv[1]
        if library_type == "AMBER":
            new_library = AmberLibrary()
        elif library_type == "CHARMM":
            new_library = CharmmLibrary()
        else:
            print("ERROR: LIBRARY_TYPE NOT RECOGNIZED!")
            print("LIBRARY_TYPE HAS TO BE EITHER \"AMBER\" OR \"CHARMM\"")
            sys.exit()
        while True:
            name = input("FROM WHICH FILE SHOULD THE (KEY,VALUE) COUPLES BE APPENDED TO THE NEW LIBRARY?")
            try:
                new_library.append_charge_dictionary(str(name))
            except:
                print("FILE DOES NOT EXIST!")
                answer = input("DO YOU WANT TO CONTINUE (Y OR N)?")
                if answer == "Y":
                    continue
                else:
                    new_library.store_charge_dictionary("new_library")
                    break
            print("THE (KEY,VALUE) COUPLES HAVE SUCCESSFULLY BEEN APPENDED.")
            answer = input("DO YOU WANT TO CONTINUE (Y OR N)?")
            if answer == "Y":
                continue
            else:
                new_library.store_charge_dictionary("new_library")
                break
    else:
        print('ERROR: WRONG INPUT')
        print('USAGE:')
        print('python titan.py library_type (\"AMBER\" or \"CHARMM\"')


