import gps


def print_menu():
    print(30 * "-", "TelloJDAM", 30 * "-")
    print("1. Menu Option 1")
    print("2. Menu Option 2")
    print("3. Menu Option 3")
    print("4. Exit")
    print(67 * "-")


loop = True
while loop:
    print_menu()
    choice = input("Enter your choice [1-4]: ")
    if choice == 1:
        print("Menu 1 has been selected")
        gps.main()
    elif choice == 2:
        print("Menu 2 has been selected")
    elif choice == 3:
        print("Menu 3 has been selected")
    elif choice == 4:
        print("Exit")
        loop = False
    else:
        input("Wrong option selection. Enter any key to try again..")
