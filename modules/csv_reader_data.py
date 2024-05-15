import pandas as pd
import modules.Table as tb

class csvReader:
    def __init__(self, path_file):
        self.path_file = path_file
        self.data = pd.read_csv(self.path_file, encoding='latin1', delimiter=';')
        self.data.insert(0, 'ID', range(0, len(self.data)))
        self.data_array = self.data.values.tolist()
    
    def getData(self):
        return self.data_array
    
    def getDatainRange(self, start, end):
        return self.data_array[start:end]

    def printData(self):
        new_array = self.data_array
        new_array.insert(0, ['iD','Nombre', 'Cell 1', 'Cell 2'])
        tb.printTabla(new_array)