#PROG 1
# Taking user input
username = input("Enter your name: ")

while len(username) < 3:
    print("Name must be at least 3 characters long.")
    username = input("Enter your name: ")

template = "Hello <<UserName>>, How are you?"
output = template.replace("<<UserName>>", username)
print(output)
