import os

def main_menu():
    print("PS3 Customization Toolkit")
    print("==========================")
    print("WARNING: /dev_blind/ must be enabled in Webman MOD!")
    print("\nSelect your tool")
    print("1. Custom wave")
    print("2. ")
    print("3. Option 3 - Launch script3.py")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        os.system("python3 toolkit/linesqrc.py")
    elif choice == "2":
        os.system("python3 script2.py")
    elif choice == "3":
        os.system("python3 script3.py")
    elif choice == "4":
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()