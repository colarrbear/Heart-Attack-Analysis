import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from model import HeartDiseaseModel

# pd.read_csv('heart.csv')
# print([i for i in data.columns])

# Load the data
# heart_disease_model = HeartDiseaseModel()
# data = heart_disease_model.data


# def show_data_information(data):
#     """Show the data information."""
#     print("Data Information")
#     print(data.info())
#     print("\n")
#
#
# show_data_information(data)

# def plot_correlation_heatmap(data):
    # # Calculate correlations
    # correlations = data.corr()
    #
    # # Create a heatmap of the correlations
    # plt.figure(figsize=(10, 8))
    # sns.heatmap(correlations, annot=True, cmap="coolwarm")
    # plt.title("Correlation Heatmap")
    # plt.show()


# plot_correlation_heatmap(data)

class DataAnalyze:
    """Class for analyzing data."""

    def __init__(self):
        self.data = pd.read_csv('heart.csv')

    def get_column_names(self):
        """Return the column names."""
        return self.data.columns.tolist()


# class DataInfomationWorker:
#     """Class for showing in Data Information tab."""

    def summary_statistics(self, column):
        """Return the summary statistics."""
        return self.data[column].describe()

        # if choice == 'mean':
        #     return df[column].mean()
        # elif choice == 'median':
        #     return df[column].median()
        # elif choice == 'mode':
        #     return df[column].mode()
        # elif choice == 'std':
        #     return df[column].std()
        # elif choice == 'min':
        #     return df[column].min()
        # elif choice == 'max':
        #     return df[column].max()
        # elif choice == 'count':
        #     return df[column].count()
        # elif choice == 'unique':
        #     return df[column].unique()
        # elif choice == 'nunique':
        #     return df[column].nunique()
        # else:
        #     return 'Invalid choice'

    def correlations(self, df):
        """Return the correlations."""
        return df.corr()
