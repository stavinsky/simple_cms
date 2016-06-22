from datetime import datetime
from .exceptions import ValidationError


def date_time_type_validator(data):
    if not isinstance(data, datetime):
        raise ValidationError(
            "data type should be Date, but provided {}".format(type(data)))
