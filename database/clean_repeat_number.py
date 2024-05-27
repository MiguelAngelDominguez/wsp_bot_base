import os
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

def main():
    for nmr in range(1, 9):
        numeros_1 = csvReader(f'./database/SMS{nmr}.csv')
        numeros_1.printDatainRange(0, 10)
        
        array_numeros_1 = numeros_1.getData()
        
        numbers_repeat = []
        for csltNumber in array_numeros_1:
            repeat = 0
            for number in array_numeros_1:
                if csltNumber == number:
                    repeat += 1
                if repeat > 1:
                    numbers_repeat.append(csltNumber)
                    break
                
        os.system("pause")
        os.system("cls")
        print(f"Numeros que se repiten en el archivo SMS{nmr}.csv:")
        print(numbers_repeat)
        log_file = open(f"./database/log_sms{nmr}.log", "w")
        log_file.write(str(numbers_repeat))

