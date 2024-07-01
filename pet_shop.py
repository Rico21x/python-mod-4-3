class PetNotAvailableError(Exception):
    pass

def sell_pet(inventory, pet_name):
    if pet_name not in inventory or inventory[pet_name] == 0:
        raise PetNotAvailableError(f"{pet_name} is not available in the inventory.")
    inventory[pet_name] -= 1
    return inventory
