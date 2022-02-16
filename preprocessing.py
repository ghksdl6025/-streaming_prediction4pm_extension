from numpy import concatenate
import pandas as pd

iro = pd.read_csv('./DATA/logs/IRO5k.csv')
oir = pd.read_csv('./DATA/logs/OIR5k.csv')

iro_cases = list(iro.loc[:,'Case ID'])
oir_cases = list(oir.loc[:,'Case ID'])
baseline_cases = []
iro1_cases = []
oir1_cases = []

for x in set(iro_cases):
    if 'b1' in x:
        baseline_cases.append(x)
    elif 'IRO1' in x:
        iro1_cases.append(x)

for y in set(oir_cases):
    if 'oir1' in y:
        oir1_cases.append(y)

baseline_df = iro[iro['Case ID'].isin(baseline_cases)]
iro1_df = iro[iro['Case ID'].isin(iro1_cases)]
oir1_df = oir[oir['Case ID'].isin(oir1_cases)]

baseline_df['Complete Timestamp'] = pd.to_datetime(baseline_df['Complete Timestamp'])
baseline_df = baseline_df.sort_values(by='Complete Timestamp')

iro1_df['Complete Timestamp'] = pd.to_datetime(iro1_df['Complete Timestamp'])
iro1_df = iro1_df.sort_values(by='Complete Timestamp')

oir1_df['Complete Timestamp'] = pd.to_datetime(oir1_df['Complete Timestamp'])
oir1_df = oir1_df.sort_values(by='Complete Timestamp')

# 2004-03-16
# 2004-03-17 10:00:00 2004-04-29 18:29:38.633000

# print(baseline_df)
iro1_modified_time = []
for x in list(iro1_df['Complete Timestamp']):
    y = x - pd.Timedelta(weeks=50, days=3)
    iro1_modified_time.append(y)
print(min(iro1_modified_time), max(iro1_modified_time))

oir1_modified_time = []
for x in list(oir1_df['Complete Timestamp']):
    y = x - pd.Timedelta(weeks=43, days=5)
    oir1_modified_time.append(y)
print(min(oir1_modified_time), max(oir1_modified_time))

iro1_df.loc[:,'Complete Timestamp'] = iro1_modified_time
oir1_df.loc[:,'Complete Timestamp'] = oir1_modified_time

baseline_df = baseline_df.drop(['Resource','Variant', 'Variant index'], axis=1)
cat1_df = pd.concat([baseline_df, iro1_df])
cat1_df = cat1_df.drop(['Resource','Variant', 'Variant index'], axis=1)

cat2_df = pd.concat([baseline_df, oir1_df])
cat2_df = cat2_df.drop(['Resource','Variant', 'Variant index'], axis=1)

cat3_df = pd.concat([baseline_df, iro1_df, oir1_df])
cat3_df = cat3_df.drop(['Resource','Variant', 'Variant index'], axis=1)

baseline_df.to_csv('./DATA/logs/synthetic_log_b.csv',index=False)
cat1_df.to_csv('./DATA/logs/synthetic_log_bc1.csv',index=False)
cat2_df.to_csv('./DATA/logs/synthetic_log_bc2.csv',index=False)
cat3_df.to_csv('./DATA/logs/synthetic_log_bc1c2.csv',index=False)
