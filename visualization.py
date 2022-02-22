import matplotlib

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd

datalabsel_list = ['synthetic_log_b', 'synthetic_log_bc1', 'synthetic_log_bc2', 'synthetic_log_bc1c2', 'bpic17', 'bpic15']
# classifier = 'htc'
# counter = 200

for counter in [50,100,200]:
    for classifier in ['htc', 'hatc', 'efdt']:
        for datalabel in datalabsel_list:

            df = pd.read_csv('./img/%s/%s result%s.csv'%(datalabel, classifier, counter))
            # df50 = pd.read_csv('./result100.csv')
            x_list =[x+1 for x in df.index.values]

            x_outliers = []
            y_outliers = []

            for pos, out in enumerate(list(df['Normality'])):
                if out == False:
                    x_outliers.append(pos+1)
                    y_outliers.append(list(df['New observation'])[pos])
            figure(figsize=(12,8,))
            plt.plot(x_list, df['New observation'])
            plt.plot(x_list, df['Acc mean'], label='Accuracy Mean')
            plt.fill_between(x_list,df['Acc mean']-df['Acc std'],df['Acc mean']+df['Acc std'],alpha=.3, label = 'Acc mean $\pm$ Std')

            # plt.plot(x_list, df['Acc mean']+df['Acc std'], 'Acc Mean + Std')
            # plt.plot(x_list, df['Acc mean']-df['Acc std'], 'Acc Mean - Std')
            plt.plot(x_outliers, y_outliers, 'ro', label = 'Outlier')
            plt.legend()
            plt.ylabel('Accuracy')
            plt.xlabel('Finished cases')
            plt.title('Realtime evaluation %s %s \n Accuracy Mean: %s'%(datalabel, classifier, counter))
            plt.ylim(0.3,1.05)
            # plt.show()
            plt.savefig('./img/%s/%s result%s.png'%(datalabel, classifier, counter))

            plt.cla()
            plt.clf()