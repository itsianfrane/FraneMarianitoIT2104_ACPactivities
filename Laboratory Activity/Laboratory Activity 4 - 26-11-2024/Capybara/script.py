from Capybara import Capybara

test_case_number = int(input("Enter the test case number: "))

if test_case_number == 1:
    capybara1 = Capybara("Biscoff", "M", 5)
    print("Test Case 1: ", end="")
    capybara1.display_info()

