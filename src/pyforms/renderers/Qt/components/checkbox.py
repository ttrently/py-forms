
from PyQt5.QtWidgets import QCheckBox

from pyforms.field import Field
from pyforms.renderer import Component


class CheckBox(QCheckBox, Component):
    ''' Checkbox component class.
    
    This class represents a `check-box` component as a `QCheckBox`.
    '''

    def __init__(self, field: Field):
        super().__init__()

        self._field = field

        self.setup()

    def setup(self):
        ''' Setup the component. '''
        pass
