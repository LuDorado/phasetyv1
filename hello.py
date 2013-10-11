# Create your views here.

#!/usr/bin/env python

# example radiobuttons.py
# Riber decime que se siente...

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
    
# dediquense a programar!

    sys.exit(app.exec_())
