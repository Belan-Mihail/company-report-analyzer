import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# 1 Loading data from sales_data.csv
df = pd.read_csv('sales_data.csv')#

print(df.head())