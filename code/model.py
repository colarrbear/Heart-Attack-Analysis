"""Model class for holds the data and calculations"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class DataLoader:
    """Class for load data."""
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.data = pd.read_csv('heart.csv')
        return cls._instance
    # def __init__(self):
    #     self.data = pd.read_csv('heart.csv')

    @property
    def load_data(self):
        """for loading the data from a CSV file"""
        return self.data

    @property
    def get_column_names(self):
        """Return the column names."""
        return self.data.columns.tolist()

    def get_column_data(self, column):
        """Return the data for the given column."""
        return self.data[column]


class HDInformation:
    """hold the data and return the summary statistics"""
    def __init__(self):
        self.data = DataLoader()

    def correlations(self):
        """for calculating the correlations between the attributes"""
        return self.data.corr()

    def summary_statistics(self):
        """returns summary statistics for the data"""
        # return self.data.describe()
        return self.data.load_data.describe()
        # return summary_stats.to_string()

    def calculate_correlations(self):
        """returns correlation values for the data"""
        correlations = self.data.corr()
        return correlations
        # return correlations.to_string()

    def filter_data(self, filters):
        """filters the data based on the given criteria"""
        filtered_data = self.data.copy()
        for column, value in filters.items():
            filtered_data = filtered_data[filtered_data[column] == value]
        return filtered_data
