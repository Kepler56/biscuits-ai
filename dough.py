import csv

class Dough:
    """
        This Dough class represents the single roll of dough that will be used to produce the biscuits. 
        ----------------
        Attributes:
            length: the length of the dough
            defects: a dictionary of defects with the position and their class type
        ----------------
        Methods:
            load_defects: loads the defects from the csv file provided
            __str__: dunder method that returns a string representation of the dough
    """
    def __init__(self, length):
        self.length = length
        self.defects = {}

    def load_defects(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                # We decided to round the defect position to the nearest integer
                position = round(float(row[0]))
                defect_type = row[1]
                self.defects[position] = defect_type

    def __str__(self):
        return "The dough is of length {} and has the following defects \n{}.".format(self.length, self.defects)