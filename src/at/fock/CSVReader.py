import csv

class CSVReader(object):
    '''
    Konstruktor
    '''
    def __init__(self):
        self.filename = 'file.csv'
        self.row = 0
        self.column = 0
        self.values = []

    '''
    Liest das CSV-File aus
    '''
    def load(self):
        self.values = []
        self.row = 0
        self.column = 0
        with open(self.filename, 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                self.values.append(row)
                self.row += 1
                self.column = len(row)-1

    '''
    Speichert die Aenderungen ins CSV File
    '''
    def save(self,values):
        with open(self.filename, 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL,lineterminator=";\n")
            for zeile in values:
                spamwriter.writerow(zeile)

    def setFilePath(self,filepath):
        self.filename = '' + filepath