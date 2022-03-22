import pandas as pd
import numpy as np



resultdict = {}

<<<<<<< HEAD
for x in ['Dataset','Classifier','Window size','Frequency of drop','Total drops per Month','Average recovery speed', 'Normalized recovery speed', 'Max performance drop','Average performance drop', 'Stability performance drop']:
    resultdict[x] = []
    
datalabsel_list = ['bpic17', 'synthetic_log_b', 'synthetic_log_bc1', 'synthetic_log_bc2', 'synthetic_log_bc1c2', 'bpic15']
for counter in [50, 200]:
=======
for x in ['Dataset','Classifier','Window size', 'Frequency of drop','Total drops per Month','Average recovery speed', 'Normalized recovery speed',
        'Max performance drop','Average performance drop','Stability of performance']:
    resultdict[x] = []
    
datalabsel_list = ['bpic17','synthetic_log_b', 'synthetic_log_bc1', 'synthetic_log_bc2', 'synthetic_log_bc1c2', 'bpic15']
for counter in [50,200]:
>>>>>>> ec758b1 (22.03.2022 upload)
    for classifier in ['htc', 'hatc', 'efdt']:
        for datalabel in datalabsel_list:
            df = pd.read_csv('./img/%s/%s result%s.csv'%(datalabel, classifier, counter))
            df['Time'] = pd.to_datetime(df['Time'])

            previous_label = True
            set_of_false = []
            
            false_period = []
            false_period_gap =[]

            std_by_window = []

<<<<<<< HEAD
=======
            gap_list = []
            
>>>>>>> ec758b1 (22.03.2022 upload)
            false_counter = 0
            for pos, t in enumerate(list(df['Normality'])):
                if t == False:
                    false_counter +=1
                    false_period.append(list(df['New observation'])[pos])
<<<<<<< HEAD
                        
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
            
            max_gap_list = []
            outlier_counter_list = []
            for pos, (values, gap) in enumerate(set_of_false):
                max_gap_list.append(max(gap))
                outlier_counter_list.append(len(values))
=======

                    if list(df['New observation'])[pos] < list(df['Acc mean'])[pos]:
                        gap = abs(list(df['New observation'])[pos]- (list(df['Acc mean'])[pos] - list(df['Acc std'])[pos]))
                    elif list(df['New observation'])[pos] > list(df['Acc mean'])[pos]:
                        gap = abs(list(df['New observation'])[pos]- (list(df['Acc mean'])[pos] + list(df['Acc std'])[pos]))

                    gap_list.append(gap)        

                if t == True:
                    if len(false_period) !=0:
                        set_of_false.append([false_period, gap_list])
                        gap_list = []
                        false_period = []
>>>>>>> ec758b1 (22.03.2022 upload)

            total_seconds = (max(df['Time'])- min(df['Time'])).total_seconds()

<<<<<<< HEAD
            print(datalabel, classifier, counter)
            # print('Average return time: ', np.mean(return_times))
            # print('Return time to total time: ', np.sum(return_times).total_seconds()/total_seconds)
            print('Average recovery speed: ', np.mean(outlier_counter_list))
            print('Normalized recovery speed: ', round(np.mean(outlier_counter_list)/counter,2))

            print('Frequency of drop: ', false_counter)
            print('Total drops per Month: ', round(false_counter*60*24*30/total_seconds,2))

            print('Max performance drop: ', round(max(max_gap_list),3))
            print('Average performance drop: ', round(np.mean(max_gap_list),3))

            print('Stability of performance: ', np.mean(std_by_window))
=======
            recovery_speed_list = [len(f) for f,_ in set_of_false]
            max_gap = np.max([max(g) for _,g in set_of_false])
            avg_gap = np.mean([g for _,gl in set_of_false for g in gl])
            stdlist = [x for x in list(df['Acc std']) if ~np.isnan(x)]
            stability_of_performance = np.mean(stdlist)

            print(np.average(recovery_speed_list), max_gap, avg_gap)
            print(datalabel, classifier, counter)
            print('Average recovery speed: ', np.mean(recovery_speed_list))
            print('Normalized recovery speed: ', np.mean(recovery_speed_list)/counter)
            print('Frequency of drop: ', false_counter)
            print('Total drops per Month: ', round(false_counter*60*24*30/total_seconds,2))
            print('Max performance drop: ', max_gap)
            print('Average performance drop: ', avg_gap)
            print('Stability of performance: ', stability_of_performance)

>>>>>>> ec758b1 (22.03.2022 upload)
            resultdict['Dataset'].append(datalabel)
            resultdict['Classifier'].append(classifier)
            resultdict['Window size'].append(counter)
            resultdict['Frequency of drop'].append(false_counter)
            resultdict['Total drops per Month'].append(round(false_counter*60*24*30/total_seconds,2))
<<<<<<< HEAD
            resultdict['Max performance drop'].append(round(max(max_gap_list),3))
            resultdict['Average performance drop'].append(round(np.mean(max_gap_list),3))
            resultdict['Average recovery speed'].append(np.mean(outlier_counter_list))
            resultdict['Normalized recovery speed'].append(round(np.mean(outlier_counter_list)/counter,2))
            resultdict['Stability performance drop'].append(np.mean(std_by_window))
=======
            resultdict['Average recovery speed'].append(round(np.mean(recovery_speed_list),2))
            resultdict['Normalized recovery speed'].append(round(np.mean(recovery_speed_list)/counter,2))
            resultdict['Max performance drop'].append(round(max_gap,2))
            resultdict['Average performance drop'].append(round(avg_gap,2))
            resultdict['Stability of performance'].append(round(stability_of_performance,2))




>>>>>>> ec758b1 (22.03.2022 upload)
df= pd.DataFrame.from_dict(resultdict)
df = df.sort_values(by='Dataset')
df.to_csv('./evaluation metrics.csv',index=False)

