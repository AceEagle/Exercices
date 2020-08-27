import random
from random import randint
import numpy as np
from pyqtgraph import PlotWidget, plot, QtCore
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import sys
import os


# class MainWindow(QtWidgets.QMainWindow):
#
#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#
#         self.graphWidget = pg.PlotWidget()
#         self.setCentralWidget(self.graphWidget)
#
#         hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
#         temperature_2 = [34, 36, 38, 45, 29, 30, 31, 29, 28, 26]
#
#         self.graphWidget.setBackground('w')
#         #b is blue, g is green, r is red, c is cyan, m is magenta, y is yellow, k is black, w is white, or anything with hex notation, RBG\RGBA values, or QColor types
#         self.graphWidget.setTitle("THE TITLE", color="b", size="30pt")
#         #modify the title, color and size
#         styles = {'color':'#f00', 'font-size':'20px'}
#         #pour les captions des axes
#         self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
#         #captions axes
#         self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)
#         #captions axes
#         self.graphWidget.addLegend()
#         #to add a legend
#         self.graphWidget.showGrid(x=True, y=True)
#         #to show the grid or not
#         #self.graphWidget.setXRange(5, 20, padding=0)
#         #add the initial axis x limit
#         #self.graphWidget.setYRange(30, 40, padding=0)
#         #add the initial y limit
#
#         #self.graphWidget.clear() if u want to clear the plots
#
#         self.plot(hour, temperature_1, "Sensor1", 'r') #add a new plot for each plot u want
#         self.plot(hour, temperature_2, "Sensor2", 'b')
#
#     def plot(self, x, y, plotname, color): #the function is to have more than 1 plot
#         pen = pg.mkPen(color=color)
#         # pen is the color, the size (width=15) and the style of the line(style=QtCore.Qt.Dashline) (https://doc.qt.io/qt-5/qpen.html#pen-style)
#         self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))
#         # name is for the legend, you can place pen=pen or/and symbol='o, s, t, d or +' if you want line or symbols, for symbols: symbolSize=nb et symbolBrush=('b')
#
#
# def main():
#     app = QtWidgets.QApplication(sys.argv)
#     main = MainWindow()
#     main.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()



class MainWindow(QtWidgets.QMainWindow): #second exemple if u want to clear and update for animated graph

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature_1 = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        temperature_2 = [34, 36, 38, 45, 29, 30, 31, 29, 28, 26]

        self.x = list(range(100)) #100 time point
        self.y = [randint(0,100) for _ in range(100)] #100 data point

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(250, 0, 0))
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)

        self.timer = QtCore.QTimer() #create a timer
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):

        self.x = self.x[1:] #remove the first element
        self.x.append(self.x[-1] + 1) #add a new value 1  higher than the last

        self.y = self.y[1:] #remove the first element
        self.y.append(randint(0, 100)) #add a random value

        self.data_line.setData(self.x, self.y) #the line who update it


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())

