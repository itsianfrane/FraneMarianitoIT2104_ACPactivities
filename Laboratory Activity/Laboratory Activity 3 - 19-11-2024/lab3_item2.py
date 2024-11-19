def is_perfect_number(n):
    if n <= 0:
        return False
    
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    return divisors_sum == n

def main():
    user_input = input("Enter a number: ")
    
    try:
        number = int(user_input) 
        if is_perfect_number(number):
            print(f"{number} is a perfect number.")
        else:
            print(f"{number} is not a perfect number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()