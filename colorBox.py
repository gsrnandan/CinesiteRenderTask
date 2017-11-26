from PyQt4 import QtGui

import constants


class ColorBox(QtGui.QPushButton):
    """ This is a class to create a  color picker with
        a push button to select the color
    """

    def __init__(self, parent=None, color=None):
        super(ColorBox, self).__init__(parent)
        self._user_color = None
        self.setFixedSize(160, 30)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding,
                           QtGui.QSizePolicy.Expanding)
        self.user_color = QtGui.QColor(color or constants.DefaultColor)

        self.clicked.connect(self._change_color)

    # Properties for the color
    @property
    def user_color(self):
        return self._user_color

    @user_color.setter
    def user_color(self, color):
        if isinstance(color, tuple):
            color = QtGui.QColor(color)
        self._user_color = color
        self.setStyleSheet(
            "QPushButton {background-color: rgba(%d, %d, %d, %d)}" % self._user_color.getRgb(
            )
        )

    def _change_color(self):
        col = QtGui.QColorDialog.getColor(self._user_color, self)
        if col.isValid():
            self.user_color = col
