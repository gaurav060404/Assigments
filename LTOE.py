class EmptyTreasureMapError(Exception):
    pass

def decipher_treasure_numbers(numbers):
    try:
        if not numbers:  # Check if the list is empty
            raise EmptyTreasureMapError("ERROR: The treasure map is empty! No numbers to decipher.")

        total_sum = 0
        for num in numbers:
            if num is None:
                num = 0  
            try:
                total_sum += float(num)  
            except ValueError:
                print(f"WARNING: Skipping invalid entry '{num}' (not a number).")

        return total_sum

    except EmptyTreasureMapError as e:
        print(e)
        return None

# The Lost Treasur Of Eldora
treasure_numbers = [10, "20", None, "abc", 50, None, "30.5"]
empty_map = []

print("Total Treasure Value:", decipher_treasure_numbers(treasure_numbers))  
print("Total Treasure Value:", decipher_treasure_numbers(empty_map))  
