#

import json

from typing import Any

from pyforms.field import Field
from pyforms.model import Model
from pyforms.utils import RenderMixin


class Form(RenderMixin):
    ''' Form class. '''

    def __init__(self, model: Model=None):
        self._model = model or Model()

    def model(self) -> Model:
        return self._model

    def submit(self) -> bool:
        ''' Submit the form.
        
        This method should hook an external callback.
        '''
        return True
    
    @classmethod
    def load(cls, form: str) -> Any:
        ''' Loads a form. '''
        new = cls()

        with open(form) as handle:
            content = json.load(handle)

            for item in content:
                item = Field(item)
                
                new.model()._items.append(
                    item
                )

        return new
