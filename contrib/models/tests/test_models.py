import pytest
from contrib.models.validators import (date_time_type_validator,
                                       string_type_validator,
                                       MinLength)
from datetime import datetime
from contrib.models.exceptions import ValidationError
from contrib.models.model import Model
from contrib.models.fields import StringField


class TestModel:
    def test_date_tyme_validator(self):
        data = datetime.now()
        date_time_type_validator(data)

        with pytest.raises(ValidationError):
            data = "not a time"
            date_time_type_validator(data)

    def test_model_clean_correct_data(self):
        class Article(Model):
            str_field = StringField(validators=[MinLength(4)])
        article = Article()
        article.str_field = 'data'
        article.clean_fields()

    def test_model_clane_incorrect_data(self):
        class Article(Model):
            str_field = StringField(validators=[MinLength(10)])
        article = Article()
        article.str_field = 'data1'
        with pytest.raises(ValidationError):
            article.clean_fields()

    def test_model_clean_min_lenth_by_param(self):
        class Article(Model):
            str_field = StringField(min_length=6, validators=[])
        article = Article()
        article.str_field = "data2"
        article.clean_fields()

    def test_model_clean_max_lenth_by_param(self):
        class Article(Model):
            str_field = StringField(max_length=4, validators=[])
        article = Article()
        article.str_field = "data2"
        article.clean_fields()
