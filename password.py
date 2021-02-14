supplied_pin = "7890"
first_attempt = input("Enter your pin:")
if supplied_pin == first_attempt:
    print("Your pin was sucessful, Welcome")
elif supplied_pin != first_attempt:
    print("Your pin was wrong, you have 2 more attempts")

    second_attempt = input("Enter your pin")
    if supplied_pin == second_attempt:
        print("Your pin was sucessful, Welcome")
    elif supplied_pin != second_attempt:
        print("Your pin was wrong, you have one more attempt")

        third_attempt = input("Enter your pin")
        if supplied_pin == third_attempt:
            print("Your pin was sucessful, Welcome")
        else:
            print("Your pin was wrong, you are now locked out")
