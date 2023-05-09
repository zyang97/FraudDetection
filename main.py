import pandas as pd
import numpy as np

# read csv
df = pd.read_csv('dataset/PS_20174392719_1491204439457_log.csv')

df.head(10)

df.isnull().values.any()

list(df.loc[df.isFraud == 1].type.drop_duplicates().values)