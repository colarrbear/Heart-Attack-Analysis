"""holds the data and calculations"""

import pandas as pd
import tkinter as tk


class HeartDiseaseModel:
    def __init__(self):
        self.data = None
        self.load_data()

    def load_data(self):
        """for loading the data from a CSV file"""
        self.data = pd.read_csv('heart.csv')

    def correlations(self):
        return self.data.corr()

    def summary_statistics(self):
        """returns summary statistics for the data"""
        summary_stats = self.data.describe()
        return summary_stats
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

# print(pd.read_csv('heart.csv'))
