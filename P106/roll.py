import numpy as ny
import csv
import plotly.express as px
marks=[]
attendance=[]

with open("Roll.csv") as f:
  df=csv.DictReader(f)
  for i in df:
    marks.append(float(i["Marks In Percentage"]))
    attendance.append(float(i["Days Present"]))
  #figure=px.scatter(df, x="Days Present", y="Marks In Percentage")
  #figure.show()

import numpy as np
correlation=np.corrcoef(marks, attendance)
print(correlation[0,1])
