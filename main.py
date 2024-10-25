from handlers import add_contact, change_contact, get_phones, get_all_contacts
from address_book import AddressBook

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(get_phones(args, contacts))
        elif command == 'all':
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
