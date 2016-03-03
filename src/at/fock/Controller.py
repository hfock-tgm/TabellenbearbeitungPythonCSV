import sys

from PySide import QtGui
from PySide.QtGui import *

import CSVReader
import View




class Controller(QMainWindow):
    '''
    Konstruktor
    '''
    def __init__(self, parent=None):
        super(Controller,self).__init__(parent)

        self.view = View.View()
        self.view.setupUi(self)
        self.csv = CSVReader.CSVReader()

        self.values = []
        self.header = ""

        self.view.actionOpen.triggered.connect(self.openFile)
        self.view.actionAdd_row.triggered.connect(self.addRow)
        self.view.actionSave.triggered.connect(self.saveFile)

    '''
    Initialisiert den CSVReader = Model
    '''
    def initCSVReader(self,path):
        self.csv.setFilePath(path)
        self.csv.load()
        self.header = self.csv.values[0][:-1]

    '''
    Initialisiert die Tabelle
    '''
    def initTable(self):
        self.view.tableWidget.setRowCount(self.csv.row-1)
        self.view.tableWidget.setColumnCount(self.csv.column)

    '''
    Befuellt die Tabelle mit den Werten des CSV Files
    '''
    def fillTable(self):
        self.view.tableWidget.setHorizontalHeaderLabels(self.header)

        for i in range(1,self.csv.row):
            for j in range(self.csv.column):
                item = QtGui.QTableWidgetItem(str(self.csv.values[i][j]))
                self.view.tableWidget.setItem(i-1, j, item)

    '''
    Liest die einzelnene Values aus der Tabelle aus
    '''
    def readTable(self):
        values = []
        values.append(self.header)
        for i in range(self.view.tableWidget.rowCount()):
            row = []
            for j in range(self.view.tableWidget.columnCount()):
                row.append(self.view.tableWidget.item(i,j).text().encode('ascii', 'ignore'))
            values.append(row)
        return values

    '''
    Oeffnet das CSV File
    '''
    def openFile(self):
        path = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '', 'CSV(*.csv)')
        self.initCSVReader(path[0])
        self.initTable()
        self.fillTable()
        self.view.statusbar.showMessage('Opened new file!')

    '''
    Fuegt eine neue Zeile bei der Tabelle hinzu
    '''
    def addRow(self):
        rowPosition = self.view.tableWidget.rowCount()
        self.view.tableWidget.insertRow(rowPosition)
        self.view.statusbar.showMessage('Added new row!')

    '''
    Speichert die geaenderten Daten
    '''
    def saveFile(self):
        self.csv.save(self.readTable())
        self.view.statusbar.showMessage('Saved changes!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show()
    sys.exit(app.exec_())