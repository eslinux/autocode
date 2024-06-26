# 1. Install python
# 	https://www.python.org/downloads/
	
# 2. Install PyQT5
# 	$ pip install pyqt5
	
# 3. Download QT Designer
# 	https://build-system.fman.io/qt-designer-download
	
# 4. Open QT Designer and create GUI file
#    Ex: MainWidget.ui (base QWidget) 
#        MainWindow.ui (base QMainWindow)
   
# 5. Create python app
# 5.1 Method 1
# 	Convert ui file to python
# 	$ pyuic5 -x MainWindow.ui -o MainWindow.py
# 5.2 Method 2
# 	Use loadui function to load MainWindow.ui
	
# 	------------------MainWindow.py---------------
# 	import sys
# 	from PyQt5 import uic
# 	from PyQt5.QtWidgets import *

# 	class MyApp(QMainWindow): #or QWidget if load MainWidget.ui
# 		def __init__(self):
# 			super().__init__()
# 			uic.loadUi("MainWindow.ui", self)
# 			self.setWindowTitle("Home")
			
# 			self.myButton = self.findChild(QPushButton, "myButton")
# 			self.myButton.clicked.connect(self.say_hello)
		
# 		def say_hello(self):
# 			print("hello world !")

# 	if __name__ == "__main__":
# 		app = QApplication(sys.argv)
# 		myApp = MyApp()
# 		myApp.show()
# 		try:
# 			sys.exit(app.exec())
# 		except SystemExit:
# 			print("close app")
# 	----------------------------------------------
	
# 6. Run app
# 	$ python MainWindow.py
	
# 	* MainWindow.py & MainWindow.ui are set of app