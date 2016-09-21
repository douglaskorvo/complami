import sys
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "form.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.botaoclicar.clicked.connect(self.clicar)
    
    def clicar(self):
        i=1
        texto = "Voce clicou " + str(i) + " vez."
        self.label1.setText(texto)
        
               
        
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


