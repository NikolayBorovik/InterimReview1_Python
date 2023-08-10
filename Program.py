import sys
import json
from Model import *

def main():
    # with open('notes.json', 'w') as f:
    #     print("The json file is created")
    file_name = 'notes.json'
    notes = read_notes_from_json(file_name)
    while True:
        print('You can:')
        print('1. Print all notes')
        print('2. Print notes filtered by a certain date')
        print('3. Print a certain note')
        print('4. Add a new note')
        print('5. Edit a note')
        print('6. Delete a note')
        print('7. Exit the program')
        user_choice = input('Please, enter your choice: ')
        if user_choice == '1':
            print_notes(notes)
        elif user_choice == '2':
            date_str = input('Enter a filter date as YYY-MM-DD: ')
            try:
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                print('Invalid date format. ')
                continue
            filtered_notes = filter_notes_by_date(notes, date)
            print_notes(filtered_notes)
        elif user_choice == '3':
            id = int(input('Enter the note ID: '))
            note = [note for note in notes if note['id'] == id]
            print_notes(note)
        elif user_choice == '4':
            notes = add_note(notes)
            save_notes_json(file_name, notes)
        elif user_choice == '5':
            id = int(input('Enter the note id to edit: '))
            notes = change_note(notes, id)
            save_notes_json(file_name, notes)
        elif user_choice == '6':
            id = int(input('Enter the note id to delete: '))
            notes = delete_note(notes, id)
            save_notes_json(file_name, notes)
        elif user_choice == '7':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()


# def cycleMatch(file):
#     match getStr(youCanDo):
#         case '1':
#             addContact(file, getStr(addContactPrompt))
#             print(whatsnextPrompt)
#             cycleMatch(file)
#         case '2':
#             showAllContacts(file)
#             print(whatsnextPrompt)
#             cycleMatch(file)
#         case '3':
#             searchByLastName(file, getStr(searchPrompt))
#             print(whatsnextPrompt)
#             cycleMatch(file)
#         case '4':
#             deleteLine(file, getStr(deletePrompt))
#             print(whatsnextPrompt)
#             cycleMatch(file)
#         case '5':
#             changeLine(file, getStr(changePrompt1), getStr(changePrompt2))
#             print(whatsnextPrompt)
#             cycleMatch(file)
#         case '6':
#             sys.exit(bye)
#         case _:
#             print(wrong)
#             print(whatsnextPrompt)
#             cycleMatch(file)