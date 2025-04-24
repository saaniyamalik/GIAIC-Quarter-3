# In this program we show an example of using dictionaries to keep track of information in a phonebook.

phonebook = {}

def add_contact():
    while True:
        name = input("✨ Enter your contact Name: ").strip()
        if name == "":
            print("❌ Name cannot be empty. Please enter a valid name.")
        else:
            break

    while True:
        number_str = input("📞 Enter your contact number: ").strip()
        if number_str == "":
            print("❌ Contact number cannot be empty. Please enter a valid number.")
            continue
        try:
            number = int(number_str)
            phonebook[name] = number
            print("🎉 Contact Saved Successfully!")
            break
        except ValueError:
            print("🚫 Invalid Input. Please enter digits only.")

def search_contact():
    search_name = input("🔍 Enter name to find: ").strip()
    if search_name == "":
        print("❌ Name cannot be empty.")
        return

    found = False
    for name in phonebook:
        if name.lower() == search_name.lower():  # Case-insensitive comparison
            print(f"💡 {name}'s number is {phonebook[name]}")
            found = True
            break
    if not found:
        print(f"😞 {search_name} not found in phonebook.")

def delete_contact():
    delete_name = input("🗑️ Enter name to delete contact: ").strip()
    if delete_name == "":
        print("❌ Name cannot be empty.")
        return

    found = False
    for name in list(phonebook.keys()):
        if name.lower() == delete_name.lower():  # Case-insensitive comparison
            del phonebook[name]
            print(f"🗑️ {name} deleted successfully!")
            found = True
            break
    if not found:
        print("😞 Name not found.")

def show_all():
    if not phonebook:
        print("📭 Phonebook is empty.")
    else:
        print("📇 All Contacts:")
        for name, number in phonebook.items():
            print(f"🔸 {name}: {number}")

def main():
    while True:
        print("\n============================")
        print("📱 Phonebook Menu")
        print("============================")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Show All Contacts")
        print("5. Exit")
        print("============================")

        choice = input("👉 Enter your choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            show_all()
        elif choice == "5":
            print("👋 Exiting. Thank you!")
            break
        else:
            print("❌ Invalid choice, please choose a valid option (1-5).")

if __name__ == "__main__":
    main()
