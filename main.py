# This Python file uses the following encoding: utf-8
import os
import sys
import configparser
import time

from PySide2 import QtCore
from PySide2.QtWidgets import QApplication, QWidget

from serial import Serial         # pip3 install pyserial
from serial.tools import list_ports
from ui_mainform import Ui_MainForm
import re


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        portsStr = list()
        for port, desc, hwid in list_ports.comports():
            portsStr.append(port)

        self.ui.comboBox_com.addItems(portsStr)

        self.ser = Serial()

        self.initSetting()

    def initSetting(self):
        if not os.path.exists('setting.ini'):
            open('setting.ini', 'w')
        self.conf = configparser.ConfigParser()
        self.conf.read('setting.ini')

        if not self.conf.has_section('serial'):
            self.conf.add_section('serial')
            self.conf.set('serial', 'port',     'COM0')
            self.conf.set('serial', 'baudrate', '115200')
        self.ui.comboBox_com.setCurrentIndex(self.ui.comboBox_com.findText(self.conf.get('serial', 'port'), QtCore.Qt.MatchExactly))

    @QtCore.Slot()
    def closeEvent(self, event):
        self.ser.close()
        self.conf.set('serial', 'port',     self.ui.comboBox_com.currentText())
        self.conf.set('serial', 'baudrate', "115200")
        self.conf.write(open('setting.ini', 'w'))

    @QtCore.Slot()
    def on_pushButton_open_clicked(self):
        if not self.ser.is_open:
            try:
                self.ser = Serial(self.ui.comboBox_com.currentText(), 115200)
            except Exception as e:
                print(e)
                self.ui.label_tip.setText(self.tr('打开串口出错:\n %s' % (e)))
            else:
                self.ui.pushButton_open.setText(self.tr('关闭串口'))
                self.ui.label_tip.clear()
        else:
            self.ser.close()
            self.ui.label_tip.clear()
            self.ui.pushButton_open.setText(self.tr('打开串口'))

    @QtCore.Slot()
    def on_pushButton_read_clicked(self):
        self.ui.label_mac.setText("???")
        self.ui.label_no.setText("???")
        self.ui.label_type.setText("???")
        if self.ser.is_open:
            while self.ser.in_waiting != 0:
                self.ser.read(self.ser.in_waiting)
            self.ser.write(b"\nastparam dump\n")
            time.sleep(0.1)

            while self.ser.in_waiting > 4:
                line = self.ser.readline().decode("latin")
                if "ethaddr" in line:
                    self.ui.label_mac.setText(line.split("=")[1].strip())
                if "serial_no" in line:
                    self.ui.label_no.setText(line.split("=")[1].strip())
                if "model_version" in line:
                    self.ui.label_type.setText(line.split("=")[1].strip())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
