char1, char2 = input("Enter two space-seperated characters: ").split()

greater_char = max(char1, char2)
print("-------------------------------------")
print(f"The character with greater value is: {greater_char}")
print("-------------------------------------")

print("Showing ASCII Values: ")
print(f"{char1} : {ord(char1)}")
print(f"{char2} : {ord(char2)}")