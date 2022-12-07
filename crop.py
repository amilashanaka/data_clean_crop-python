import pandas as pd
#import pandas. libarary

df = pd.read_csv('bristol-air-quality-data.csv', sep=';',engine='python')
# read csv file's data in to panda's data frame

print(len(df.index))
# get the row count from the data frame

df_crop = pd.DataFrame(df[df['Date Time'] > "2010-01-01"])
# apply filter to get data older than "2010-01-01"

print(len(df_crop.index))
# get the row count from the data frame

df_crop.to_csv('crop.csv')
# save to csv file
