import pandas
from datetime import datetime as dt
import numpy as np
import logging as log

today = dt.strftime(dt.today(), '%Y-%m-%d')
df = pandas.read_csv(f'./data/raw/alphavprices_{today}.csv')

df = df[:10]
l = df['close'].to_list()

diffs = [0] + [l[i+1]-l[i] for i in range(len(l)-1)]
diffs_pct = [0] + [(l[i+1]/l[i]-1)*100 for i in range(len(l)-1)]

df.insert(6, "daily diffs", diffs)
df.insert(7, "daily %age diffs", diffs_pct)

#avgclose = np.mean(l)
#hiclose = max(l)
#loclose = min(l)
#avgdd = np.mean(diffs)
#avgdpd = np.mean(diffs_pct)
#maxgain = diffs_pct.max()
#maxloss = diffs_pct.min()
#avgvol = np.mean(df['volume']

summary = {'average close': np.mean(l),
'highest close': max(l),
'lowest close': min(l),
'avg daily diff': np.mean(diffs[1:]),
'avg daily %age diff': np.mean(diffs_pct[1:]),
'max gain': max(diffs_pct[1:]),
'max loss': min(diffs_pct[1:]),
'avg volume': np.mean(df['volume'])}

summary_df = pandas.DataFrame.from_dict(summary, orient="index", columns=["Value"])

title = "\n*** T-10 Day Summary ***\n"

print(title)
log.info(title)

print(df,'\n')
log.info(df)

print(summary_df,'\n')
log.info(summary_df)

summary_df.to_csv(f"./data/processed/summary_{today}.csv")
log.info("Saved summary to csv")
