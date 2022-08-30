import pandas as pd
import numpy as np

# class for data information
class dataInfo:
    
    def __init__(self, df: pd.DataFrame):
        """
            Returns a dataframe Info Object
        """
        self.df = df

    def get_info(self):
        """
            Returns the info of the dataframe read into it
        """
        return self.df.info()

    def get_shape(self):
        """
            Returns the shape of the data frame read into it
        """
        return self.df.shape()


