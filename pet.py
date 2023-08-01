# Pet class that contains pet details
class Pet:
    # Initialize pet class
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    
    # Get the pet name
    def get_name(self):
        return self.__name
    
    # Get the animal type
    def get_animal_type(self):
        return self.__animal_type
    
    # Get the pet age
    def get_age(self):
        return self.__age
    
    # Set the pet name
    def set_name(self, name):
        self.__name = name
    
    # Set the pet animal type
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
       
    # Set the pet age 
    def set_age(self, age):
        self.__age = age