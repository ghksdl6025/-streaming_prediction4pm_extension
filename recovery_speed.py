import pandas as pd
import numpy as np
import os
import datetime
import json

from sympy import sec

resultdict = {}

performance_measure = 'WeightedF1'

for x in ['Dataset','Classifier','Window size', 'Frequency of drop','Average recovery speed', 'Normalized recovery speed',
        'Max performance drop','Average performance drop','Stability of performance']:
    resultdict[x] = []
    
datalabsel_list = ['bpic17','synthetic_log_b', 'synthetic_log_bc1', 'synthetic_log_bc2', 'synthetic_log_bc1c2', 'bpic15']

for counter in [50,200]:
    for classifier in ['htc', 'hatc', 'efdt']:
        for datalabel in datalabsel_list:
            with open('./result/%s_graceperiod.txt'%(datalabel), 'r') as f:
                grace_period = f.read()
            grace_period = grace_period.split()
            days = grace_period[0]
            time = grace_period[2].split(':')
            hours, mins, secs = time[0], time[1],time[2]
            days = int(days) *24*60*60
            hours = int(hours) * 60*60
            mins = int(mins) * 60
            secs = int(secs)
            total_secs = days +hours + mins+ secs
            grace_period = total_secs/(60*60*24*30)

            with open('./result/%s_testperiod.txt'%(datalabel), 'r') as f:
                test_period = f.read()
            test_period = test_period.split()
            days = test_period[0]
            time = test_period[2].split(':')
            hours, mins, secs = time[0], time[1],time[2]
            days = int(days) *24*60*60
            hours = int(hours) * 60*60
            mins = int(mins) * 60
            secs = int(secs)
            total_secs = days +hours + mins+ secs
            test_period = total_secs/(60*60*24*30)

            denominator = test_period/grace_period
            # print(test_period, grace_period, test_period/grace_period)
            df = pd.read_csv('./img/%s/%s/%s %s result%s.csv'%(datalabel, classifier, classifier, performance_measure, counter))
            df['Time'] = pd.to_datetime(df['Time'])

            previous_label = True
            set_of_false = []
            
            false_period = []
            false_period_gap =[]

            std_by_window = []

            false_counter = 0
            for pos, t in enumerate(list(df['Normality'])):
                if t == False:
                    false_counter +=1
                    false_period.append(list(df['New observation'])[pos])

                        
                    if list(df['New observation'])[pos] < list(df['Acc mean'])[pos]:
                        gap = abs(list(df['New observation'])[pos]- (list(df['Acc mean'])[pos]-list(df['Acc std'])[pos]))
                    else:
                        gap = abs(list(df['New observation'])[pos]- (list(df['Acc mean'])[pos]+list(df['Acc std'])[pos]))

                    false_period_gap.append(gap)

                elif t == True:
                    if len(false_period) !=0:
                        set_of_false.append([false_period,false_period_gap])
                    false_period = []
                    false_period_gap =[]

                if ~np.isnan(list(df['Acc std'])[pos]):
                    std_by_window.append(list(df['Acc std'])[pos])
            

            total_seconds = (max(df['Time'])- min(df['Time'])).total_seconds()
            recovery_speed_list = [len(f) for f,_ in set_of_false]
            max_gap = np.max([max(g) for _,g in set_of_false])
            avg_gap = np.mean([g for _,gl in set_of_false for g in gl])
            stdlist = [x for x in list(df['Acc std']) if ~np.isnan(x)]
            stability_of_performance = np.mean(stdlist)

            
            print(datalabel, classifier, counter)
            print('Average recovery speed: ', np.mean(recovery_speed_list))
            print('Normalized recovery speed: ', np.mean(recovery_speed_list)/counter)
            # print('Frequency of drop: ', false_counter)
            print('Frequency of drop: ', round(false_counter/denominator,1))
            print('Max performance drop: ', max_gap)
            print('Average performance drop: ', avg_gap)
            print('Stability of performance: ', stability_of_performance)


            resultdict['Dataset'].append(datalabel)
            resultdict['Classifier'].append(classifier)
            resultdict['Window size'].append(counter)
            # resultdict['Frequency of drop'].append(false_counter)
            resultdict['Frequency of drop'].append(round(false_counter/denominator,1))
            resultdict['Average recovery speed'].append(round(np.mean(recovery_speed_list),2))
            resultdict['Normalized recovery speed'].append(round(np.mean(recovery_speed_list)/counter,2))
            resultdict['Max performance drop'].append(round(max_gap,2))
            resultdict['Average performance drop'].append(round(avg_gap,2))
            resultdict['Stability of performance'].append(round(stability_of_performance,2))




df= pd.DataFrame.from_dict(resultdict)
df = df.sort_values(by='Dataset')
print(df)

try:
    os.makedirs('./metrics/')
except:
    pass

df.to_csv('./metrics/%s evaluation metrics.csv'%(performance_measure),index=False)

