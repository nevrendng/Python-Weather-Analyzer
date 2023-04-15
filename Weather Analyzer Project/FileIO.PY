import numpy as np 

class FileIO:
    def __init__(self):
        self.filePath = r"\Users\JP\Documents\HelloWorldProject\Project\Weather1.csv"
        self.dataTable = self.read_weather()
       

    def read_weather(self):

        data = np.loadtxt(self.filePath, delimiter=',', skiprows=1, usecols=(0, 1, 2, 3, 4), dtype=np.float)

        return data
