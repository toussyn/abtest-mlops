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

    def find_aggregate(self, stat_list: list):
        '''
            Returns the aggregate of the passed Dataframe
        '''
        try:
            return self.df.agg(stat_list)
        except:
            print("Failed to get aggregates")

    def find_unique_value_count(self):
        """
            Returns the unique value count of the passed dataframe
        """
        return pd.DataFrame(self.df.apply(lambda x: len(x.value_counts(dropna=False)), axis=0), columns=['Unique Value Count']).sort_values(by='Unique Value Count', ascending=True)

    def find_duplicates(self):
        """
            Returns the duplicates of the passed dataframe
        """
        if self.df[self.df.duplicated()].count == 0:
            print(f"There are {self.df[self.df.duplicated()].count} duplicated values")
        else:
            return self.df[self.df.duplicated()]

    def find_columns_missing_percentage(self, df):
        """
        Returns the missing percentage of the passed Dataframe
        """
        col_null = self.df.isnull().sum()
        total_entries = self.df.shape[0]
        missing_percentage = []
        for col_missing_entries in col_null:
            value = str(
                round(((col_missing_entries/total_entries) * 100), 2)) + " %"
            missing_percentage.append(value)

        missing_df = pd.DataFrame(col_null, columns=['total_missing_values'])
        missing_df['missing_percentage'] = missing_percentage
        return missing_df

    def find_columns_missing_percentage_greater_than(self, num: float):
        '''
            Returns the missing percentage of the passed Dataframe
        '''
        all_cols = self.get_column_based_missing_percentage()
        extracted = all_cols['missing_percentage'].str.extract(r'(.+)%')
        return extracted[extracted[0].apply(lambda x: float(x) >= num)].index

    def find_columns_with_missing_values(self):
        '''
            Returns the missing vlaue of the passed Dataframe
        '''
        lst = self.df.isnull().any()
        arr = []
        index = 0
        for col in lst:
            if col == True:
                arr.append(lst.index[index])
            index += 1
        return arr

    def find_column_based_missing_values(self):
        '''
            Returns the missing value of the passed dataframe
        '''
        value = self.df.isnull().sum()
        df = pd.DataFrame(value, columns=['missing_count'])
        df.drop(df[df['missing_count'] == 0].index, inplace=True)
        df['type'] = [self.df.dtypes.loc[i] for i in df.index]
        return df

    
# Class for handling all the methods for data preprocessing
class data_preprocessing:

    def __init__(self, df: pd.DataFrame) -> None:
        """
            Returns a data_preprocessing object of the passed dataframe
        """
        self.df = df

    def remove_duplicates(self) -> pd.DataFrame:
        """
            Returns a dataframe where duplicate rows are removed
        """
        removables = self.df[self.df.duplicated()].index
        return self.df.drop(index=removables, inplace=True)

    def fix_outlier(self, column: str) -> pd.DataFrame:
        """
            Returns a dataframe where outliers of the specified columns is fixed
        """
        self.df[column] = np.where(self.df[column] > self.df[column].quantile(
            0.95), self.df[column].median(), self.df[column])

        return self.df

    def fix_outlier_columns(self, columns: list) -> pd.DataFrame:
        """
        Returns a DataFrame where outlier of the specified column is fixed
        """
        try:
            for column in columns:
                self.df[column] = np.where(self.df[column] > self.df[column].quantile(
                    0.95), self.df[column].median(), self.df[column])
        except:
            print("Cant fix outliers for each column")

        return self.df

    def remove_unwanted_columns(self, columns: list) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns in the list are removed
        """
        self.df.drop(columns, axis=1, inplace=True)
        return self.df

    def change_columns_type_to(self, cols: list, data_type: str) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns data types are changed to the specified data type
        """
        try:
            for col in cols:
                self.df[col] = self.df[col].astype(data_type)
        except:
            print('Failed to change columns type')

        return self.df

    def save_clean_data(self, name: str):
        """
        The objects dataframe gets saved with the specified name 
        """
        try:
            self.df.to_csv(name)

        except:
            print("Failed to save data")