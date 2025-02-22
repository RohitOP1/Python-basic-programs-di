#PROG 4
# Get user input for number of terms
num = int(input("Enter the number of terms: "))

# Generate the power of 2 sequence
result = list(map(lambda x: 2 ** x, range(num)))

# Print the total number of terms
print("The total number of terms are:", num)

# Print each power of 2
for i in range(num):
    print("2 raised to the power", i, "is", result[i])
