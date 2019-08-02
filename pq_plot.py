import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

datasets = [[pd.DataFrame(),"specific"], [pd.DataFrame(),"specific-0001"], [pd.DataFrame(),"entrap"], [pd.DataFrame(), "pan"]]

for ix in range(len(datasets)):
    datasets[ix][0] = pd.read_csv(datasets[ix][1] + ".out", sep = "\t")
    datasets[ix][0]["Identified"] = range(1,datasets[ix][0].shape[0]+1)

fig, ax = plt.subplots()
for df,name in datasets:
    sns.lineplot(x="q-value",y="Identified", estimator = None, data=df, lw=1, ax=ax, label=name)
plt.xlim(0,0.1)
plt.ylim(0,500000)
plt.savefig('pq_plot.png')
plt.show()
