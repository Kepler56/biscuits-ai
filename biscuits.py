class Biscuit:
    """
        The Biscuit class represents the types of biscuits that will be produced from the single roll of dough.
        ----------------
        Attributes:
            size: the size of the biscuit
            value: the price of the biscuit
            defects: a dictionary containing the threshold of the maximum number of defects per class type
            type: the type of biscuit {0,1,2,3}
        ----------------
        Methods:
            get_max_defects: returns the maximum number of defects allowed for a particular class
            check_defect_threshold: checks if the number of defects for each class is within the threshold
            __str__: dunder method that returns a string representation of the biscuit
    """
    def __init__(self, id, size, value, max_defects):
        self.id = id
        self.size = size
        self.value = value
        self.max_defects = max_defects

    def get_max_defects(self, defect_class):
        return self.max_defects.get(defect_class, 0)

    def check_defect_threshold(self, defect_counts):
        for defect_class, count in defect_counts.items():
            max_count = self.get_max_defects(defect_class)
            if count > max_count:
                return True
        return False
    
    def __str__(self):
        return "The biscuit of type {} is of size {} with a value of {} and has the following threshold for the different defects \n{}.".format(self.id, self.size, self.value,self.max_defects)