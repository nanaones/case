import pandas as pd
import sqlalchemy

class StoreCSV:
    def __init__(self):
        self.csv_path = '../Raw/wanted_temp_data.csv'
        self.read_data = pd.read_csv(self.csv_path, sep=',')
        print(self.read_data["company_ko"])
