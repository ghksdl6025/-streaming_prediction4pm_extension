import pandas as pd
import numpy as np



resultdict = {}

for x in ['Dataset','Classifier','Window size','Average return time','Return time to total time', 'Frequency of drop','Total drops per Month','Max performance drop','Average performance drop']:
    resultdict[x] = []
    
datalabsel_list = ['synthetic_log_b', 'synthetic_log_bc1', 'synthetic_log_bc2', 'synthetic_log_bc1c2', 'bpic15' ,'bpic17']
for counter in [50,200]:
    for classifier in ['htc', 'hatc', 'efdt']:
        for datalabel in datalabsel_list:
            df = pd.read_csv('./img/%s/%s result%s.csv'%(datalabel, classifier, counter))
            df['Time'] = pd.to_datetime(df['Time'])


            previous_label = True
            set_of_false = []
            false_start = ''
            false_end = ''

            max_gap_list = []
            maximum_gap = 0
            false_counter = 0
            for pos, t in enumerate(list(df['Normality'])):
                if t == False:
                    false_counter +=1
                    if previous_label == True:
                        false_start = list(df['Time'])[pos]
                        previous_label = False
                        maximum_gap = abs(list(df['New observation'])[pos]- list(df['Acc mean'])[pos])
                        maximum_gap = 0

                    if abs(list(df['New observation'])[pos]- list(df['Acc mean'])[pos]) > maximum_gap:
                        maximum_gap = abs(list(df['New observation'])[pos]- list(df['Acc mean'])[pos])

                if t == True:
                    if previous_label == False:
                        false_end = list(df['Time'])[pos-1]
                        max_gap_list.append(maximum_gap)
                        previous_label = True
                        set_of_false.append([false_start, false_end])

            return_times = []
            for x in set_of_false:
                return_times.append(x[1]-x[0])

            total_seconds = (max(df['Time'])- min(df['Time'])).total_seconds()
            # print(datalabel, classifier, counter)
            # print('Average return time: ', np.mean(return_times))
            # print('Return time to total time: ', np.sum(return_times).total_seconds()/total_seconds)
            # print('Frequency of drop: ', false_counter)
            # print('Total drops per Month: ', round(false_counter*60*24*30/total_seconds,2))
            # print('Max performance drop: ', round(max(max_gap_list),3))
            # print('Average performance drop: ', round(np.mean(max_gap_list),3))
            resultdict['Dataset'].append(datalabel)
            resultdict['Classifier'].append(classifier)
            resultdict['Window size'].append(counter)
            resultdict['Average return time'].append(np.mean(return_times))
            resultdict['Return time to total time'].append(np.sum(return_times).total_seconds()/total_seconds)
            resultdict['Frequency of drop'].append(false_counter)
            resultdict['Total drops per Month'].append(round(false_counter*60*24*30/total_seconds,2))
            resultdict['Max performance drop'].append(round(max(max_gap_list),3))
            resultdict['Average performance drop'].append(round(np.mean(max_gap_list),3))

df= pd.DataFrame.from_dict(resultdict)
# df = df.sort_values(by='Dataset')
df.to_csv('./evaluation metrics.csv',index=False)

