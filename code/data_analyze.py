import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from model import HeartDiseaseModel

# data = pd.read_csv('heart.csv')
# print([i for i in data.columns])

# Load the data
heart_disease_model = HeartDiseaseModel()
data = heart_disease_model.data

# Iterate through each column
for column in data.columns:
    # # Create a new figure for each plot
    # plt.figure()
    #
    # # Plot the distribution of data in the column using seaborn's distplot
    # sns.histplot(data[column], kde=True)
    # plt.title(f'Distribution of {column}')
    # plt.xlabel(column)
    # plt.ylabel('Frequency')
    #
    # # Show the plot
    # plt.show()

    max_value = data[column].max()
    min_value = data[column].min()
    iqr_value = data[column].quantile(0.75) - data[column].quantile(0.25)
    data_range = max_value - min_value
    std_dev = data[column].std()
    variance = data[column].var()
    mode_value = data[column].mode().values[0] if data[column].dtype == 'object' else None  # Mode for nominal data

    # Plot histograms
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    sns.histplot(data[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)

    # Plot boxplots
    plt.subplot(1, 2, 2)
    sns.boxplot(data[column])
    plt.title(f'Boxplot of {column}')
    plt.xlabel(column)
    plt.tight_layout()

    # Print statistics
    print(f"Column: {column}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"IQR: {iqr_value}")
    print(f"Range: {data_range}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Variance: {variance}")
    print(f"Mode: {mode_value}\n")

    # Show plots
    plt.show()