import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter


# Load the data from the CSV
df = pd.read_csv('./salesforce_accounts.csv')

# Function to plot and save a horizontal bar chart
def plot_and_save_barh(data, title, xlabel, ylabel, file_path, label_format="{:.2f}"):
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(data.index, data.values, color='skyblue')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Adding data labels
    for bar in bars:
        width = bar.get_width()
        ax.text(width + (width * 0.01), bar.get_y() + bar.get_height() / 2, label_format.format(width), va='center')

    # Save the plot as PNG
    fig.savefig(file_path)
    plt.close(fig)  # Close the figure after saving to free up memory

# Function to plot and save a pie chart
def plot_and_save_pie(sizes, labels, title, file_path, colors=None):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.set_title(title)

    # Save the plot as PNG
    fig.savefig(file_path)
    plt.close(fig)  # Close the figure after saving to free up memory

def aggregate_string_counts(data_column):
    # Aggregate the string counts using Counter
    counts = Counter(data_column)
    
    # Create two lists: one for labels and one for counts
    labels = list(counts.keys())
    values = list(counts.values())
    
    return labels, values

# Data for the plots
opportunity_stage_counts = df['opportunity_stage'].value_counts()
average_opportunity_amount_by_stage = df.groupby('opportunity_stage')['opportunity_amount'].mean()
opportunities_labels, opportunities_values = aggregate_string_counts(df['opportunity_stage'])
total_opportunities = df.shape[0]
closed_won_count = df[df['opportunity_stage'] == 'Closed Won'].shape[0]
win_rate = (closed_won_count / total_opportunities) * 100

# File paths for saving the plots
pipeline_stage_file_path = './opportunity_pipeline_by_stage.png'
average_amount_file_path = './average_opportunity_amount_by_stage.png'
win_rate_file_path = './opportunity_win_rate.png'

# Use the functions to create and save the plots
plot_and_save_barh(
    data=opportunity_stage_counts,
    title='Opportunity Pipeline by Stage',
    xlabel='Number of Opportunities',
    ylabel='Opportunity Stage',
    file_path=pipeline_stage_file_path,
    label_format="{:,.0f}"
)

plot_and_save_barh(
    data=average_opportunity_amount_by_stage,
    title='Average Opportunity Amount by Stage',
    xlabel='Average Opportunity Amount (USD)',
    ylabel='Opportunity Stage',
    file_path=average_amount_file_path,
    label_format="${:,.2f}"
)

plot_and_save_pie(
    sizes=opportunities_values,
    labels=opportunities_labels,
    title='Opportunity Win Rate',
    file_path=win_rate_file_path,
)

pipeline_stage_file_path, average_amount_file_path, win_rate_file_path

