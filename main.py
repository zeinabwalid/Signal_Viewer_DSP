from PyQt5 import QtWidgets
from last5 import Ui_SignalViewer
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from numpy import loadtxt
import biosignalsnotebooks as bsnb
#data = loadtxt("fsr.txt")
import numpy as np
import pyqtgraph as pg
import pandas as pd 
#import librosa
import wave
import math

#data2 = pd.read_csv('data.csv')
from scipy.io import wavfile
#samplerate, data1 = wavfile.read("signal.wav")


class ApplicationWindow(QtWidgets.QMainWindow):
	#data2 = pd.read_csv('data.csv')
	data3 = []
	data2= []
	data1=[]
	i1=0
	i2=0
	i3=0
	ch1=0
	ch2=0
	ch3=0
	def __init__(self):
		super(ApplicationWindow, self).__init__()
		self.ui = Ui_SignalViewer()
		self.ui.setupUi(self)
		self.data_line1 =  self.ui.win1.plotItem.plot()
		self.timer1 = QtCore.QTimer()
		self.timer1.setInterval(2)
		self.timer1.timeout.connect(self.update)
		self.timer1.start()

		

		self.data_line2 =  self.ui.win2.plotItem.plot()

		'''self.timer2 = QtCore.QTimer()
		self.timer2.setInterval(10)
		self.timer2.timeout.connect(self.update_plot_data_2)'''

		self.data_line3 =  self.ui.win3.plotItem.plot()
		'''self.timer3 = QtCore.QTimer()
		self.timer3.setInterval(1)
		self.timer3.timeout.connect(self.update_plot_data_3)'''

		self.ui.startbutton1.clicked.connect(self.start_1)
		self.ui.startbutton3.clicked.connect(self.start_3)
		self.ui.startbutton2.clicked.connect(self.start_2)


		self.ui.pausebutton1.clicked.connect(self.pause_1)
		self.ui.pausebutton2.clicked.connect(self.pause_2)
		self.ui.pausebutton3.clicked.connect(self.pause_3)

		self.ui.restartbutton1.clicked.connect(self.restart_1)
		self.ui.restartbutton2.clicked.connect(self.restart_2)
		self.ui.restartbutton3.clicked.connect(self.restart_3)

		

	def update(self):
		if(self.ch1):
			self.update_plot_data_1()
		if(self.ch2):
			self.update_plot_data_2()
		if(self.ch3):
			self.update_plot_data_3()


	def update_plot_data_1(self):
	    pen = pg.mkPen(color=(0, 200, 0))
	    #self.x1 = fs #move the first y element.
	    self.y1 = self.data1[:] # Remove the first 
	    self.data_line1.setData(self.y1,pen=pen) 
	    #self.ui.win1.setLimits(xMin= -math.inf)
	     # Update the data.

	    self.i1+=1
	def update_plot_data_2(self):
	    pen = pg.mkPen(color=(0, 0, 200))
	    #self.x2 = data[:self.i2,0] #move the first y element.
	    self.y2 = self.data2[:]  # Remove the first 
	    self.data_line2.setData(self.y2, pen=pen)  # Update the data.
	    self.i2+=1
	    

	def update_plot_data_3(self):
	    pen = pg.mkPen(color=(200, 0, 0))
	    #self.x3 = xaxis[0:self.i3] #move the first y element.
	    self.y3 = self.data3[0:]  # Remove the first 
	    self.data_line3.setData(self.y3,pen=pen)  # Update the data.
	    self.i3+=1

	def start_1(self):
	    self.ch1=1
	   # self.timer1.start()

	def start_2(self):
	    self.ch2=1
	    #self.timer2.start()

	def start_3(self):
		self.ch3=1
	    
	    #self.timer3.start()

	def pause_1(self):
	    print("stooop")
	    self.ch1=0
	    #self.timer1.stop()

	def pause_2(self):
	    print("stooop")
	    self.ch2=0
	    #self.timer2.stop()

	def pause_3(self):
	    print("stooop")
	    self.ch3=0
	    #QtGui.QApplication.processEvents()
	    #self.timer3.stop()
	    

	def restart_1(self):
	    self.i1=0

	def restart_2(self):
	    self.i2=0

	def restart_3(self):
	    self.i3=0





	def loaddata(self):
		filename = QFileDialog.getOpenFileName(self)
		if filename[0]:
			if filename[0].endswith('.txt'):
				#filename = QFileDialog.getOpenFileName()
				path3 = filename[0]
	    
				self.MyBrowse = path3
				self.storedata3(path3)

			elif filename[0].endswith('.csv'):
			#filename = QFileDialog.getOpenFileName()
				path2 = filename[0]

				self.MyBrowse = path2
				self.storedata2(path2)
			elif filename[0].endswith('.wav'):
			#filename = QFileDialog.getOpenFileName()
				path1 = filename[0]
				self.MyBrowse = path1
				self.storedata1(path1)

				
	    			



	def storedata1(self, path):
		samplerate, data1 = wavfile.read(path)
		self.data1 = data1

	
	


	def storedata2(self, path):
		
		data2 = np.genfromtxt(path , delimiter=',')
		self.data2 = data2

	

	def storedata3(self, path):
	    data3 = np.genfromtxt(path , delimiter=',')
	    self.data3 = data3

	



def main():
	app = QtWidgets.QApplication(sys.argv)
	application = ApplicationWindow()

	application.ui.actionOpenWaveFile.triggered.connect(application.loaddata)
	application.ui.actionOpenCSVFile.triggered.connect(application.loaddata)
	application.ui.actionOpentxtFile.triggered.connect(application.loaddata)
	application.show()
	app.exec_()


if __name__ == "__main__":
    main()