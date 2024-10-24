from exeptions import PhoneValidationError

default_message = 'Invalid input. Please check your command.'

def input_error(func):
    def inner(*args, **kwargs) -> str:
        try:
            return func(*args, **kwargs)
        except PhoneValidationError as e:
            return e
        except ValueError as e:
            return handle_value_error(func.__name__)
        except IndexError as e:
            return handle_index_error(func.__name__)
        except KeyError as e:
            return handle_key_error(func.__name__, str(e))
        except Exception as e:
            return f"[ERROR]: {str(e)}"
    return inner


def handle_value_error(func_name: str) -> str:
    error_messages = {
        'add_contact': 'Enter both a name and phone number after the "add" command.',
        'change_contact': 'Enter both a name and phone number after the "change" command.'
    }
    return error_messages.get(func_name, default_message)


def handle_index_error(func_name: str) -> str:
    error_messages = {
        'get_phone': 'Enter a name after the "phone" command.'
    }
    return error_messages.get(func_name, default_message)


def handle_key_error(func_name: str, key) -> str:
    error_messages = {
        'add_contact': f'Contact {key} already exists!',
        'change_contact':f'Contact {key} does not exists!',
        'get_phone': f'Contact {key} does not exists!'
    }
    return error_messages.get(func_name, default_message)