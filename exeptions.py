class PhoneValidationError(Exception):
    def __init__(self, message: str = 'Phone number must be 10 digits like "0000000000"'):
        self.message = message
        super().__init__(self.message)


class PhoneDuplicate(Exception):
    def __init__(self, message: str = 'Entered phone number already exists for this user', entered_phone: str = None, entered_name: str = None):
        self.entered_phone = entered_phone
        self.entered_name = entered_name
        self.message = message
        super().__init__(message)


# class ContactDuplcate(Exception):
#     def __init__(self, message: str = 'Contact with entered name already exists', entered_name:str = None):
#         self.entered_name = entered_name
#         self.message = message
#         super().__init__(message)


class RecordNotFound(Exception):
    def __init__(self, message: str = 'Entered contact not found', entered_name: str = None):
        self.entered_name = entered_name
        self.message = message
        super().__init__(message)


class PhoneNotFound(Exception):
    def __init__(self, message: str = 'Phone number not found', entered_phone: str = None, entered_name: str = None):
        self.entered_phone = entered_phone
        self.entered_name = entered_name
        self.message = message
        super().__init__(message)