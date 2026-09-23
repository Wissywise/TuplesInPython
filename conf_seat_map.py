"""
Build a small tool that uses tuples to store seats, search a seat, and extend the seat map. Use loops, if/else, and a
tiny function. Questions for this assignment Create a tuple of seats and print the total. (Each seat is (row, number).)

Count how many seats are in row "A" using a loop and if/else (do not convert to list).
Write a function find_seat(target, seat_map) that returns the index of a seat if found, otherwise "Not Found". Use a
loop and break. Add extra seats by concatenating another tuple, then print the last two using slicing.
Make a small nested tuple of rows and their labels, then print all seats in row "B" using a loop

In Python, tuples are "immutable," meaning once they are created, they cannot be changed. This makes them perfect for a
seat map where you don't want the layout to be accidentally modified. Here is your seat management tool, built using
tuples and the specific logic you requested.

#Creating the Seat Map
#We use a tuple of tuples, where each individual seat is represented by a coordinate pair: (row, number).
"""

# Initial tuple of seats (Row, Seat Number)
seat_map = (("A", 1), ("A", 2), ("B", 1), ("B", 2), ("C", 1))

print(f"Total seats initially: {len(seat_map)}")

# Count seats specifically in Row A
count_a = 0
for seat in seat_map:
    if seat[0] == "A":
        count_a += 1

print(f"Seats in Row A: {count_a}")


# Finding a Seat: This function uses a loop to check each "coordinate" in our map. We use break to stop as soon as we
# find the target to save processing #power.

def find_seat(target, seat_map):
    """Returns the index of the seat if found, otherwise 'Not Found'."""
    for index, seat in enumerate(seat_map):
        if seat == target:
            result = index
            break  # Exit the loop immediately once found
    else:
        # The else block of a loop runs only if 'break' was NOT hit
        return "Not Found"

    return result


# Function calls
print(f"Index of ('B', 1): {find_seat(('B', 1), seat_map)}")
print(f"Index of ('Z', 9): {find_seat(('Z', 9), seat_map)}")

# Extending the Seat Map (Concatenation)
# Since we can't .append() to a tuple, we create a new one by adding (concatenating) two tuples together.


# Create extra seats and concatenate
extra_seats = (("D", 1), ("D", 2))
full_map = seat_map + extra_seats

# Slicing the last two seats
print(f"Last two seats in updated map: {full_map[-2:]}")

# Nested Tuples and Row Filtering
# In this section, we create a nested structure to represent the venue rows and then iterate through them to find
# specific labels.


# Nested tuple: (Row Label, (Seat Numbers))
venue_layout = (
    ("A", (1, 2, 3)),
    ("B", (1, 2)),
    ("C", (1, 2, 3, 4))
)

print("\n--- Printing all seats in Row B ---")
for row_label, seats in venue_layout:
    if row_label == "B":
        for seat_num in seats:
            print(f"Seat: {row_label}{seat_num}")
"""
Key Concepts Applied
Immutability: We used + to "extend" our map. This actually creates a brand-new tuple in memory rather than modifying the old one.

Tuple Unpacking: In the final loop, for row_label, seats in venue_layout automatically "unpacks" the two items in each inner 
tuple into variables. Loop-Else logic: In the search function, using a break allows us to handle the "Not Found" case cleanly.
"""

# Converting Tuples to a Dictionary. We will use the seat coordinate (the tuple) as the Key and the availability or attendee
# name as the #Value.

# Initial tuple map
seat_tuple = (("A", 1), ("A", 2), ("B", 1), ("B", 2))

# Convert to Dictionary using a comprehension
# Key: (Row, Number), Value: Status
seat_dict = {seat: "Available" for seat in seat_tuple}

print(f"Dictionary Map: {seat_dict}")


# High-Speed Lookups. In the tuple version, we had to use a for loop and break. In the dictionary version, we use the .get()
# method. This is #significantly faster for large venues.

def check_seat_fast(target, map_dict):
    """Instantly returns the status of a seat without a loop."""
    # .get() returns "Not Found" if the key doesn't exist, preventing errors
    return map_dict.get(target, "Not Found")


# Instant lookup (no looping required!)
print(f"Status of ('B', 1): {check_seat_fast(('B', 1), seat_dict)}")
print(f"Status of ('Z', 9): {check_seat_fast(('Z', 9), seat_dict)}")

# Updating and Extending the Map. While tuples require concatenation (creating a whole new object), dictionaries are mutable.
# We can add or update seats instantly.

# Adding a single new seat
seat_dict[("C", 1)] = "Available"

# Updating a seat status (Booking a seat)
seat_dict[("A", 1)] = "Occupied by Lucía"

# Extending with multiple seats using .update()
extra_seats = {("D", 1): "Available", ("D", 2): "Available"}
seat_dict.update(extra_seats)

print(f"Total seats in dictionary: {len(seat_dict)}")

"""
Comparison: Tuple vs. Dictionary
Feature		Tuple Map				Dictionary Map
Search Logic	Must loop through every item.		Direct access via Key.
Speed		$O(n)$ (Slower as list grows).		$O(1)$ (Instant, regardless of size).
Flexibility	Immutable (Must recreate to change).	Mutable (Update in place).
Use Case	Fixed layouts/Coordinates.		Active booking systems/Databases.

Why use a Tuple as a Key?
You might notice we used the tuple ("A", 1) as the key. This is a common Python trick! Dictionary keys must be immutable. 
Since tuples cannot be changed, they make perfect "coordinates" or composite keys for a dictionary.Would you like me to 
show you how to nest these dictionaries (e.g., {'Row A': {1: 'Available', 2: 'Occupied'}}) for even more organized data?
"""