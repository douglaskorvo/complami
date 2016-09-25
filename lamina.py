import sys
import numpy as np
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "lamina.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.calcular.clicked.connect(self.clicar)
		self.radioButton_2.toggled.connect(self.calc_tensao)
		self.radioButton.toggled.connect(self.calc_def)
#Funcao para desabilitar os campos de deformacao quando o checkbox da tensao estiver com o sinal "toggled"
#Esta funcao habilita tambem os campos que eventualmente estejam desabilitados, caso clique por engano em um dos "checkbox"
	def calc_tensao(self):
		self.textEdit_6.setDisabled(True) 
		self.textEdit_7.setDisabled(True)
		self.textEdit_8.setDisabled(True)
 		self.textEdit_9.setDisabled(False)
		self.textEdit_10.setDisabled(False)
		self.textEdit_11.setDisabled(False)
#Funcao para desabilitar os campos de tensao quando o checkbox da deformacao estiver com o sinal "toggled"
#Esta funcao habilita tambem os campos que eventualmente estejam desabilitados, caso clique por engano em um dos "checkbox"	
	def calc_def(self):
		self.textEdit_9.setDisabled(True)
		self.textEdit_10.setDisabled(True)
		self.textEdit_11.setDisabled(True)
		self.textEdit_6.setDisabled(False)
		self.textEdit_7.setDisabled(False)
		self.textEdit_8.setDisabled(False)
		
#Essa funcao clicar() carrega os valores digitados pelo usuario
#Testa se todos os campos foram preenchidos		
#Calcula Q, S, Qbarra, Qbarra, Deformacoes locais e globais e tensoes locais e globais para uma lamina unidirecional

	def clicar(self):
#S = [1/E1 -v21/E2 0
#-v12/E1 1/E2 0
#0 0 1/G12];
#lendo os valores que estao no formulario Qt e fazendo o tratamento de erro
		if not self.radioButton.isChecked() or not self.radioButton_2.isChecked():
			self.textBrowser.setText("Entre com os dados de tensao ou deformacao")
		try:
			e1 = self.e1.toPlainText()
			e1=float(e1)
			e2 = self.e2.toPlainText()
			e2 = float(e2)
			v12 = self.v12.toPlainText()
			v12 = float(v12)
			g12 = float(self.g12.toPlainText())
			#g12 = float(g12)
			v21 = e2*v12/e1
			a = float(self.angulo.toPlainText())
			S = np.array([1/e1, -v21/e2, 0, -v12/e1, 1/e2, 0, 0, 0, 1/g12]).reshape(3,3)
			Q = np.linalg.inv(S)
			pass
		except ValueError:
			self.textBrowser.setText("Confirme se todos os dados de input estao preenchidos e sao numericos") #mensagem de erro caso haja algum erro de preenchimento no form 
		#Bloco de codigo que calcula a partir das tensoes ou deformacoes, de acordo com os inputs que alimentarem o sistema
		if self.radioButton.isChecked():
			resposta = "CALCULANDO AS TENSOES" + "\n"+"\n"
			
			resposta = resposta + "\n" + "MATRIZ S" + "\n" +str(S)+"\n"
			resposta = resposta + "\n" + "MATRIZ Q" + "\n" +str(Q)
			self.textBrowser.setText(resposta)
		elif self.radioButton_2.isChecked():
			resposta = "CALCULANDO AS DEFORMACOES" + "\n"+"\n"
			tensao = np.array([[self.textEdit_6,self.textEdit_7,self.textEdit_8]])
			
			resposta = resposta + "\n" + "MATRIZ S" + "\n" +str(S)+"\n"
			resposta = resposta + "\n" + "MATRIZ Q" + "\n" +str(Q)
			self.textBrowser.setText(resposta)
	#Funcao vazia por enquanto
	def qbarra():
		 pass
		
        
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


