import pandas as pd
import numpy as np


datalabsel_list = ['bpic15',]#'synthetic_log_b', 'synthetic_log_bc1', 'synthetic_log_bc2', 'synthetic_log_bc1c2', 'bpic17',]
for counter in [50,100,200]:
    for classifier in ['htc', 'hatc', 'efdt']:
        for datalabel in datalabsel_list:
            df = pd.read_csv('./img/%s/%s result%s.csv'%(datalabel, classifier, counter))
            df['Time'] = pd.to_datetime(df['Time'])


            previous_label = True
            set_of_false = []
            false_start = ''
            false_end = ''

            false_counter = 0
            for pos, t in enumerate(list(df['Normality'])):
                if t == False:
                    false_counter +=1
                    if previous_label == True:
                        false_start = list(df['Time'])[pos]
                        previous_label = False
                if t == True:
                    if previous_label == False:
                        false_end = list(df['Time'])[pos-1]
                        previous_label = True
                        set_of_false.append([false_start, false_end])

            return_times = []
            for x in set_of_false:
                return_times.append(x[1]-x[0])

            total_seconds = (max(df['Time'])- min(df['Time'])).total_seconds()
            print(datalabel, classifier, counter)
            print(np.mean(return_times), false_counter, round(false_counter*60*24*30/total_seconds,2))
            print('\n')


