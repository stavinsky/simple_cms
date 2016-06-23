import abc
from datetime import datetime
from .exceptions import ValidationError


class Validator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def clean(self, value):
        pass

    def __call__(self, value):
        self.clean(value)


class MinLength(Validator):
    def __init__(self, min_value):
        self.min_value = min_value

    def clean(self, value):
        if len(value) < self.min_value:
            raise ValidationError(
                """value should be not less than {min_value}, \
provided {value}""".format(min_value=self.min_value, value=value))


class MaxLength(Validator):
    def __init__(self, max_value):
        self.max_value = max_value

    def clean(self, value):
        if len(value) > self.max_value:
            raise ValidationError(
                """value should be not less than {max_value},
    provided {value}""".format(max_value=self.max_value, value=value))
