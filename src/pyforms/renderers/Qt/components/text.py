
from typing import Any

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLineEdit

from pyforms.field import Field
from pyforms.renderer import Component


class Text(QLineEdit, Component):
    ''' Text component class.
    
    This class represents a `text` component as a `QLineEdit`.
    '''

    changed = pyqtSignal()

    def __init__(self, field: Field):
        super().__init__()

        self._field = field

        self.setup()

    def setup(self):
        ''' Setup the component. '''
        pass
