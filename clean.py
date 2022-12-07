import pandas as pd
import numpy as np

df = pd.read_csv("crop.csv",engine='python')
# read csv file's data in to panda's data frame

station = {
    188: "AURN Bristol Centre",
    203: "Brislington Depot",
    206: "Rupert Street",
    209: "IKEA M32",
    213: "Old Market",
    215: "Parson Street School",
    228: "Temple Meads Station",
    270: "Wells Road",
    271: "Trailer Portway P&R",
    375: "Newfoundland Road Police Station",
    395: "Shiner's Garage",
    452: "AURN St Pauls",
    447: "Bath Road",
    459: "Cheltenham Road \ Station Road",
    463: "Fishponds Road",
    481: "CREATE Centre Roof",
    500: "Temple Way",
    501: "Colston Avenue",
}
#create data dictionary for station name and station ID  

print(len(df.index))
#get number of rows before clean 

df = df[df['Location'].isin(station.values())]
#validate station name with station ID

print(len(df.index))
#get number of rows 

df = df[df['SiteID'].isin(station.keys())]
#validate station iD with station name

print(len(df.index))
#get number of rows 


df['Location'] = np.where((df['Location'] == [station[k] for k in df['SiteID'] if k in station]), df['Location'], 'NaN')

# Set NaN values to Location Names which does not correspond to station ID 
            


df = df.loc[df['Location'] != 'NaN']
# drop rows which station name having NaN values

print(len(df.index))
#get number of rows 

df.to_csv('clean.csv')
#convert filtered data to CSV 