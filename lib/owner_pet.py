class Pet:
    # Class-level variable for allowed pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    # Class-level variable to store all pet instances
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate that pet_type is one of the allowed PET_TYPES
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")

        # Instance attributes
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Add the pet to the all pets list
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return a list of pets that have this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Check that the pet is an instance of the Pet class
        if not isinstance(pet, Pet):
            raise Exception("Only Pet instances can be added as pets.")
        
        # Assign this owner to the pet
        pet.owner = self

    def get_sorted_pets(self):
        # Sort the owner's pets by their names
        return sorted(self.pets(), key=lambda pet: pet.name)
