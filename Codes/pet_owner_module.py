###  This module defines a class that models a pet owner.
#

## A PetOwner has a name and a list of pets. 
#
class PetOwner:
    
    
    ## Constructs a PetOwner with a name and a list of pets.
    #  @param owner_name the name of the pet owner.
    #  @param pet_list the list of Pet objects
    #
    def __init__(self, the_name, the_pet_list):
            self.name = the_name
            self.pet_list = the_pet_list
            
    ##    
    # @return string representation of object.
    #
    def __str__(self):
        all_the_pets = ""
        for pet in self._pets:
            all_the_pets + pet._name + ", "
        return "Name: " + self.name + ", pets: " + all_the_pets


    ## name property allows get/set access to PetOwner's name value.
    #  name must not be whitespace else a ValueError is raised.
    #
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, theName):
        if len(theName.strip()) != 0:
            self._name = theName
        else:
            raise ValueError("Invalid name: " + name)
   
    ## pet_list property allows get/set access to Employee's list of pets.
    #  pet_list is a list of Pet objects
    #
    @property
    def pet_list(self):
        return self._pet_list
    ## 
    # Check that the objects in the list are Pet objects.
    # It is valid for the list to be empty.
    @pet_list.setter
    def pet_list(self, the_pet_list):
      
        for pet in the_pet_list:
            if isinstance(pet, Pet) == False :
                raise TypeError("List of pets contains an object which doesn't have type \"Pet\".")
        self._pet_list = the_pet_list
    
            
            
            
            
            
class Pet:
    def __init__(self, name):
        self._name = name
        
        
    ## name property allows get/set access to Pet's name value.
    #  name must not be whitespace else a ValueError is raised.
    #
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, theName):
        if len(theName.strip()) != 0:
            self._name = theName
        else:
            raise ValueError("Invalid pet name: " + name)
        