import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# 1 Loading data from sales_data.csv
df = pd.read_csv('sales_data.csv')

selected_reports = ['report3']

def generate_pdf(df, selected_reports):

    df = pd.read_csv('sales_data.csv')

    # Converting the 'Date' column to date format
    df['Date'] = pd.to_datetime(df['Date'])
    
    
    # if report1 in selected_reports:
    if 'report1' in selected_reports:

        # group sales by region
        region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
        
        # Abbreviation of region names to the first 7 letters
        region_sales.index = region_sales.index.str.slice(0,7)

        # Plotting a graph
        sns.barplot(x=region_sales.index, y=region_sales.values)
        plt.title('Sales by region')
        plt.xticks(rotation=45) # Rotate captions to improve readability
        # plt.show()
        

    # if report2 in selected_reports:
    if 'report2' in selected_reports:
        
        # Group sales by company
        company_sales = df.groupby('Company')['Sales'].sum().sort_values(ascending=False)
        print(company_sales)

        # Abbreviation of region names to the first 10 letters
        company_sales.index = company_sales.index.str.slice(0,10)

        # Plotting a graph
        sns.barplot(x=company_sales.index, y=company_sales.values)
        plt.title('Sales by companies')
        plt.xticks(rotation=45)
        plt.show()

    
    # if report3 in selected_reports:
    if 'report3' in selected_reports:
        
        # add month column
        df['Month'] = df['Date'].dt.to_period('M')
        
        # Sales by month
        sales_by_month = df.groupby('Month')['Sales'].sum()

        # Plotting a graph
        sales_by_month.plot(kind='line', title='Sales by month')
        

        

    
    # if report4 in selected_reports:
    if 'report4' in selected_reports:
        print('hello report4')
    
    # if report5 in selected_reports:
    if 'report5' in selected_reports:
        print('hello report5')

    # if report6 in selected_reports:
    if 'report6' in selected_reports:
        print('hello report6')

    # if report7 in selected_reports:
    if 'report7' in selected_reports:
        print('hello report7')

    # if report8 in selected_reports:
    if 'report8' in selected_reports:
        print('hello report8')

generate_pdf(df, selected_reports)