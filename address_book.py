from collections import UserDict
from exeptions import PhoneValidationError, PhoneDuplicate
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
        if not re.match(r'^\d{10}$', value):
            raise PhoneValidationError()
        self.value = value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, new_phone: str):
        for phone in self.phones:
             if phone.value == new_phone:
                  raise PhoneDuplicate()
        self.phones.append(Phone(new_phone))

    def remove_phone(self, phone_to_remove: str):
        init_phones_lenght = len(self.phones)
        self.phones = [phone for phone in self.phones if phone.value != phone_to_remove]
        return init_phones_lenght > len(self.phones)

    def edit_phone(self, phone_to_edit: str, new_phone: str):
        for phone in self.phones:
            if phone.value == phone_to_edit:
                phone.value = new_phone
                return True
        return False

    def find_phone(self, phone_search: str):
        for phone in self.phones:
             if phone.value == phone_search:
                  return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: \n{'\n'.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def remove_record(self, name: str):
        if name in self.data:
            del self.data[name]

    def find_record(self, name: str):
        return self.data.get(name, None)
