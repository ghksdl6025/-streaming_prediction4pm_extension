import pickle as pkl
import pandas as pd
from collections import deque
import numpy as np
import os 

datalabsel_list = ['bpic17','synthetic_log_b', 'synthetic_log_bc1', 'synthetic_log_bc2', 'synthetic_log_bc1c2', 'bpic15']

# classifier = 'htc'
# counter = 200
performance_measure = 'ROCAUC'
for counter in [50, 100, 200]:
    for classifier in ['htc', 'hatc', 'efdt']:

        for datalabel in datalabsel_list:
            with open('./result/%s/%s %s window 50 %s.pkl'%(datalabel, datalabel, classifier, performance_measure) ,'rb') as result_file:
                data = pkl.load(result_file)

            
            e = data['Accuracy']
            time = data['Time']
            acc_interval =deque([])

            acc_outlier = []
            acc_mean_list = []
            acc_std_list = []
            new_observation = []
            normality = []
            for pos, x in enumerate(e):
                normal = True
                if pos ==0:
                    acc_mean_list.append(0)
                    acc_std_list.append(0)
                    
                else:
                    acc_mean = np.mean(acc_interval)
                    acc_std = np.std(acc_interval)
                    if x > acc_mean+acc_std or x < acc_mean-acc_std:
                        normal = False
                    acc_mean_list.append(acc_mean)
                    acc_std_list.append(acc_std)
                new_observation.append(x)
                normality.append(normal)

                if pos !=0:
                    acc_interval.append(x)
                if len(acc_interval) >counter:
                    acc_interval.popleft()


            
            df = pd.DataFrame(columns=['Acc mean', 'Acc std','New observation','Normality'])
            df['Acc mean'] = acc_mean_list
            df['Acc std'] = acc_std_list
            df['New observation'] = new_observation
            df['Normality'] = normality
            df['Time'] = time


            with open('./result/%s/%s %s window 50 window_%s.pkl'%(datalabel, datalabel, classifier, performance_measure) ,'rb') as result_file:
                data = pkl.load(result_file)

            for t in data.keys():

                if 'prefix_' in t:
                    df.loc[:,t] = data[t]

            end_signal = len(df)
            
            try:
                os.makedirs('./img/%s/%s/%s'%(datalabel, classifier, performance_measure))
            except:
                pass
            

            df.to_csv('./img/%s/%s/%s %s result%s.csv'%(datalabel, classifier, classifier, performance_measure, counter), index=False)

