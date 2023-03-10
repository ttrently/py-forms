#

from typing import Any

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QFormLayout

from pyforms.field import Field
from pyforms.form import Form
from pyforms.renderer import Renderer

from pyforms.renderers.Qt.components import (
    CheckBox,
    Select,
    Text
)


def component_factory(component_map: dict, field: Field) -> Any:
    ''' Returns a component. '''
    component = component_map.get(
        field.data('component', 'text')
    )

    return component(field)


class QtRenderer(Renderer):
    ''' Renderer class. '''

    component_map = {
        'check-box'     : CheckBox,
        'select'        : Select,
        'select-none'   : Select,
        'text'          : Text,
        'text-none'     : Text,
    }

    def render(self, form: Form) -> Any:
        ''' Render the `form`. '''
        frame = QFrame()

        frame.setLayout(QFormLayout())
        frame.layout().setLabelAlignment(Qt.AlignRight)
        frame.layout().setSpacing(2)
        frame.layout().setContentsMargins(2,2,2,2)

        for item in form.model().items():

            name = item.data('label', 'Unknown')
            if not item.data('isRequired'):
                name = f'{name} (Optional)'

            frame.layout().addRow(name, component_factory(self.component_map, item))

        return frame
