from pet_owner_module import PetOwner
from pet_owner_module import Pet

def main():
    

    selection = 'a'
    pet_owner_list = []
    
    while selection != 'q':
        print("\n\tType: ")
        print("\t\tc - to create a pet owner")
        print("\t\tv - to view all pet owners")
        print("\t\tq - to quit\n")

        selection = input("\tEnter selection: ")[0]
        if selection == 'c':
            owner = create_pet_owner()
            pet_owner_list.append(owner)
            
        elif selection == 'v':
            view_pet_owners(pet_owner_list)

    print("\tPROGRAM ENDED\n")

    
## Create a pet owner with zero or more pets
# @return a PetOwner object
#  
def create_pet_owner() :

    name = input("\n\tEnter the pet owner's name: ")
            
    more_pets = True
    pet_list = []
    while more_pets == True:
        pet = input("\n\tEnter {}'s pet's name or just <Enter> to finish: ".format(name))
        if len(pet.strip()) != 0:
            petObj = Pet(pet)
            pet_list.append(petObj)
        else:
            more_pets = False
            owner = PetOwner(name, pet_list)

    return owner

  
## View the list of pet owners
# @param owner_list list containing PetOwner objects
#   
def view_pet_owners(owner_list):  
    if len(owner_list) == 0:
        print("\n\tThere are no pet owners")
    else:
        for owner in owner_list:
            print("\t", owner.name, " has: ")
            if len(owner.pet_list) == 0:
                print("\t\t no pets")
            else:
                for pet in owner.pet_list:
                    print("\t\t", pet.name)
  
  
    
if __name__ == "__main__":
    main()

