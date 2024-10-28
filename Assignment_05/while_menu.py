#This program gives a small riddle with 2 options
#Choose wisely :)

#Prime the while statement
menu_option =''
while menu_option != 'q':
    print("I speak without a mouth and hear without ears. I have no body, but i come alive with wind. What am i?: \n"
          "a) A Shadow \n"
          "b) A Echo \n"
          "q) quit ")
    menu_option = input("Choose a letter to select your answer: ")
    if menu_option == 'a':
        print("Wrong!! idk why you would think a shadow? Pfft, dont even bother trying again")
    elif menu_option == "b":
        choice = input("Nice! you're smarter then you look ;), would you like to try again? (y/n): ")
        if choice == "y":
            print("okay! back to the menu -->")
        else:
            menu_option = "q"
    else:
        print("Goodbye")
        menu_option == "q"

