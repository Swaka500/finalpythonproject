import pandas as pd
import ipywidgets as widgets
from IPython.display import display

# Load your cleaned COVID-19 data
df = pd.read_csv('covid_data.csv')

# Create widgets for country and date range selection
country_widget = widgets.Dropdown(
    options=df['location'].unique(),
    description='Country:'
)

date_widget = widgets.SelectionRangeSlider(
    options=sorted(df['date'].unique()),
    index=(0, len(df['date'].unique()) - 1),
    description='Date Range:',
    continuous_update=False
)

# Function to filter data based on user input
def filter_data(country, date_range):
    filtered_df = df[(df['location'] == country) & 
                     (df['date'] >= date_range[0]) & 
                     (df['date'] <= date_range[1])]
    display(filtered_df.head())  # Display the first few rows of filtered data

# Create interactive display
widgets.interactive(filter_data, country=country_widget, date_range=date_widget)
