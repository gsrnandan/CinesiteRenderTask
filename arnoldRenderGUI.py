import os
from PyQt4 import QtGui

import constants
from arnoldRenderScene import ArnoldRenderScene as _ArnoldRenderScene
from colorBox import ColorBox as _ColorBox


class ArnoldRenderWindow(QtGui.QWidget):
    """ This is a class to create a Window to render an object in arnold,
        display the image in a viewer and read the render log as a text file.

    """

    def __init__(self, parent=None):
        super(ArnoldRenderWindow, self).__init__(parent=parent)

        self.arnold_render_scene = _ArnoldRenderScene(
            constants.SceneName,
            constants.DefaultColor
        )

        # Create the Widgets for Image Viewer and Log Reader
        self._create_widgets()
        self._connect_slots()

    def _create_widgets(self):
        """ This method creates the layout and the buttons
            for the widget GUI
        """

        self.image_viewer = QtGui.QLabel('Render Image')
        self.log_viewer = QtGui.QTextEdit('Render Log')
        self.log_viewer.setMinimumWidth(400)

        # Create the buttons for render and setting Color
        self.render_btn = QtGui.QPushButton('Render')
        self.setColor_btn = _ColorBox(
            "Set Color", color=constants.DefaultColor)
        main_layout = QtGui.QVBoxLayout()
        top_layout = QtGui.QHBoxLayout()
        bottom_layout = QtGui.QHBoxLayout()
        top_layout.addWidget(self.image_viewer)
        top_layout.addWidget(self.log_viewer)
        bottom_layout.addWidget(self.render_btn)
        bottom_layout.addWidget(self.setColor_btn)
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

    def _connect_slots(self):
        """ Method to connect the render button to the call_render function

        """
        self.render_btn.clicked.connect(self._call_render)

    def _call_render(self):
        """ Method to render the object and display the image file and render log

        """
        self.arnold_render_scene.setColor(
            self.setColor_btn.user_color.getRgb())
        self.arnold_render_scene.renderGeo()
        self._set_image(self.arnold_render_scene.image)
        self._set_text(self.arnold_render_scene.log)

    def _set_image(self, path):
        """ Method to read the image path and set it in the image viewer

            Args:
                path(string): Takes the path of the image and loads the image

        """
        if os.path.exists(path):
            image = QtGui.QPixmap(path)
            self.image_viewer.setPixmap(image)

    def _set_text(self, path):
        """ Method to read the path of the render log and set it in the text viewer

            Args:
                path(string): Takes the path of the text file and loads
                the text
        """
        if os.path.exists(path):
            with open(path, 'r') as f:
                self.log_viewer.setPlainText("".join(f.readlines()))


if __name__ == '__main__':
    app = QtGui.QApplication([])
    widget = ArnoldRenderWindow()
    widget.show()
    app.exec_()
