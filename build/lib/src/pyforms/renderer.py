#

from typing import Any

from pyforms.field import Field
from pyforms.form import Form


class Component:
    ''' Component class.
    
    All renderer components should subclass from this.
    '''

    changed = None

    def bind(self, field: Field) -> bool:
        ''' Bind component information. '''
        pass

    def value(self) -> Any:
        ''' Return component value. '''
        raise NotImplementedError(
            'Component `value` method must be defined in the subclass.'
        )


class Renderer:
    ''' Renderer class.
    
    All renderers should subclass from this.
    '''

    # component map between component name `str` - and component `class`.
    component_map = {}

    def render(self, form: Form):
        ''' Render the `form`. '''
        raise NotImplementedError(
            'Renderer `render` method must be defined in the subclass.'
        )
