import pandas as pd
import datetime

class Housing:
    def __init__(self, data):
        self.data = pd.read_csv(data, low_memory = False)
        self.timestamp = datetime.datetime.now()
    
    def get_data(self):
        return self.data

    def get_last_update(self):
        return self.timestamp