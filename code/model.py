"""Model class for holds the data and calculations.
**This should be model of data structure.**"""

import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')


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

    # @classmethod
    # def load_data(cls):
    #     """for loading the data from a CSV file"""
    #     return cls._instance

    @property
    def get_column_names(self):
        """Return the column names."""
        return self.data.columns.tolist()

    def get_column_data(self, column):
        """Return the data for the given column."""
        return self.data[column]

    def filter_data(self, filters):
        """filters the data based on the given criteria"""
        filtered_data = self.data.load_data.copy()
        for column, value in filters.items():
            filtered_data = filtered_data[filtered_data[column] == value]
        return filtered_data


class PlotGraphs:
    """
    Model for tabs.
    Hold the data and return the calculated requested data.
    """
    def __init__(self, input_data):
        self.data = input_data

    def summary_statistics(self):
        """returns summary statistics for the data"""
        return self.data.load_data.describe()

    def calculate_correlations(self):
        """returns correlation values for the data"""
        correlations = self.data.load_data.corr()
        return correlations

    def plot_bar_chart(self, attb1, attb2, parent_frame) -> tk.Widget:
        """for plotting a bar chart for the given attribute"""
        if attb1 == 'sex' and attb2 == '':  # nominal
            df = self.data.load_data
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.countplot(data=df, x=attb1, hue=attb1)
            plt.title(f"Bar Chart for {attb1}")
            # Embed the plot into the tkinter frame
            canvas = FigureCanvasTkAgg(fig, master=parent_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.BOTTOM)
            return canvas.get_tk_widget()
        else:
            df = self.data.load_data
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.barplot(data=df, x=attb1, y=attb2)
            plt.title(f"Bar Chart for {attb1} and {attb2}")
            # Embed the plot into the tkinter frame
            canvas = FigureCanvasTkAgg(fig, master=parent_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.BOTTOM)
            return canvas.get_tk_widget()

    def plot_histogram(self, attribute, parent_frame) -> tk.Widget:
        """for plotting a histogram for the given attribute"""
        df = self.data.load_data
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(data=df, x=attribute, kde=True, ax=ax)
        plt.title(f"Histogram for {attribute}")
        # Embed the plot into the tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM)

        return canvas.get_tk_widget()

    def plot_correlation(self, parent_frame):
        """for plotting a correlation between two attributes"""

        # Selecting only the specified attributes for correlation calculation
        selected_attributes = ["age", "trtbps", "chol", "thalachh"]
        df_corr = self.data.load_data[selected_attributes].corr()

        # Plot the correlation matrix
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.heatmap(df_corr, annot=True, cmap="coolwarm", ax=ax)

        plt.title(f"Correlation of age, trtbps, chol, thalachh")
        # Embed the plot into the tkinter frame
        canvas = FigureCanvasTkAgg(plt.gcf(), master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM)

        return canvas.get_tk_widget()
