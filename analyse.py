import pandas
from datetime import datetime as dt
import numpy as np
import logging as log

today = dt.strftime(dt.today(), '%Y-%m-%d')
df = pandas.read_csv(f'./data/raw/alphavprices_{today}.csv')

df = df[:10]
l = df.to_list()

diffs = [0] + [l[i+1]-df[i] for i in range(len(l)-1)]
diffs_pct = [0] + [(l(i+1)/l[i]-1)*100 for i in range(len(l)-1)]

df.insert(6, "daily diffs", diffs)
df.insert(7, "daily diffs %age", diffs_pct)

#avgclose = np.mean(l)
#hiclose = l.max()
#loclose = l.min()
#avgdd = np.mean(diffs)
#avgdpd = np.mean(diffs_pct)
#maxgain = diffs_pct.max()
#maxloss = diffs_pct.min()
#avgvol = np.mean(df['volume']

summary = {'average close': np.mean(l),
'highest close': l.max(),
'lowest close' l.min(),
'avg daily diff': np.mean(diffs),
'avg daily %age diff': np.mean(diffs_pct),
'max gain': diffs_pct.max(),
'max loss': diffs_pct.min(),
'avg volume': np.mean(df['volume'])}

summary_df = pd.DataFrame.from_dict(summary, orient="index", columns=["Value"])

title = "\n*** T-10 Day Summary ***\n"

print(title)
log.info(title)

print(df)
log.info(df)

print(summary_df)
log.info(summary_df)

summary_df.to_csv(f"./data/processed/summary_{date}.csv")
log.info("Saved summary to csv")
