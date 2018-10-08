#importing necessary library files: numpy matplotlib pandas					
import matplotlib.mlab as mlab   
import matplotlib.pyplot as plt 			
import seaborn as sns				
import pandas as pd
# reading the csv files
cr = pd.read_csv('crimerate.csv', skiprows =[30,38,39], usecols = [5]) 
un = pd.read_csv('unemploymentrate.csv',skiprows =[37], usecols = [4])

un1 = un.to_records(index=False) #Converting Dataframe into NumPy array
cr1 = cr.to_records(index=False) #Converting Dataframe into NumPy array

#calculating the mean of crime rate
sum2 = 0  # defining 0 initial sum
i = 0   # defining 0 index
for i in range(len(cr1)):   #running for loop to find the sum of all the state's crime rate
    sum2= sum2 + cr1[i][0]  # taking crime rate column of cr1 and summing up
    i = i+1     #increasing the index by 1 in each iteration
mean_cr = sum2/len(cr1)  # mean = sum(all no)/ sample size
print(mean_cr) #printing mean
#finding variance of crime rate
for i in range(len(cr1)):  #running for loop to find the variance of all the state's crime rate
    var1= ((cr1[i][0] - mean_cr)**2)/(len(cr1)-1)  # the variance =( x - x_mean)/(sample size -1)
    i = i+1  #increasing the index by 1 in each iteration
print(var1)  # printing variance
std1 = var1**0.5  # standard deviation = var^(1/2)
print std1   # printing  std

#calculating the mean of crime rate
sum1 = 0    # defining 0 initial sum
i = 0   # defining 0 index
for i in range(len(un1)):  #running for loop to find the sum of all the state's crime rate
    sum1= sum1 + un1[i][0]   # taking unemp rate column of cr1 and summing up
    i = i+1   #increasing the index by 1 in each iteration
mean = sum1/len(un1) # mean = sum(all no)/ sample size
print(mean) #printing mean
#finding variance of unemp rate
for i in range(len(un1)):  #running for loop to find the variance of all the state's crime rate
    var= ((un1[i][0] - mean)**2)/(len(un1)-1)  # the variance =( x - x_mean)/(sample size -1)
    i = i+1   #increasing the index by 1 in each iteration
print(var)  # printing variance
std = var**0.5 # standard deviation = var^(1/2)
print std # printing  std

ls = np.zeros((len(un1)),order='C')  # creating one array of same length as un1
ls.tolist()    # converting ls to list
for i in range(len(un1)):  #taking the valies of un1 to the list ls
    ls[i]= un1[i][0]  #the (i,0) th data is needed
    i = i +1  #increasing the index by 1 in each iteration
print ls  # printing ls

cr2 = np.zeros((len(cr1)),order='C')  # creating one array of same length as cr1
cr2.tolist()    # converting cr2 to list
for i in range(len(un1)):  #taking the valies of cr1 to the list cr2
    cr2[i]= cr1[i][0]    #the (i,0) th data is needed
    i = i +1    #increasing the index by 1 in each iteration
print cr2    # printing cr2
#the correlation relation
i = 0 #setting index value 0

for i in range(len(un1)): #initiating for loop
    cor= ((un1[i][0] - mean))*((cr1[i][0] - mean_cr))/(len(cr1)-1) # correlation formula is written
    i = i+1  #increasing the index by 1 in each iteration
print(cor) #printing correlation
i = 0  #setting index value 0
den = abs(cor)/(std*std1)  # correlation density formula^2
density = den**0.5 # correlation density formula
print(density)  #printing density
plt.hist(ls,histtype='step', label="unemployment rate") #plotting 1d histogram for unemployment rate

plt.ylabel("No of states ") #giving y label
plt.xlabel('Unemployment rate') # giving x label
Mean= mean  #taking the mean valuer calculated 
standad_dev = std #taking the std valuer calculated 
plt.axvline(Mean, label="Mean", lw=1, ls='dashed') # the mean will be shown by a dashed vertical line 
plt.axhline(standad_dev, label="Standard deviation", lw=1) # the std will be shown by a  horizontal line 
plt.title('Histogram of unemployment rate ') # writing the title of plot
plt.legend() #showing legend
plt.show() #show the plot
plt.hist(cr2, histtype='step', label="Crime rate")  #plotting 1d histogram forcrime rate
plt.ylabel("Number of states")#giving y label
plt.xlabel('Crime rate')#giving x label
Mean1= mean_cr #taking the mean valuer calculated 
standard_dev = std1 #taking the std valuer calculated 
plt.axvline(Mean1, label="Mean", lw=1, ls='dashed') # the mean will be shown by a dashed vertical line 
plt.axvline(standard_dev, label="Standard deviation", lw=1)# the std will be shown by a  vertical line
plt.title(r'Histogram for Crime rate')#showing title
plt.legend()#showing legend
plt.show()#show the plot
data1 = pd.read_csv('crimerate.csv', skiprows =[30,38,39], usecols = [5]) # taking the data by pandas
data2 = pd.read_csv('unemploymentrate.csv',skiprows =[37], usecols = [4])  # taking the data by pandas

plt.scatter(data1, data2)  #scatter plot
plt.xlabel('unemployment rate') # giving x label
plt.ylabel('Crime rate') # giving y label
plt.show() #show the plot
ls1 = np.asarray(ls) #converting list to numpy array
cr3 = np.asarray(cr2) #converting list to numpy array
plt.hist2d(cr3,  ls1)  #plotting 2d histogram for unemployment rate and Crime rate
plt.colorbar() # showing colorbar
plt.title(r'2D Histogram for unemployment and Crime rate')#showing title
plt.xlabel('unemployment rate') # giving x label
plt.ylabel('Crime rate')# giving y label
plt.show() #show the plot
			
