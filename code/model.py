"""holds the data and calculations"""

import pandas as pd


class HeartDiseaseModel:
    def __init__(self):
        self.data = None
        self.load_data()

    def load_data(self):
        self.data = pd.read_csv('heart.csv')

    # def summary_statistics(self):
    #     return self.data.describe()
    #
    # def correlations(self):
    #     return self.data.corr()

    def summary_statistics(self):
        summary_stats = self.data.describe()
        return summary_stats.to_string()

    def calculate_correlations(self):
        # Example correlations, replace with actual calculations
        correlations = self.data.corr()
        return correlations.to_string()

    def filter_data(self, filters):
        filtered_data = self.data.copy()
        for column, value in filters.items():
            filtered_data = filtered_data[filtered_data[column] == value]
        return filtered_data
