import pandas as pd
df = pd.DataFrame()
for i in range(22):
    df2 = pd.read_csv("./ECGmetricsV5" + str(i) + ".csv")
    df = df.append(df2)
df.to_csv("./combinedECGv5.csv")
