import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# 1 Loading data from sales_data.csv
df = pd.read_csv('sales_data.csv')

selected_reports = ['report1', 'report3', 'report6', 'report8']

def generate_pdf(df, selected_reports):

    
    # if report1 in selected_reports:
    if 'report1' in selected_reports:
        print('hello report1')

    # if report2 in selected_reports:
    if 'report2' in selected_reports:
        print('hello report2')
    
    # if report3 in selected_reports:
    if 'report3' in selected_reports:
        print('hello report3')
    
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