# 

import jsonschema

from typing import Any


class Field:

    def __init__(self, schema: dict):
        self._schema = schema
        self.value = None

    def clear(self) -> None:
        ''' Clear the value. '''
        self.value = None

    def data(self, k: str, d: Any=None) -> Any:
        ''' Return `schema` value. '''
        return self._schema.get(k, d)

    def validate(self) -> bool:
        ''' Validate the `schema`. '''
        return jsonschema.validate(self._schema)
