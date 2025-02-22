import math

def euclidean_distance(x, y):
    # Calculate the distance using the formula sqrt(x^2 + y^2)
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

# Input: Read x and y as integers
x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))

# Calculate and print the distance
distance = euclidean_distance(x, y)
print(f"Euclidean distance from ({x}, {y}) to origin (0, 0): {distance}")
