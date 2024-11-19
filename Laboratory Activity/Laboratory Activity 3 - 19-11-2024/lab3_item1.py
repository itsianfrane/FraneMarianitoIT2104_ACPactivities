def roman_to_integer(roman):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Convert the Roman numeral to uppercase
    roman = roman.upper()
    total = 0
    prev_value = 0

    # Process the Roman numeral from right to left
    for char in reversed(roman):
        if char in roman_values:
            value = roman_values[char]
            if value < prev_value:
                total -= value  # Subtract if the current value is less than the previous
            else:
                total += value  # Add otherwise
            prev_value = value
        else:
            print(f"Invalid Roman numeral character: {char}")
            return None

    return total

def main():
    roman_input = input("Enter a Roman numeral: ")
    result = roman_to_integer(roman_input)
    
    if result is not None:
        print(f"The integer value of '{roman_input.upper()}' is: {result}")

if __name__ == "__main__":
    main()