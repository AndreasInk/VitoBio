import pandas as pd
import numpy as np
import heartpy as hp
import matplotlib.pyplot as plt
df = pd.read_csv("./ECG4.txt")
df2 = pd.DataFrame()
i = 0
for data in np.array_split(df, len(df.index)/15366.0):
    sample_rate = 250
    try: 
        data = list(pd.DataFrame(data).Values)

    # plt.figure(figsize=(12,4))
    # plt.plot(data)
    # plt.show()

        wd, m = hp.process(data, sample_rate)

        #visualise in plot of custom size
        plt.figure(figsize=(12,4))
        hp.plotter(wd, m)

        #display computed measures

        for measure in m.keys():
            print('%s: %f' %(measure, m[measure]))
            try: 
                df2[str(measure)].append([m[measure]], ignore_index=True)
            except:
                df2[str(measure)] = [m[measure]]
                df2.to_csv("./ECGmetricsV5" + str(i) + ".csv")
        i += 1
           
    except:
        print(1)

