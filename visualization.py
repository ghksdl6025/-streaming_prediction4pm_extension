import matplotlib
import json
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd

# datalabsel_list = ['synthetic_log_b', 'synthetic_log_bc1', 'synthetic_log_bc2', 'synthetic_log_bc1c2', 'bpic17', 'bpic15']
# datalabsel_list = ['synthetic_log_bc1c2']#, 'synthetic_log_bc1']
# performance_measure = 'Accuracy'

# # classifier = 'htc'
# # counter = 200
# figure(figsize=(12,8,))

# for counter in [50,100,200]:
#     for classifier in ['htc','hatc','efdt']:
#         for datalabel in datalabsel_list:

#             df = pd.read_csv('./img/%s/%s/%s %s result%s.csv'%(datalabel, classifier,classifier ,performance_measure ,counter))
#             # df50 = pd.read_csv('./result100.csv')
#             x_list =[x+1 for x in df.index.values]

#             x_outliers = []
#             y_outliers = []

#             for pos, out in enumerate(list(df['Normality'])):
#                 if out == False:
#                     x_outliers.append(pos+1)
#                     y_outliers.append(list(df['New observation'])[pos])
#             plt.plot(x_list, df['New observation'])
#             plt.plot(x_list, df['Acc mean'], label='Accuracy Mean')
#             plt.fill_between(x_list,df['Acc mean']-df['Acc std'],df['Acc mean']+df['Acc std'],alpha=.3, label = 'Acc mean $\pm$ Std')

#             plt.axvline(x=293, color='grey', linestyle='--', label='Concept drift')
#             plt.text(x=295, y=0.01, s='293', fontsize= 13)
#             plt.axvline(x=793, color='grey', linestyle='--', label='Concept drift')
#             plt.text(x=795, y=0.01, s='793', fontsize= 13)

#             plt.plot(x_outliers, y_outliers, 'ro', label = 'Outlier')
#             plt.legend()
#             plt.ylabel('Accuracy')
#             plt.xlabel('Finished cases')

#             if performance_measure =='ROCAUC':
#                 performance_measure ='AUC'
#             plt.title('Realtime evaluation %s %s \n %s Mean: %s'%(datalabel, classifier,performance_measure ,counter))
#             plt.ylim(-0.05,1.05)
#             # plt.show()
#             plt.tight_layout()

#             if performance_measure =='AUC':
#                 performance_measure ='ROCAUC'
#             plt.savefig('./img/%s/%s/%s %s result%s.pdf'%(datalabel, classifier, classifier, performance_measure,counter))

#             plt.cla()
#             plt.clf()



performance_measure = 'Accuracy'
# datalabsel_list = ['synthetic_log_b', 'synthetic_log_bc1', 'synthetic_log_bc2', 'synthetic_log_bc1c2', 'bpic17', 'bpic15']
datalabsel_list = ['synthetic_log_bc1c2']#, 'synthetic_log_bc1']

figure(figsize=(12,4,))

for counter in [50,200]:
    for classifier in ['htc', 'hatc', 'efdt']:
        for datalabel in datalabsel_list:
            with open('./dataset_parameters.json','r') as json_file:
                parameters = json.load(json_file)[datalabel]
                maximum_prefix = parameters['maximum_prefix']
            for prefix in range(2, maximum_prefix+1):


                df = pd.read_csv('./img/%s/%s/%s/result%s prefix%s.csv'%(datalabel, classifier,performance_measure ,counter, prefix))
                # df50 = pd.read_csv('./result100.csv')
                x_list =[x+1 for x in df.index.values]

                x_outliers = []
                y_outliers = []

                for pos, out in enumerate(list(df['Normality'])):
                    if out == False:
                        x_outliers.append(pos+1)
                        y_outliers.append(list(df['New observation'])[pos])
                plt.plot(x_list, df['New observation'])
                plt.plot(x_list, df['Acc mean'], label='Accuracy Mean')
                plt.fill_between(x_list,df['Acc mean']-df['Acc std'],df['Acc mean']+df['Acc std'],alpha=.3, label = 'Acc mean $\pm$ Std')

                plt.axvline(x=293, color='grey', linestyle='--', label='Concept drift')
                plt.text(x=295, y=0.01, s='293', fontsize= 13)
                plt.axvline(x=793, color='grey', linestyle='--', label='Concept drift')
                plt.text(x=795, y=0.01, s='793', fontsize= 13)

                plt.plot(x_outliers, y_outliers, 'ro', label = 'Outlier')
                plt.legend()
                plt.ylabel('Accuracy')
                plt.xlabel('Finished cases')
                plt.title('Realtime evaluation %s %s \n Accuracy Mean: %s Prefix: %s'%(datalabel, classifier, counter, prefix))
                plt.ylim(-0.05,1.05)
                plt.tight_layout()
                plt.savefig('./img/%s/%s/%s/result%s prefix%s.pdf'%(datalabel, classifier, performance_measure, counter, prefix))

                plt.cla()
                plt.clf()