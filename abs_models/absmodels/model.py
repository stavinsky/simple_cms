import json
from .fields import Field


class Model(object):
    @classmethod
    def get_fields(cls):
        fields = []
        for attr in dir(cls):
            if attr.startswith('_'):
                continue
            if isinstance(getattr(cls, attr), Field):
                fields.append(attr)
        return fields

    def clean_fields(self):
        for field in self.get_fields():
            clean = getattr(type(self), field).clean
            cleaned_field = clean(getattr(self, field))
            setattr(self, field, cleaned_field)

    def to_json(self):
        data = {field: getattr(self, field) for field in self.get_fields()}
        return json.dumps(data)
