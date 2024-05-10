"""Model class for holds the data and calculations.
**This should be model of data structure.**"""

from tkinter import messagebox

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
import seaborn as sns
import pandas as pd

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

    @property
    def get_column_names(self):
        """Return the column names."""
        return self.data.columns.tolist()


class PlotGraphs:
    """
    Model for tabs.
    Hold the data and return the calculated requested data.
    """

    def __init__(self, input_data):
        self.data = input_data

    def get_max_value(self, attribute):
        """returns the maximum value for the given attribute"""
        return self.data.load_data[attribute].max()

    def summary_statistics(self):
        """returns summary statistics for the data"""
        # return self.data.load_data.describe()
        nominal_attributes = ["sex", "fbs", "output"]
        ordinal_attributes = ["cp", "restecg", "exng", "slp"]
        numerical_attributes = ["age", "trtbps", "chol", "thalachh", "oldpeak",
                                "caa", "thall"]

        data_description = self.data.load_data.describe()

        custom_summary = {}
        for attribute in data_description.columns:
            attribute_data = data_description[attribute]

            # Determine attribute type
            if attribute in nominal_attributes:
                mode_value = attribute_data.mode()[0]
                custom_summary[attribute] = {"Mode": mode_value}
            elif attribute in ordinal_attributes:
                median_value = attribute_data.median()
                data_range = attribute_data.max() - attribute_data.min()
                quartiles = attribute_data.quantile([0.25, 0.75])
                iqr_value = quartiles[0.75] - quartiles[0.25]
                custom_summary[attribute] = {
                    "Median": median_value,
                    "Range": data_range,
                    "Interquartile Range (IQR)": iqr_value
                }
            # elif attribute in numerical_attributes:
            #     mean_value = attribute_data.mean()
            #     median_value = attribute_data.median()
            #     std_deviation = attribute_data.std()
            #     variance = attribute_data.var()
            #     data_range = attribute_data.max() - attribute_data.min()
            #     quartiles = attribute_data.quantile([0.25, 0.75])
            #     iqr_value = quartiles[0.75] - quartiles[0.25]
            #     custom_summary[attribute] = {
            #         "Mean": mean_value,
            #         "Median": median_value,
            #         "Standard Deviation": std_deviation,
            #         "Variance": variance,
            #         "Range": data_range,
            #         "Interquartile Range (IQR)": iqr_value
            #     }
            elif attribute in numerical_attributes:
                quartiles = attribute_data.quantile([0.25, 0.75])
                custom_summary[attribute] = {
                    "Mean": attribute_data.mean(),
                    "Median": attribute_data.median(),
                    "Standard Deviation": attribute_data.std(),
                    "Variance": attribute_data.var(),
                    "Range": attribute_data.max() - attribute_data.min(),
                    "Interquartile Range (IQR)": quartiles[0.75] - quartiles[0.25]
                }

        return custom_summary

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
            canvas.get_tk_widget().pack(side="bottom")
            return canvas.get_tk_widget()
        else:
            df = self.data.load_data
            if not attb1:
                messagebox.showerror("Error",
                                     "Select an attribute for the left combobox.")
                return
            elif not attb2:
                messagebox.showerror("Error",
                                     "Select an attribute for the right combobox.")
                return

            fig, ax = plt.subplots(figsize=(6, 4))
            if attb1 == 'sex':
                sns.barplot(data=df, x=attb1, y=attb2, hue=attb1)
            elif attb2 == 'sex':
                sns.barplot(data=df, x=attb2, y=attb1, hue=attb2)
            else:
                sns.barplot(data=df, x=attb1, y=attb2)
            plt.title(f"Bar Chart for {attb1} and {attb2}")
            # Embed the plot into the tkinter frame
            canvas = FigureCanvasTkAgg(fig, master=parent_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side="bottom")
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
        canvas.get_tk_widget().pack(side="bottom")

        return canvas.get_tk_widget()

    def plot_correlation(self, parent_frame):
        """for plotting a correlation between two attributes"""

        # Selecting only the specified attributes for correlation calculation
        selected_attributes = ["chol", "exng", "trtbps", "thalachh", "caa", "age", "sex", "output"]

        df_corr = self.data.load_data[selected_attributes].corr()

        # Plot the correlation matrix
        fig, ax = plt.subplots(figsize=(7, 4.5))
        sns.heatmap(df_corr, annot=True, cmap="coolwarm", ax=ax)

        plt.title("Correlation of chol, exng, trtbps, thalachh, caa, age, sex, output")
        # Embed the plot into the tkinter frame
        canvas = FigureCanvasTkAgg(plt.gcf(), master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM)

        return canvas.get_tk_widget()

    def plot_distribution(self, attb1, attb2, range_attb1, range_attb2,
                          parent_frame) -> tk.Widget:
        """Plot a distribution plot for the given attributes within the specified ranges."""
        df = self.data.load_data
        if not attb1:
            messagebox.showerror("Error",
                                 "Select an attribute for the left combobox.")
            return
        elif not attb2:
            messagebox.showerror("Error",
                                 "Select an attribute for the right combobox.")
            return

        if range_attb1 and range_attb2:
            # Filter data based on specified ranges
            filtered_df = df[
                (df[attb1] <= range_attb1) & (df[attb2] <= range_attb2)]

            # Determine the maximum range value for the x-axis
            max_range_value = max(range_attb1, range_attb2)
        elif range_attb1:
            filtered_df = df[df[attb1] <= range_attb1]
            max_range_value = range_attb1
        elif range_attb2:
            filtered_df = df[df[attb2] <= range_attb2]
            max_range_value = range_attb2
        else:
            # If no range is specified, use the entire DataFrame
            filtered_df = df
            max_range_value = None

        fig, ax = plt.subplots(figsize=(6, 4))

        # Plot distribution of attribute 1
        sns.kdeplot(data=filtered_df[attb1], fill=True, color="#5A60A5",
                    label=f"{attb1}", ax=ax)

        # Plot distribution of attribute 2
        sns.kdeplot(data=filtered_df[attb2], fill=True, color="#F27A79",
                    label=f"{attb2}", ax=ax)

        plt.title(f"Distribution Plot for {attb1} and {attb2}")
        plt.xlabel("Attribute Values")
        plt.ylabel("Density")
        plt.legend()

        # Set maximum value for x-axis
        if max_range_value is not None:
            plt.xlim(right=max_range_value)

        # Embed the plot into the tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="bottom")
        return canvas.get_tk_widget()

    def plot_scatter(self, attb1, attb2, range_attb1, range_attb2,
                     parent_frame) -> tk.Widget:
        """Plot a scatter plot for the given attributes within the specified ranges."""

        df = self.data.load_data
        if not attb1:
            messagebox.showerror("Error",
                                 "Select an attribute for the left combobox.")
            return
        elif not attb2:
            messagebox.showerror("Error",
                                 "Select an attribute for the right combobox.")
            return

        if range_attb1 and range_attb2:
            # Filter data based on specified ranges
            filtered_df = df[
                (df[attb1] <= range_attb1) & (df[attb2] <= range_attb2)]
            # Determine the maximum range value for the x-axis
            max_range_value = max(range_attb1, range_attb2)
        elif range_attb1:
            filtered_df = df[df[attb1] <= range_attb1]
            max_range_value = range_attb1
        elif range_attb2:
            filtered_df = df[df[attb2] <= range_attb2]
            max_range_value = range_attb2
        else:
            # If no range is specified, use the entire DataFrame
            filtered_df = df
            max_range_value = None

        fig, ax = plt.subplots(figsize=(6, 4))

        # Plot scatter plot of the two attributes
        sns.scatterplot(data=filtered_df, x=attb1, y=attb2, ax=ax)

        correlation_coefficient = np.corrcoef(filtered_df[attb1], filtered_df[attb2])[0, 1]

        # Add coefficient to the plot title
        plt.title(
            f"Scatter Plot for {attb1} and {attb2} (Correlation: {correlation_coefficient:.2f})")
        plt.xlabel(attb1)
        plt.ylabel(attb2)

        # Set maximum value for x-axis
        if max_range_value is not None:
            plt.xlim(right=max_range_value)

        # Embed the plot into the tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="bottom")
        return canvas.get_tk_widget()

    def plot_stack_bar_graph(self, attb1, attb2, parent_frame) -> tk.Widget:
        """for plotting possibility of heart attack based on age and sex"""

        if not attb1:
            messagebox.showerror("Error",
                                 "Select an attribute for the left combobox.")
            return
        elif not attb2:
            messagebox.showerror("Error",
                                 "Select an attribute for the right combobox.")
            return

        sns.set_theme()  # Set seaborn style
        df = self.data.load_data

        # Group data by 'attb1' and 'attb2' and calculate the count of occurrences
        grouped_data = df.groupby([attb1, attb2]).size().unstack()

        # Plot stacked bar graph
        ax = grouped_data.plot(kind='bar', stacked=True, figsize=(8, 5))

        # Set labels and title
        plt.title(f"Stacked Bar Graph for {attb1} and {attb2}")
        plt.xlabel(attb1)
        plt.ylabel("Count")
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

        plt.show()
