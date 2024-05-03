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
    """
    Model for **data information** tab.
    Hold the data and return the summary statistics
    """
    def __init__(self):
        self.data = DataLoader()

    def correlations(self):
        """for calculating the correlations between the attributes"""
        return self.data.corr()

    def summary_statistics(self):
        """returns summary statistics for the data"""
        return self.data.load_data.describe()

    def calculate_correlations(self):
        """returns correlation values for the data"""
        correlations = self.data.load_data.corr()
        return correlations

    def filter_data(self, filters):
        """filters the data based on the given criteria"""
        filtered_data = self.data.load_data.copy()
        for column, value in filters.items():
            filtered_data = filtered_data[filtered_data[column] == value]
        return filtered_data


class Statistics:
    """
    Model for **statistics** tab. Calculate statistics including bar chart,
    histogram and correlation for the data.
    """
    def __init__(self):
        self.data = DataLoader()

    def plot_bar_chart(self, attribute):
        """for plotting a bar chart for the given attribute"""
        df = self.data.load_data
        plt.figure(figsize=(6, 4))
        sns.countplot(data=df, x=attribute)
        plt.title(f"Bar Chart for {attribute}")
        plt.show()

    def plot_histogram(self, attribute):
        """for plotting a histogram for the given attribute"""
        df = self.data.load_data
        plt.figure(figsize=(6, 4))
        sns.histplot(data=df, x=attribute, kde=True)
        plt.title(f"Histogram for {attribute}")
        plt.show()

    def plot_correlation(self, attribute1, attribute2):
        """for plotting a correlation between two attributes"""
        df = self.data.load_data
        sns.pairplot(df[[attribute1, attribute2]])
        plt.title(f"Correlation between {attribute1} and {attribute2}")
        plt.show()
