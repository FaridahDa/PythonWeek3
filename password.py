supplied_pin = "7890"
attempt = 1
while attempt < 4:
    pin = input("Enter your pin:")
    if pin == supplied_pin:
        print("Your pin was successful, Welcome!")
    else:
        print("Your pin was incorrect, please try again." + "" + "You have tried" + str(attempt) + "" + "times")
    attempt = attempt + 1
    if attempt == 4:
        print("Sorry you are now locked out")






