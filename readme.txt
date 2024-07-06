Contact Management System

This Contact Management System is a command-line interface (CLI) program that allows users to manage their contacts. The program provides functionality to add, edit, delete, search, display, export, and import contacts.

Features

- Add a new contact with details such as name, phone number, email address, address, and additional notes.
- Edit an existing contact's information.
- Delete a contact by their unique identifier (phone number or email address).
- Search for a contact by their unique identifier and display their details.
- Display a list of all contacts with their unique identifiers.
- Export contacts to a text file in a structured format.
- Import contacts from a text file and add them to the system.

How to Use

Prerequisites

- Python 3.x

Running the Program

1. Clone or Download the Repository:
   git clone https://github.com/donniej5k/contact-management-system.git
   cd contact-management-system

2. Run the Program:
   python contact-program2.py

Menu Options

After running the program, you will see a menu with the following options:

1. Add a new contact:
   - Enter the contact's unique identifier (phone number or email address).
   - Enter the contact's name, phone number, email address, address, and additional notes.
   
2. Edit an existing contact:
   - Enter the unique identifier of the contact to edit.
   - Update the contact's information (leave fields blank to keep current values).
   
3. Delete a contact:
   - Enter the unique identifier of the contact to delete.
   
4. Search for a contact:
   - Enter the unique identifier of the contact to search.
   - The program will display the contact's details if found.
   
5. Display all contacts:
   - Display a list of all contacts with their unique identifiers and details.
   
6. Export contacts to a text file:
   - Enter the filename to export contacts to.
   
7. Import contacts from a text file:
   - Enter the filename to import contacts from.
   
8. Quit:
   - Exit the Contact Management System.

Example Usage

Adding a New Contact:
Enter unique identifier (phone number or email): john.doe@example.com
Enter name: John Doe
Enter phone number: 123-456-7890
Enter email address: john.doe@example.com
Enter address: 123 Main St, Springfield
Enter additional notes: Friend from college
Contact added successfully.

Editing an Existing Contact:
Enter unique identifier of the contact to edit: john.doe@example.com
Editing contact. Leave fields blank to keep current values.
Enter new name (John Doe): Johnathan Doe
Enter new phone number (123-456-7890): 987-654-3210
Enter new email address (john.doe@example.com): johnathan.doe@example.com
Enter new address (123 Main St, Springfield): 456 Elm St, Springfield
Enter new additional notes (Friend from college): Best friend
Contact edited successfully.

Deleting a Contact:
Enter unique identifier of the contact to delete: john.doe@example.com
Contact deleted successfully.

Searching for a Contact:
Enter unique identifier of the contact to search: john.doe@example.com
Contact details:
Name: Johnathan Doe
Phone: 987-654-3210
Email: johnathan.doe@example.com
Address: 456 Elm St, Springfield
Additional Notes: Best friend

Displaying All Contacts:
Identifier: john.doe@example.com
  Name: Johnathan Doe
  Phone: 987-654-3210
  Email: johnathan.doe@example.com
  Address: 456 Elm St, Springfield
  Additional Notes: Best friend

Exporting Contacts to a Text File:
Enter filename to export contacts to: contacts.json
Contacts exported to contacts.json successfully.

Importing Contacts from a Text File:
Enter filename to import contacts from: contacts.json
Contacts imported from contacts.json successfully.

Error Handling

The program includes error handling to manage unexpected issues that may arise during execution. If an error occurs, an appropriate error message will be displayed.

Contact

For any issues or suggestions, please contact Donnie donniej5k@gmail.com

