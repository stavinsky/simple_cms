from datetime import datetime


def date_time_type_validator(data):
    if not isinstance(data, datetime):
        raise Exception(
            "data type should be Date, but provided {}".format(type(data)))
