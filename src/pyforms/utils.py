#

import re

from typing import Any


def pretty_name(name: str)->str:
    ''' Returns a pretty name.
    
    This function will convert a name such as "someName" to "Some Name".
    '''
    result = re.sub(
        '([A-Z][a-z]+)', name
    ).split()

    return ' '.join(result)


class RenderMixin:
    ''' Render mixin class. '''

    def render(self, renderer: object=None) -> None:
        ''' Render the parent class.
        
        Uses the given `Renderer` instance to render the form.
        '''
        return renderer.render(self)
