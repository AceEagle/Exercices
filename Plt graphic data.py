import random
import numpy as np
from pyqtgraph import PlotWidget, plot, QtCore
from PyQt5 import QtWidgets
import pyqtgraph as pg
import sys
import os


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.DashLine)  # pen is the color, the size and the style of the line (https://doc.qt.io/qt-5/qpen.html#pen-style)
        self.graphWidget.plot(hour, temperature,name="Sensor1", pen=pen, symbol='+', symbolSize=30, symbolBrush=('b')) # name is for the legend, you can place pen=pen or/and symbol='o, s, t, d or +' if you want line or symbols, for symbols: symbolSize=nb et symbolBrush=('b')
        self.graphWidget.setBackground('w') #b is blue, g is green, r is red, c is cyan, m is magenta, y is yellow, k is black, w is white, or anything with hex notation, RBG\RGBA values, or QColor types
        self.graphWidget.setTitle("THE TITLE", color="b", size="30pt")#modify the title, color and size
        styles = {'color':'r', 'font-size':'20px'} #pour les captions des axes
        self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)#captions axes
        self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)#captions axes
        self.graphWidget.addLegend()#to add a legend
        self.graphWidget.showGrid(x=True, y=True)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main= MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

