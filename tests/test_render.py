
import sys

from pathlib import Path

from PyQt5.QtWidgets import QApplication

from pyforms.form import Form
from pyforms.renderers.Qt import QtRenderer


def main():
    app = QApplication([])

    form = Form.load(
        Path(Path(__file__).parent, 'test.JSON')
    )

    render = form.render(QtRenderer())
    render.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
