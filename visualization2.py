import pandas as pd 
from matplotlib.pyplot import figure
import pandas as pd
import matplotlib.pyplot as plt


# datalabsel_list = ['synthetic_log_b', 'synthetic_log_bc1', 'synthetic_log_bc2', 'synthetic_log_bc1c2', 'bpic17', 'bpic15']
datalabsel_list = ['synthetic_log_bc1c2']#, 'synthetic_log_bc1']
performance_measure = 'Accuracy'

# classifier = 'htc'
# counter = 200
figure(figsize=(12,4,))

for counter in [200]:
    for datalabel in datalabsel_list:
        for classifier in ['htc','hatc','efdt']:


            df = pd.read_csv('./img/%s/%s/%s %s result%s.csv'%(datalabel, classifier,classifier ,performance_measure ,counter))
            # df50 = pd.read_csv('./result100.csv')
            x_list =[x+1 for x in df.index.values]

            x_outliers = []
            y_outliers = []

            for pos, out in enumerate(list(df['Normality'])):
                if out == False:
                    x_outliers.append(pos+1)
                    y_outliers.append(list(df['New observation'])[pos])
            plt.plot(x_list, df['New observation'], label = classifier)
            # plt.plot(x_list, df['Acc mean'], label='Accuracy Mean')
            plt.fill_between(x_list,df['Acc mean']-df['Acc std'],df['Acc mean']+df['Acc std'],alpha=.3, label = 'Acc mean $\pm$ Std')

            color_cls_dict={'htc':'blue', 'hatc':'orange','efdt':'green'}
            plt.plot(x_outliers, y_outliers, 'o', color = color_cls_dict[classifier], label = '%s Outlier'%(classifier))

        plt.axvline(x=293, color='grey', linestyle='--', label='Concept drift')
        plt.text(x=295, y=0.01, s='293', fontsize= 13)
        plt.axvline(x=793, color='grey', linestyle='--', label='Concept drift')
        plt.text(x=795, y=0.01, s='793', fontsize= 13)

        plt.legend()
        plt.ylabel('Accuracy')
        plt.xlabel('Finished cases')

        if performance_measure =='ROCAUC':
            performance_measure ='AUC'
        plt.title('Realtime evaluation %s %s \n %s Mean: %s'%(datalabel, classifier,performance_measure ,counter))
        plt.ylim(-0.05,1.05)
        # plt.show()
        plt.tight_layout()

        if performance_measure =='AUC':
            performance_measure ='ROCAUC'
        # plt.savefig('./img/%s/%s/%s %s result%s.pdf'%(datalabel, classifier, classifier, performance_measure,counter))
        plt.show()
        plt.cla()
        plt.clf()