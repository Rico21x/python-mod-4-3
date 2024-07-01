import pytest
from pet_shop import sell_pet, PetNotAvailableError

def test_sell_pet():
    # Initial inventory
    inventory = {
        'dog': 5,
        'cat': 3,
        'fish': 10
    }
    
    # Test case 1: Successful sale
    updated_inventory = sell_pet(inventory.copy(), 'dog')
    assert updated_inventory['dog'] == 4, f"Expected 4 but got {updated_inventory['dog']}"
    
    # Test case 2: Pet not in inventory
    with pytest.raises(PetNotAvailableError, match="rabbit is not available in the inventory."):
        sell_pet(inventory.copy(), 'rabbit')
    
    # Test case 3: Pet is out of stock
    out_of_stock_inventory = {'cat': 0}
    with pytest.raises(PetNotAvailableError, match="cat is not available in the inventory."):
        sell_pet(out_of_stock_inventory.copy(), 'cat')

if __name__ == "__main__":
    pytest.main()
