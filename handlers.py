from err_handlers import input_error
from address_book import Record

@input_error
def add_contact(args, contacts):
    name, phone = args

    if contacts.find_record(name):
        raise KeyError(name)
    
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return f'Contact "{name}" added.'

@input_error
def change_contact(args, contacts):
    name, phone_to_change, new_phone = args
    record = contacts.find_record(name)

    if not(record):
        raise KeyError(name)
    
    record.edit_phone(phone_to_change, new_phone)
    return f'Contact "{name}" modified.'

@input_error
def get_phone(args, contacts):
    name = args[0]
    return f'{name}: {contacts[name]}'

def get_all_contacts(contacts):
    contact_strings = []
    for key, value in contacts.items():
        contact_strings.append(f'{key}: {value}')
    return '\n'.join(contact_strings)