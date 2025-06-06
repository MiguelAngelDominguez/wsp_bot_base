import pandas as pd
import modules.Table as tb

class csvReader:
    def __init__(self, path_file):
        self.path_file = path_file
        self.data = pd.read_csv(self.path_file, encoding='latin1', delimiter=';')
        self.data_array = self.data.values.tolist()
    
    def getData(self):
        return self.data_array
    
    def getDatainRange(self, start=0, end=0):
        if end == 0:
            end = len(self.data_array)
        return self.data_array[start:end]

    def printData(self):
        new_array = self.data_array
        new_array.insert(0, ['Numeros'])
        tb.printTabla(new_array)
    
    def printDatainRange(self, start = 0, end = 0):
        new_array = self.getDatainRange(start, end)
        new_array.insert(0, ['Numeros'])
        tb.printTabla(new_array)