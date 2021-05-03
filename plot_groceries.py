import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import csv

# https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
# https://datatofish.com/integers-datetime-pandas-dataframe/
# https://stackoverflow.com/questions/15910019/annotate-data-points-while-plotting-from-pandas-dataframe
# https://matplotlib.org/stable/tutorials/text/text_intro.html

d = pd.read_csv('groceries_data.csv')
df = pd.DataFrame(data=d)
df.columns=df.columns.str.strip()
dateformat = "%Y%m%d"

#print(df)

df.sort_values(by=['date'], inplace=True)

df['date'] = pd.to_datetime(df['date'], format=dateformat)

print('formatted dates')
print(df)

ax = df.set_index('date')['val'].plot(style='o')

# ** may need some separate variables for this plotting, so it
# doesn't follow the date axes cause those are messing it up
for i, point in df.iterrows():
    ax.text(point['date'], point['val'], str(point['store']))

#df.plot(kind='scatter', x='date', y='val', color='red')
plt.show()

