class PasswordError(Exception):
    def __init__(self):
        self.message = 'Invalid password'


class LoginError(Exception):
    def __init__(self):
        self.message = 'A user with this email is not registered'


class RegisterError(Exception):
    def __init__(self):
        self.message = 'A user with such an email already exists'


class UserAttributesError(Exception):
    def __init__(self):
        self.message = 'A non-existent user parameter was entered'


class RetreatAttributesError(Exception):
    def __init__(self):
        self.message = 'A non-existent retreat parameter was entered'


class AttributesEnteringError(Exception):
    def __init__(self):
        self.message = 'Error entering parameters'
