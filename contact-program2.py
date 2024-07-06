import re
import json

class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}

    def display_menu(self):
        print("Welcome to the Contact Management System!")
        print("Menu:")
        print("1. Add a new contact")
        print("2. Edit an existing contact")
        print("3. Delete a contact")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Export contacts to a text file")
        print("7. Import contacts from a text file")
        print("8. Quit")

    def add_contact(self):
        unique_id = input("Enter unique identifier (phone number or email): ")
        if unique_id in self.contacts:
            print("Contact with this identifier already exists.")
            return
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        additional_notes = input("Enter additional notes: ")

        self.contacts[unique_id] = {
            'Name': name,
            'Phone': phone,
            'Email': email,
            'Address': address,
            'Additional Notes': additional_notes
        }
        print("Contact added successfully.")

    def edit_contact(self):
        unique_id = input("Enter unique identifier of the contact to edit: ")
        if unique_id not in self.contacts:
            print("Contact not found.")
            return
        print("Editing contact. Leave fields blank to keep current values.")
        name = input(f"Enter new name ({self.contacts[unique_id]['Name']}): ") or self.contacts[unique_id]['Name']
        phone = input(f"Enter new phone number ({self.contacts[unique_id]['Phone']}): ") or self.contacts[unique_id]['Phone']
        email = input(f"Enter new email address ({self.contacts[unique_id]['Email']}): ") or self.contacts[unique_id]['Email']
        address = input(f"Enter new address ({self.contacts[unique_id]['Address']}): ") or self.contacts[unique_id]['Address']
        additional_notes = input(f"Enter new additional notes ({self.contacts[unique_id]['Additional Notes']}): ") or self.contacts[unique_id]['Additional Notes']

        self.contacts[unique_id] = {
            'Name': name,
            'Phone': phone,
            'Email': email,
            'Address': address,
            'Additional Notes': additional_notes
        }
        print("Contact edited successfully.")

    def delete_contact(self):
        unique_id = input("Enter unique identifier of the contact to delete: ")
        if unique_id in self.contacts:
            del self.contacts[unique_id]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def search_contact(self):
        unique_id = input("Enter unique identifier of the contact to search: ")
        if unique_id in self.contacts:
            print("Contact details:")
            for key, value in self.contacts[unique_id].items():
                print(f"{key}: {value}")
        else:
            print("Contact not found.")

    def display_all_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for unique_id, details in self.contacts.items():
            print(f"Identifier: {unique_id}")
            for key, value in details.items():
                print(f"  {key}: {value}")
            print("")

    def export_contacts(self):
        filename = input("Enter filename to export contacts to: ")
        with open(filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)
        print(f"Contacts exported to {filename} successfully.")

    def import_contacts(self):
        filename = input("Enter filename to import contacts from: ")
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
            print(f"Contacts imported from {filename} successfully.")
        except FileNotFoundError:
            print("File not found.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")
            try:
                if choice == '1':
                    self.add_contact()
                elif choice == '2':
                    self.edit_contact()
                elif choice == '3':
                    self.delete_contact()
                elif choice == '4':
                    self.search_contact()
                elif choice == '5':
                    self.display_all_contacts()
                elif choice == '6':
                    self.export_contacts()
                elif choice == '7':
                    self.import_contacts()
                elif choice == '8':
                    print("Exiting the Contact Management System. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    cms = ContactManagementSystem()
    cms.run()
