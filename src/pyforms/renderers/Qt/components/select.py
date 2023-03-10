
from typing import Any

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QComboBox

from pyforms.field import Field
from pyforms.renderer import Component


class Select(QComboBox, Component):
    ''' Select component class. 
    
    This class represents a `select` component as a `QComboBox`.
    '''

    changed = pyqtSignal()

    def __init__(self, field: Field):
        super().__init__()

        self._field = field

        self.setup()

    def field(self) -> Any:
        return self._field

    def setup(self) -> None:
        ''' Setup the component. '''
        self.setModel(QStandardItemModel())

        self.model().clear()
        self.model().appendRow(QStandardItem(''))

        for d in self.field().data('options', []):
            item = QStandardItem(d['label'])
            item.setData(d, Qt.UserRole + 1)

            self.model().appendRow(item)

        self.currentIndexChanged.connect(self.on_changed)

    def on_changed(self, index: int) -> None:
        ''' Callback on component value changed. '''
        item = self.model().item(index)
        data = item.data(Qt.UserRole + 1)
        self.field().value = data.get('value')
        print(item)

        self.changed.emit()
