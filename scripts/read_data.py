import json
import pandas as pd


class ReadData:

    def init():
        pass
    def read_json(self,json_file: str, dfExctractor)->pd.DataFrame:

        data = []
        for item in open(json_file,'r'):
            data.append(json.loads(item))
        return dfExtractor(data)
    
    def read_csv(self, csv_file):
        data = pd.read_csv(csv_file)
        return data
    
    def read_excel(self,excel_file, startRow=0)->pd.DataFrame:
        data = pd.read_excel(excel_file)
        return data
    