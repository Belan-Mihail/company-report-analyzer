import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# 1 Loading data from sales_data.csv
df = pd.read_csv('sales_data.csv')

selected_reports = ['report1']

def generate_pdf(df, selected_reports):

    
    # if first report in selected_reports:
        if 'report1' in selected_reports:
            print('hello report1')

generate_pdf(df, selected_reports)