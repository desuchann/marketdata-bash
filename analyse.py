import os
import pandas as pd

# pandas formatting
pd.set_option("display.max_columns", None)
pd.options.display.float_format = '{:.2f}'.format

# file grab
rawfile = os.environ["RAWFILE"]
df = pd.read_csv(rawfile)

# 10 days worth of data only
df = df.head(10).sort_values("timestamp")

# create diff cols
l = df['close'].to_list()
diffs = [l[i+1]-l[i] for i in range(len(l)-1)]
diffs_pct = [((l[i+1] - l[i]) / l[i])*100 for i in range(len(l)-1)]
df["daily diffs"] = [0] + diffs
df["daily %age diffs"] = [0] + diffs_pct

# create summary table
summary = {'average close': df["close"].mean(),
'highest close': max(l),
'lowest close': min(l),
'avg daily diff': df["daily diffs"].mean(),
'avg daily %age diff': df["daily %age diffs"].mean(),
'max gain': max(diffs_pct),
'max loss': min(diffs_pct),
'avg volume': df["volume"].mean()}

summary_df = pd.DataFrame.from_dict(summary, orient="index", columns=["Value"])

# return and save results
symbol = os.environ["SYMBOL"]
title = f"\n*** T-10 Day Summary: {symbol} ***\n"

print(title)
print(df,'\n')
print(summary_df,'\n')

processed_path = os.environ["PROCESSEDFILE"]
summary_df.to_csv(processed_path)


