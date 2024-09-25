while True:
    total_purchase = float(input("Enter the total purchase amount: "))

    if total_purchase > 5000:
        discount = 0.10
    else:
        discount = 0.05

    discount_amount = total_purchase * discount
    final_price = total_purchase - discount_amount

    print(f"Initial Purchase Amount: {total_purchase:.2f}")
    print(f"Discount: {discount_amount:.2f}")
    print(f"Final Price: {final_price:.2f}")

    try_again = input("Do you want to try again? (yes/no): ").lower()
      
    if try_again != "yes":
        print("Thank you!")
        break

    