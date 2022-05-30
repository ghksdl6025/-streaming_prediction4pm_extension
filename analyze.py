from numpy import mean
import pandas as pd
import numpy as np
df = pd.read_csv('./DATA/logs/synthetic_log_bc1c2.csv')

groups = df.groupby('Case ID')

actnums = []

for _, group in groups:
    actnums.append(len(group))

print(np.mean(actnums), np.median(actnums))