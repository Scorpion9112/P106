import numpy as ny
import csv
import plotly.express as px

coffee=[]
sleep=[]

with open("CoffeeL.csv") as f:
  df=csv.DictReader(f)
  for i in df:
    coffee.append(float(i["Coffee in ml"]))
    sleep.append(float(i["sleep in hours"]))
  figure=px.scatter(df, x="Coffee in ml", y="sleep in hours")
  figure.show()

import numpy as np
correlation=np.corrcoef(coffee, sleep)
print(correlation[0,1])


