# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# from model import HeartDiseaseModel
#
# # data = pd.read_csv('heart.csv')
# # print(data)
# print(pd.read_csv('heart.csv'))
#
#
# # def display_summary_statistics(data):
# #     """Displays summary statistics graphically"""
# #     sns.set(style="whitegrid")
# #     plt.figure(figsize=(10, 6))
# #     ax = sns.barplot(data.columns, data.loc['mean'], palette="Blues_d")
# #     ax.set_title("Summary Statistics")
# #     ax.set_ylabel("Mean Value")
# #     ax.set_xlabel("Feature")
# #     plt.xticks(rotation=45)
# #     plt.tight_layout()
# #     plt.show()
# #
# #
# # def display_correlation_graph(correlation_data):
# #     """Displays correlation graphically"""
# #     sns.set(style="white")
# #     mask = correlation_data.applymap(lambda x: True if abs(x) < 0.7 else False)
# #     plt.figure(figsize=(10, 8))
# #     sns.heatmap(correlation_data, annot=True, cmap="coolwarm", mask=mask)
# #     plt.title("Correlation Heatmap")
# #     plt.show()
# #
# # if __name__ == "__main__":
# #     model = HeartDiseaseModel()
# #     summary_stats = model.summary_statistics()
# #     correlations = model.calculate_correlations()
# #
# #     # Display summary statistics graphically
# #     summary_stats_df = pd.read_csv(pd.compat.StringIO(summary_stats), delimiter=r"\s{2,}", engine='python')
# #     display_summary_statistics(summary_stats_df)
# #
# #     # Display correlation graphically
# #     correlations_df = pd.read_csv(pd.compat.StringIO(correlations), delimiter=r"\s{2,}", engine='python', index_col=0)
# #     display_correlation_graph(correlations_df)

"""holds the data and calculations"""

import pandas as pd
import tkinter as tk


# class HeartDiseaseModel:
#     def __init__(self):
#         self.data = None
#         self.load_data()
#
#     def load_data(self):
#         """for loading the data from a CSV file"""
#         self.data = pd.read_csv('heart.csv')
#
#     # def summary_statistics(self):
#     #     return self.data.describe()
#     #
#     # def correlations(self):
#     #     return self.data.corr()
#
#     def summary_statistics(self):
#         """returns summary statistics for the data"""
#         summary_stats = self.data.describe()
#         return summary_stats.to_string()
#
#     def calculate_correlations(self):
#         """returns correlation values for the data"""
#         correlations = self.data.corr()
#         return correlations.to_string()
#
#     def filter_data(self, filters):
#         """filters the data based on the given criteria"""
#         filtered_data = self.data.copy()
#         for column, value in filters.items():
#             filtered_data = filtered_data[filtered_data[column] == value]
#         return filtered_data

