import pytest
from contrib.models.validators import date_time_type_validator
from datetime import datetime
from contrib.models.exceptions import ValidationError


class TestModel:
    def test_date_tyme_validator(self):
        data = datetime.now()
        date_time_type_validator(data)

        with pytest.raises(ValidationError):
            data = "not a time"
            date_time_type_validator(data)
