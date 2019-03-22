from qt_dotgraph_wheel.dot_to_qt import DotToQtGenerator
from qt_dotgraph_wheel.interactiv_graphics_view import InteractiveGraphicsView

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

 
class Test(QWidget):
     
    def __init__(self):
        super(Test,self).__init__()
         
        self.initUI()
         
         
    def initUI(self):
         
        dot_to_qt = DotToQtGenerator()

        _scene = QGraphicsScene()
        _scene.setBackgroundBrush(Qt.white)
        graphics_view = InteractiveGraphicsView()
        graphics_view.setScene(_scene)

        # with open('rosgraph.dot') as f:
        #     _current_dotcode = f

        try:
            fh = open('qt_dotgraph_wheel/test.dot', 'rb')
            _current_dotcode = fh.read()
            fh.close()
        except IOError:
            return

        # t = RosGraphDotcodeGenerator()
        # self.a = t.generate_dotcode()

        highlight_level = 1

        dot_to_qt.dotcode_to_qt_items(_current_dotcode,highlight_level=highlight_level,same_label_siblings=True,scene=_scene)  
        # dot_to_qt.dotcode_to_qt_items(self.a,highlight_level=highlight_level,same_label_siblings=True,scene=_scene)  

        hlayout = QHBoxLayout()       
        hlayout.addWidget(graphics_view) 
        self.setLayout(hlayout)   
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Test()
    ex.show()
    sys.exit(app.exec_()) 