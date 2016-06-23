import pytest
from contrib.models.validators import (MinLength)
from contrib.models.exceptions import ValidationError
from contrib.models.model import Model
from contrib.models.fields import StringField


class TestModel:
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
            str_field = StringField(min_length=5, validators=[])
        article = Article()
        article.str_field = "data2"
        article.clean_fields()

    def test_model_clean_max_lenth_by_param(self):
        class Article(Model):
            str_field = StringField(max_length=4, validators=[])
        article = Article()
        article.str_field = 1234
        article.clean_fields()

    def test_model_clean_max_lenth_by_param_incorrect(self):
        class Article(Model):
            str_field = StringField(max_length=4, validators=[])
        article = Article()
        article.str_field = "data1"
        with pytest.raises(ValidationError):
            article.clean_fields()
