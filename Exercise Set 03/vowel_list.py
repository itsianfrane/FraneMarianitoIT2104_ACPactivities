name_input = input("Enter a string: ")

vowels = 'aeiouAEIOU'

vowel_list = [char for char in name_input if char in vowels]

print(vowel_list)
