import pandas as pd
import numpy as np


datalabsel_list = ['bpic15', 'synthetic_log_b', 'synthetic_log_bc1', 'synthetic_log_bc2', 'synthetic_log_bc1c2', 'bpic17',]
for counter in [50,100,200]:
    for classifier in ['htc', 'hatc', 'efdt']:
        for datalabel in datalabsel_list:
            df = pd.read_csv('./img/%s/%s result%s.csv'%(datalabel, classifier, counter))
            df['Time'] = pd.to_datetime(df['Time'])


            previous_label = True
            max_gap_list = []
            maximum_gap = 0
            false_counter = 0
            for pos, t in enumerate(list(df['Normality'])):
                if t == False:
                    
                    false_counter +=1
                    if previous_label == True:
                        maximum_gap = 0
                        maximum_gap = abs(list(df['New observation'])[pos]- list(df['Acc mean'])[pos])
                        previous_label = False
                    
                    if abs(list(df['New observation'])[pos]- list(df['Acc mean'])[pos]) > maximum_gap:
                        maximum_gap = abs(list(df['New observation'])[pos]- list(df['Acc mean'])[pos])
                if t == True:
                    if previous_label == False:
                        max_gap_list.append(maximum_gap)
                        previous_label = True

            
            print(datalabel, classifier, counter, '/',round(max(max_gap_list),3), '/',round(np.mean(max_gap_list),3))
            # print(np.mean(return_times), false_counter, round(false_counter*60*24*30/total_seconds,2))


