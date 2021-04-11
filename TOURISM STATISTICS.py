import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Tourism.csv")
df["Domestic Growth Rate"]=((df["Domestic - 2017-18"]-df["Domestic - 2016-17"])/(df["Domestic - 2016-17"]))*100
df["Foreign Growth Rate"]=((df["Foreign - 2017-18"]-df["Foreign - 2016-17"])/(df["Foreign - 2016-17"]))*100
print(df.drop(df[(df["Domestic Growth Rate"]>100)|(df["Foreign Growth Rate"]>100)].index))
df.drop(df[(df["Name of the Monument"]=="Total")|(df["Name of the Monument"]=="Grand Total")].index,inplace=True)
circles=df["Circle"].unique().tolist()
circlesgrp=df.groupby("Circle")
circle_data=[circlesgrp.get_group(x) for x in circles]
hdomestic_data=[print(circle_data[x].loc[circle_data[x]["Domestic Growth Rate"]==circle_data[x]["Domestic Growth Rate"].max()]) for x in range(0,len(circle_data))]
ldomestic_data=[print(circle_data[x].loc[circle_data[x]["Domestic Growth Rate"]==circle_data[x]["Domestic Growth Rate"].min()]) for x in range(0,len(circle_data))]
hforeign_data=[print(circle_data[x].loc[circle_data[x]["Foreign Growth Rate"]==circle_data[x]["Foreign Growth Rate"].max()]) for x in range(0,len(circle_data))]
lforeign_data=[print(circle_data[x].loc[circle_data[x]["Foreign Growth Rate"]==circle_data[x]["Foreign Growth Rate"].min()]) for x in range(0,len(circle_data))]
pos=np.arange(len(circles))
hdomgr=[circle_data[x]["Domestic Growth Rate"].max() for x in range(0,len(circle_data))]
ldomgr=[circle_data[x]["Domestic Growth Rate"].min() for x in range(0,len(circle_data))]
hforgr=[circle_data[x]["Foreign Growth Rate"].max() for x in range(0,len(circle_data))]
lforgr=[circle_data[x]["Foreign Growth Rate"].min() for x in range(0,len(circle_data))]
plt.bar(pos,hdomgr,color="r",width=0.2)
plt.bar(pos+0.2,ldomgr,color="b",width=0.2)
plt.xticks(pos,circles)
plt.xlabel("Circles")
plt.ylabel("Domestic Growth Rate")
plt.legend(["Highest","Least"])
plt.show()
plt.bar(pos,hforgr,color="r",width=0.2)
plt.bar(pos+0.2,lforgr,color="g",width=0.2)
plt.xticks(pos,circles)
plt.xlabel("Circles")
plt.ylabel("Foreign Growth Rate")
plt.legend(["Highest","Least"])
plt.show()
