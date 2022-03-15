import pandas as pd
import numpy as np
import pickle as pkl
import os
resultdict = {}

datalabsel_list = ['synthetic_log_b']#, 'synthetic_log_bc1', 'synthetic_log_bc2', 'synthetic_log_bc1c2','bpic17', 'bpic15']

# for counter in [50,100,200]:
#     for classifier in ['htc', 'hatc', 'efdt']:

#         for datalabel in datalabsel_list:
#             with open('./result/%s/%s %s window 50 window_acc.pkl'%(datalabel, datalabel, classifier) ,'rb') as result_file:
#                 data = pkl.load(result_file)

#             for t in data.keys():
#                 if 'prefix_' in t:
#                     e = data[t]
#                     prefix = t.split('_')[1]
            
#                 else:
#                     continue

#                 time = data['Time']
#                 acc_interval =deque([])

#                 acc_outlier = []
#                 acc_mean_list = []
#                 acc_std_list = []
#                 new_observation = []
#                 normality = []
#                 for pos, x in enumerate(e):
#                     normal = True
#                     if pos ==0:
#                         acc_mean_list.append(x)
#                         acc_std_list.append(0)
                    
#                     else:
#                         acc_mean = np.mean(acc_interval)
#                         acc_std = np.std(acc_interval)
#                         if x > acc_mean+acc_std or x < acc_mean-acc_std:
#                             normal = False
#                         acc_mean_list.append(acc_mean)
#                         acc_std_list.append(acc_std)
#                     new_observation.append(x)
#                     normality.append(normal)

#                     acc_interval.append(x)
#                     if len(acc_interval) >counter:
#                         acc_interval.popleft()


                
#                 df = pd.DataFrame(columns=['Acc mean', 'Acc std','New observation','Normality'])
#                 df['Acc mean'] = acc_mean_list
#                 df['Acc std'] = acc_std_list
#                 df['New observation'] = new_observation
#                 df['Normality'] = normality
#                 df['Time'] = time

#                 end_signal = len(df)
#                 df.loc[end_signal, 'Time'] = time[-1] + pd.Timedelta(minutes=1)
#                 df.loc[end_signal, 'Normality'] = True

#                 try:
#                     os.makedirs('./img/%s/%s'%(datalabel, classifier))
#                 except:
#                     pass
                
#                 print(df.head)

#                 df.to_csv('./img/%s/%s/result%s prefix%s.csv'%(datalabel, classifier, counter, prefix), index=False)


datalabsel_list = ['synthetic_log_b', 'synthetic_log_bc1', 'synthetic_log_bc2', 'synthetic_log_bc1c2','bpic17', 'bpic15']

df_datalabel = []
df_classifier= []
df_counter = []
df_results = []
for datalabel in datalabsel_list:
    for counter in [200]:
        for classifier in ['htc', 'hatc', 'efdt']:
            maxlength = 0
            
            for x in list(os.listdir('./img/%s/%s/'%(datalabel, classifier))):
                x = x.replace(' ','.').split('.')
                x1 = x[1].split('x')
                prefix_length = int(x1[1])
                if 'png' in x[2] and maxlength < prefix_length:
                    maxlength = prefix_length

            # print(os.path.basename('./img/synthetic_log_b/efdt/result100 prefix10.csv'))

            average_diff = []
            for t in range(2, maxlength+1):
                df = pd.read_csv('./img/%s/%s/result%s prefix%s.csv'%(datalabel, classifier,counter,t))
                prediction_score = list(df['New observation'])
                diffs_list = []
                for pos, x in enumerate(prediction_score):
                    if pos ==0:
                        pass
                    elif pos == len(prediction_score)-1:
                        pass
                    else:
                        diffs_list.append(abs(x - prediction_score[pos-1]))

                average_diff.append(np.average(diffs_list))
            df_datalabel.append(datalabel)
            df_classifier.append(classifier)
            df_counter.append(counter)
            df_results.append(1-np.average(average_diff))

df1 = pd.DataFrame(columns=['Datalabel','Classifier','Counter','Results'])
df1['Datalabel'] = df_datalabel
df1['Classifier'] = df_classifier
df1['Counter'] = df_counter
df1['Results'] = df_results
df1.to_csv('./temporal_stability_result.csv',index=False)
