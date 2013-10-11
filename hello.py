# Create your views here.

#!/usr/bin/env python

# example radiobuttons.py

import sys
from PyQt4 import QtCore, QtGui
 
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    model = QtGui.QDirModel()
    tree = QtGui.QTreeView()
    tree.setModel(model)
    
    tree.setWindowTitle(tree.tr("Vista Directorio"))
    tree.resize(320, 480)
    tree.show()
    
    sys.exit(app.exec_())
