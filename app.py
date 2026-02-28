# [app.py](http://_vscodecontentref_/3)
import pandas as pd

# URL of the CSV file on GitHub
url = (
    "https://raw.githubusercontent.com/"
    "justinjohn0306/Sample-Superstore-Data/main/SampleSuperstore.csv"
)

# read the data
df = pd.read_excel(r"C:\Users\LENOVO\Downloads\sample_-_superstore.xls")

# quick look
print(df.head())
print(df.describe())

# ... perform cleaning, EDA, plotting, etc. ...