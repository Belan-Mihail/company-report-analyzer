import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from io import BytesIO


def generate_pdf(df, selected_reports):

    # Create a BytesIO object to hold the PDF content
    pdf_buffer = BytesIO()
    pdf_pages = PdfPages(pdf_buffer)

    # Converting the 'Date' column to date format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # if report1 in selected_reports:
    if 'report1' in selected_reports:

        # group sales by region
        region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
        
        # Abbreviation of region names to the first 7 letters
        region_sales.index = region_sales.index.str.slice(0,7)

        # Plotting a graph
        plt.figure(figsize=(8,6))
        sns.barplot(x=region_sales.index, y=region_sales.values)
        plt.title('Sales by region')
        plt.xticks(rotation=45) # Rotate captions to improve readability
        pdf_pages.savefig()
        plt.close
        
        

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
        
        # Sales Distribution
        plt.hist(df['Sales'], bins=20, color='skyblue', edgecolor='black')
        plt.title('Sales Distribution')
        
    
    # if report5 in selected_reports:
    if 'report5' in selected_reports:
        
        # Average sales by region
        region_avg_sale = df.groupby('Region')['Sales'].mean()
        
        # Shorten region name and rotate x 
        region_avg_sale.index = region_avg_sale.index.str.slice(0,10)
        plt.xticks(rotation=45)

        # Plotting graph
        sns.barplot(x=region_avg_sale.index, y=region_avg_sale.values)
        plt.title('Average sales by region')
        plt.show()

    # if report6 in selected_reports:
    if 'report6' in selected_reports:
        
        # Correlation between sales and dates
        corr = df[['Sales', 'Date']].corr()

        # Add graph
        sns.heatmap(corr, annot=True, cmap='coolwarm', cbar=True)
        plt.title('Correlation between sales and dates')
        

    # if report7 in selected_reports:
    if 'report7' in selected_reports:
        
        # Checking for the existence of the month column in the table
        if 'Month' not in df.columns:
            df['Month'] = df['Date'].dt.to_period('M')

        # Sales by month and region
        sales_by_month_region = df.groupby(['Region', 'Month'])['Sales'].sum()

        # Create graph
        sales_by_month_region.plot(kind='line', title='Sale trends by month and region')
        
        
    # if report8 in selected_reports:
    if 'report8' in selected_reports:
        
        # Percentage distribution of sales by region
        percentage_by_region = round(df.groupby('Region')['Sales'].sum() / df['Sales'].sum() * 100, 2)
        
        # Percentage distribution of sales by companies
        percentage_by_companies = round(df.groupby('Company')['Sales'].sum() / df['Sales'].sum() * 100, 2)

        # Create a figure with two subgraphs
        fig, axes = plt.subplots(1, 2, figsize=(14, 7))

        # Graph for regions
        percentage_by_region.plot(kind='pie', autopct='%1.1f%%', title='Percentage distribution of sales by region', ax=axes[0])

        # Graph fro companies
        percentage_by_companies.plot(kind='pie', autopct='%1.1f%%', title='Percentage distribution of sales by companies', ax=axes[1] )

        plt.tight_layout()
        plt.show()
        

