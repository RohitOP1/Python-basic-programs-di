rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
array = []

for i in range(rows):
    while True:  # Loop until valid input is provided
        row = list(map(int, input(f"Row {i + 1} (enter {cols} integers): ").split()))
        if len(row) == cols:  # Check if the number of columns matches
            array.append(row)
            break
        else:
            print(f"Error")

print("2D Array:")
for row in array:
    print(" ".join(map(str, row)))
