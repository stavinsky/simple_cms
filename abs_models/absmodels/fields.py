from .validators import (
    MinLength,
    MaxLength
)


class Field(object):
    def __init__(self, validators=None, null=False, blank=False):
        self.validators = []
        self.null = null
        self.blank = blank
        if validators:
            self.validators += validators

    def clean(self, value):
        value = self.to_python(value)
        for validator in self.validators:
            validator(value)
        return value

    def to_python(self, value):
        return value


class DateTimeField(Field):
    validators = [
    ]


class StringField(Field):
    def __init__(self, validators=None, null=False, blank=False,
                 min_length=None, max_length=None):
        super().__init__(validators=validators, null=null, blank=blank)
        if min_length:
            self.validators.insert(0, MinLength(min_length))
        if max_length:
            self.validators.insert(0, MaxLength(max_length))

    def to_python(self, value):
        return str(value)
