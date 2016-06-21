from .validators import date_time_type_validator


class Field(object):
    def __init__(self, validators=None):
        if validators:
            self.validators += validators
    validators = []

    @staticmethod
    def clean(data):
        pass


class DateTimeField(Field):
    validators = [
        date_time_type_validator,
    ]

    def clean(self, data):
        for validator in self.validators:
            validator(data)
