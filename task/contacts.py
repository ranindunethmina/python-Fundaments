def view_contacts():
    with open("task\contacts.txt", "r") as file:
        content = file.readlines()
        for contact in content:
            print(contact)

def add_contacts():
    name = input("Enter your name:")
    phone_num = input("Enter your Phone Number:")
    email = input("Enter your email address:")
    with open("task\contacts.txt", "a") as file:
        new_contact = name + "," + phone_num + "," + email + "\n"
        file.write(new_contact)
    print("Added Successfully")
    
while True:
    print("\nContact Management System")
    print("1. View Contact")
    print("2. Add Contacts")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        view_contacts()
    elif choice == "2":
        add_contacts()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")