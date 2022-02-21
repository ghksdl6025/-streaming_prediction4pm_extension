import pandas as pd

data = pd.read_csv('./DATA/logs/synthetic_log_bc2.csv')
data['Complete Timestamp'] = pd.to_datetime(data['Complete Timestamp'])
groups = data.groupby('Case ID')


dropcase = []
concating = []


for _, events in groups:
    # events = events.sort_values(by='Complete Timestamp')
    events = events.reset_index(drop=True)
    actlist = list(events['Activity'])

    if 'Loan__application_approved' in actlist:
        outcome = True
        labelidx = actlist.index('Loan__application_approved')
    elif 'Loan_application_rejected' in actlist:
        outcome = False
        labelidx = actlist.index('Loan_application_rejected')
    
    elif 'Loan__application_canceled' in actlist:
        #   Loan__application_canceled
        outcome = False
        labelidx = actlist.index('Loan__application_canceled')
    else:
        dropcase.append(events)
    events.loc[labelidx,'outcome'] = outcome
    concating.append(events)

concat = pd.concat(concating)
concat = concat.sort_values(by='Complete Timestamp')
concat.to_csv('./DATA/logs/synthetic_log_bc2.csv', index=False)