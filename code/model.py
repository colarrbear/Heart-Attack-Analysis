"""holds the data and calculations"""

import pandas as pd


class HeartDiseaseModel:
    def __init__(self):
        self.data = None
        self.load_data()

    def load_data(self):
        self.data = pd.read_csv('heart.csv')

    def summary_statistics(self):
        return self.data.describe()

    def correlations(self):
        return self.data.corr()

    def filter_data(self, filters):
        filtered_data = self.data.copy()
        for column, value in filters.items():
            filtered_data = filtered_data[filtered_data[column] == value]
        return filtered_data
