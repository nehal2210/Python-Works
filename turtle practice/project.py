# # from turtle import *
# # color('red', 'yellow')
# # begin_fill()
# # while True:
# #     forward(200)
# #     left(170)
# #     if abs(pos()) < 1:
# #         break
# # end_fill()
# # done()

# import turtle as t
# a=t.position()
# print(a)
# t.circle(120,60)
# t.done()   


import sys
from PyQt5 import QtGui

# def window():
#    app = QtGui.QApplication(sys.argv)
#    w = QtGui.QWidget()
#    b = QtGui.QLabel(w)
#    b.setText("Hello World!")
#    w.setGeometry(100,100,200,50)
#    b.move(50,20)
#    w.setWindowTitle(“PyQt”)
#    w.show()
#    sys.exit(app.exec_())
	
# if __name__ == '__main__':
#    window()


from PyQt5 import QtWidgets, uic
 
import sys
 
app = QtWidgets.QApplication([])
 
win = uic.loadUi("mydesign.ui") #specify the location of your .ui file
 
win.show()
 
sys.exit(app.exec())