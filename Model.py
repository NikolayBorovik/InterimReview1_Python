import datetime
import json

def read_notes_from_json (file):
    with open (file, 'r') as data:
        try:
            notes = json.load(data)
            return notes
        except json.JSONDecodeError:
            print('There are no entries in the notes.')
            pass
    
def save_notes_json(file, notes):
    with open(file, 'w') as data:
        json.dump(notes, data)

def filter_notes_by_date (notes, date):
    filtered_notes = []
    for note in notes:
        note_date = datetime.datetime.strptime(note['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        if note_date.date() == date:
            filtered_notes.append(note)
    return filtered_notes

def print_notes(notes):
    if not notes:
        print('No notes found')
    else:
        for note in notes:
            print(f'ID: {note["id"]}')
            print(f'Title: {note["title"]}')
            print(f'Body: {note["body"]}')
            print(f'Timestamp: {note["timestamp"]}')
            print('---')

def add_note(notes):
    id = len(notes) + 1
    title = input('Введите заголовок: ')
    body = input('Введите тело заметки: ')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    new_note = {'id': id, 'title': title, 'body': body, 'timestamp': timestamp}
    notes.append(new_note)
    return notes

def delete_note(notes, id):
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            break
    return notes
    

def change_note(notes, id):
    for note in notes:
        if note['id'] == id:
            new_title = input(f'The old note title is: {note["title"]}. Enter a new note title: ')
            note['body'] = input('Enter a new note doby: ')
            note['title'] = new_title
            note['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            break
    return notes



