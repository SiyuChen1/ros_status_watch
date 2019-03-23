from qt_dotgraph_wheel.dot_to_qt import DotToQtGenerator
from qt_grahview.interactiv_graphics_view import InteractiveGraphicsView
from qt_dotgraph_wheel.generate_graph import from_graph_generate_dot

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QApplication,QHBoxLayout,QGraphicsScene
from PyQt5.QtGui import *

 
class StatusCheck(QWidget):
     
    def __init__(self):
        super(StatusCheck,self).__init__()
         
        self.initUI()

        self.get_dot_convert_to_scene()
             
    def initUI(self): 
        self._scene = QGraphicsScene()
        self._scene.setBackgroundBrush(Qt.white)
        self.graphics_view = InteractiveGraphicsView()
        self.graphics_view.setScene(self._scene)

        hlayout = QHBoxLayout()       
        hlayout.addWidget(self.graphics_view) 
        self.setLayout(hlayout)

    def open_dot_files(self):
        try:
            fh = open('qt_dotgraph_wheel/test.dot', 'rb')
            _current_dotcode = fh.read()
            fh.close()
        except IOError:
            return

    def get_dot_convert_to_scene(self):
        # generate dot_to_qt generator 
        self.dot_to_qt = DotToQtGenerator()

        # get current dot code
        _current_dotcode = from_graph_generate_dot()

        self.highlight_level = 1

        self.dot_to_qt.dotcode_to_qt_items(_current_dotcode,highlight_level=self.highlight_level,same_label_siblings=True,scene=self._scene) 
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    status_check = StatusCheck()
    status_check.show()
    sys.exit(app.exec_()) 