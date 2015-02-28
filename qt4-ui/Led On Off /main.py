from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
from led_on_off import Ui_Form
import serial
import commands
class LED_ON_OFF(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		command = 'ls /dev/ttyACM*'
		self.dev = " "
		result = commands.getstatusoutput(command)
		if result[0]==0:
			self.dev = result[1]
			
		else :
			self.dev = "/dev/ttyUSB0"
		print self.dev
		self.ser_obj = serial.Serial(self.dev, 38400, stopbits=1, timeout = 1.0)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		####
		self.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.on_led)
		self.connect(self.ui.pushButton_2,QtCore.SIGNAL('clicked()'),self.led_off)
		####
		self.show()
	def on_led(self):
		self.ser_obj.write("1")
	def led_off(self):
		self.ser_obj.write("0")
		
if __name__ == "__main__":
	
	app_obj = QtGui.QApplication(sys.argv)
	main_win = LED_ON_OFF()
	sys.exit(app_obj.exec_())
