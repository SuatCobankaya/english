from    PyQt5.QtWidgets import QApplication
from anasayfa import anapencere
app = QApplication([])
pencere = anapencere()
pencere.show()
app.exec_()