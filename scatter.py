import numpy as np					
import matplotlib.mlab as mlab   
import matplotlib.pyplot as plt 			
import seaborn as sns				
import pandas as pd
data1 = pd.read_csv("crimerate.csv", skiprows = [30, 38, 39], usecols = [5])
data2 = pd.read_csv("unemploymentrate.csv", skiprows =  [37], usecols = [4])
#df = data1.join(data2)
#datanum = data.to_records(index=False)


sns.set()
plt.scatter(data1, data2)
plt.xlabel('Unemployement Rate')
plt.ylabel('Crime Rate')
plt.show()
#sns.set()
#plt.hist2d(data1, data2)
#plt.xlabel('Unemployement Rate')
#plt.ylabel('Crime Rate')
#plt.show()

#sns.scatterplot('2015-16', 'Year - 2016 (Col.6)', data=df) 
#plt.title('Scatterplot')
#


#sns.scatterplot(x="Unemployment rate", y="Crime Rate", datalol)

			