"""Model class for holds the data and calculations.
**This should be model of data structure.**"""

import matplotlib
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import seaborn as sns
import pandas as pd
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

    def get_data_types(self):
        """returns the data types of the columns"""
        return self.data.dtypes

    @staticmethod
    def get_data_categories(atb):
        """return types: nominal, ordinal, numerical
        - nominal are sex, fbs
        - ordinal are cp, restecg, exng, slp
        - numerical are age, trtbps, chol, thalachh, oldpeak, caa, thall"""
        nominal_attributes = ["sex", "fbs"]
        ordinal_attributes = ["cp", "restecg", "exng", "slp"]
        numerical_attributes = ["age", "trtbps", "chol", "thalachh", "oldpeak",
                                "caa", "thall"]

        if atb in nominal_attributes:
            return "nominal"
        elif atb in ordinal_attributes:
            return "ordinal"
        elif atb in numerical_attributes:
            return "numerical"
        else:
            return None  # Unknown type or attribute not found


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
            elif attribute in numerical_attributes:
                mean_value = attribute_data.mean()
                median_value = attribute_data.median()
                std_deviation = attribute_data.std()
                variance = attribute_data.var()
                data_range = attribute_data.max() - attribute_data.min()
                quartiles = attribute_data.quantile([0.25, 0.75])
                iqr_value = quartiles[0.75] - quartiles[0.25]
                custom_summary[attribute] = {
                    "Mean": mean_value,
                    "Median": median_value,
                    "Standard Deviation": std_deviation,
                    "Variance": variance,
                    "Range": data_range,
                    "Interquartile Range (IQR)": iqr_value
                }

        return custom_summary

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

    def plot_distribution(self, attb1, attb2, range_attb1, range_attb2,
                          parent_frame) -> tk.Widget:
        """Plot a distribution plot for the given attributes within the specified ranges."""
        df = self.data.load_data

        if attb1 is None or attb2 == None:
            # Filter data based on specified ranges
            filtered_df = df[
                (df[attb1] >= range_attb1[0]) & (df[attb1] <= range_attb1[1]) &
                (df[attb2] >= range_attb2[0]) & (df[attb2] <= range_attb2[1])]

            fig, ax = plt.subplots(figsize=(6, 4))

            # Plot distribution of attribute 1
            sns.kdeplot(data=filtered_df[attb1], shade=True, color="b",
                        label=f"{attb1}", ax=ax)

            # Plot distribution of attribute 2
            sns.kdeplot(data=filtered_df[attb2], shade=True, color="r",
                        label=f"{attb2}", ax=ax)

            plt.title(f"Distribution Plot for {attb1} and {attb2}")
            plt.xlabel("Attribute Values")
            plt.ylabel("Density")
            plt.legend()

            # Embed the plot into the tkinter frame
            canvas = FigureCanvasTkAgg(fig, master=parent_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.BOTTOM)
            return canvas.get_tk_widget()
        else:
            # plot without filtering
            fig, ax = plt.subplots(figsize=(6, 4))

            # Plot distribution of attribute 1
            sns.kdeplot(data=df[attb1], shade=True, color="#5A60A5",
                        label=f"{attb1}", ax=ax)

            # Plot distribution of attribute 2
            sns.kdeplot(data=df[attb2], shade=True, color="#F27A79",
                        label=f"{attb2}", ax=ax)

            plt.title(f"Distribution Plot for {attb1} and {attb2}")
            plt.xlabel("Attribute Values")
            plt.ylabel("Density")
            plt.legend()

            # Embed the plot into the tkinter frame
            canvas = FigureCanvasTkAgg(fig, master=parent_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.BOTTOM)
            return canvas.get_tk_widget()




    # def plot_scatter(self, attb1, attb2, parent_frame) -> tk.Widget:
    #     """for plotting a scatter plot for the given attributes"""
    #     df = self.data.load_data
    #     fig, ax = plt.subplots(figsize=(6, 4))
    #     sns.scatterplot(data=df, x=attb1, y=attb2, hue='output')
    #     plt.title(f"Scatter Plot for {attb1} and {attb2}")
    #     # Embed the plot into the tkinter frame
    #     canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    #     canvas.draw()
    #     canvas.get_tk_widget().pack(side=tk.BOTTOM)
    #     return canvas.get_tk_widget()
    def plot_scatter(self, attb1, attb2, range_attb1, range_attb2,
                     parent_frame) -> tk.Widget:
        """Plot a scatter plot for the given attributes within the specified ranges."""
        df = self.data.load_data

        # Filter data based on specified ranges
        filtered_df = df[
            (df[attb1] >= range_attb1[0]) & (df[attb1] <= range_attb1[1]) &
            (df[attb2] >= range_attb2[0]) & (df[attb2] <= range_attb2[1])]

        fig, ax = plt.subplots(figsize=(6, 4))
        sns.scatterplot(data=filtered_df, x=attb1, y=attb2, hue='output')
        plt.title(f"Scatter Plot for {attb1} and {attb2}")

        # Embed the plot into the tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="bottom")
        return canvas.get_tk_widget()

    # def plot_boxplot(self, attb1, attb2, parent_frame) -> tk.Widget:
    #     """for plotting a box plot for the given attributes"""
    #     df = self.data.load_data
    #     fig, ax = plt.subplots(figsize=(6, 4))
    #     sns.boxplot(data=df, x=attb1, y=attb2)
    #     plt.title(f"Box Plot for {attb1} and {attb2}")
    #     # Embed the plot into the tkinter frame
    #     canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    #     canvas.draw()
    #     canvas.get_tk_widget().pack(side=tk.BOTTOM)
    #     return canvas.get_tk_widget()

    def plot_boxplot(self, attb1, attb2, range_attb1, range_attb2,
                     parent_frame) -> tk.Widget:
        """Plot a scatter plot for the given attributes within the specified ranges."""
        df = self.data.load_data
        # Filter data based on specified ranges
        filtered_df = df[
            (df[attb1] >= range_attb1[0]) & (df[attb1] <= range_attb1[1]) &
            (df[attb2] >= range_attb2[0]) & (df[attb2] <= range_attb2[1])]

        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(data=filtered_df, x=attb1, y=attb2)
        plt.title(f"Box Plot for {attb1} and {attb2}")

        # Embed the plot into the tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="bottom")
        return canvas.get_tk_widget()

    def plot_pie_chart(self, attb1, attb2, range_attb1, range_attb2,
                       parent_frame) -> tk.Widget:
        """for plotting a pie chart for the given attribute"""
        df = self.data.load_data

        filtered_df = df[
            (df[attb1] >= range_attb1[0]) & (df[attb1] <= range_attb1[1]) &
            (df[attb2] >= range_attb2[0]) & (df[attb2] <= range_attb2[1])]

        fig, ax = plt.subplots(figsize=(6, 4))
        filtered_df[attb1].value_counts().plot.pie(autopct='%1.1f%%')
        plt.title(f"Pie Chart for {attb1}")

        # Embed the plot into the tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="bottom")
        return canvas.get_tk_widget()
