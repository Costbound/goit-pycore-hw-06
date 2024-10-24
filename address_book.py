from collections import UserDict
from exeptions import PhoneValidationError
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
    def __init__(self, value: str):
        filtered_value = re.sub(r'\D', '', value)
        if len(filtered_value) != 2:
              raise PhoneValidationError('Phone number must be 10 digits')
        self.value = filtered_value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, new_phone: str):
        self.phones.append(Phone(new_phone))

    def remove_phone(self, phone_to_remove: str):
        self.phones = [phone for phone in self.phones if phone.value != phone_to_remove]

    def edit_phone(self, phone_to_edit: str, new_phone: str):
        for phone in self.phones:
            if phone.value == phone_to_edit:
                phone.value = new_phone
                break

    def find_phone(self, phone_search: str):
        for phone in self.phones:
             if phone.value == phone_search:
                  return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = []
    
    def add_record(self, record: Record):
        self.data.append(record)

    def remove_record(self, name: str):
        self.data = [record for record in self.data if record.name != name]

    def find_record(self, name: str):
        for record in self.data:
            if record.name.value == name:
                 return record
        return None

