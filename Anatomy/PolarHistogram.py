#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#this code creates a (normalized) mean polar histogram with the data from the first sheet of a given Excel file. It takes the first row for column names and there have to be 'numberofdatapoints' datapoints in each row.

#setup
filename = 'MeanPolarHistogramAxonCell33_88rotated.xlsx'
color = 'red' #color of histogram bars
savediagram = "diagramname.svg" #if only a name is given, file will be saved in current working directory
numberofdatapoints = 36 #number of datapoints
normalize = 0 # 1 if you want to normalize, 0 if not

def readfile(filename):
    #read in excel sheet as dataframe
    return pd.read_excel(filename)
    

def degtorad():
    #calculate radians for dataframe of degrees
    listDeg = np.arange(0, 360, 10).tolist()
    dfDeg = pd.DataFrame(listDeg, columns=['Degrees'])
    #return (((dfDeg.Degrees-180)/180)*np.pi) #if the original tracing is turned by 180 degrees (EC on the right side of the Alveus)
    return ((dfDeg.Degrees/180)*np.pi) #use this if tracing was done with EC to the left of the alveus

def renamecolumnswithnumbers():
    #get rid of the individual names (CellIDs) and numbers the columns
    numberofcolumns = df.count(axis=1) [0] #defines the number of columns
    newcolumnnames = np.arange(0, numberofcolumns, 1) #creates an array with as many increasing columns as there are numbers
    df.columns = [newcolumnnames] #renames the columns with the created array
    return numberofcolumns

def calculatepercentage():
    #transforms the dataframe to percentages of axonal/dendritic direction of the regarding neuron
    for i in range (numberofcolumns):
        total = df.sum(axis=0) [i] #calculates the total value of lenght for each column/individualneuron
        df[i] = df.div(total)*100 #calculates the percentage

# read in Excel sheet in
df = readfile(filename)

# create dataframe "radians" of degrees to get the exact x value of the bars
radians = degtorad()

# calculate the percentage of each direction of each cell and then build the mean percentage of those new values
numberofcolumns = renamecolumnswithnumbers()
if normalize == 1:
    calculatepercentage() #use this function only for the normalized histogram

# get mean over each row. This is the average for that direction and will be the bar lenght
length = df.mean(axis=1)

# draw plot
width = (2*np.pi) / numberofdatapoints #width of bars depends on number of datapoints (36) and gets calculated
ax = plt.subplot(111, projection='polar') #sets up polar axis
bars = ax.bar(radians, length, width=width, bottom=0.0, color=color, edgecolor='black', linewidth=0.25, align='edge') #defines bars
ticks_x = (((np.arange(0, 360, 30))/180)*np.pi) #sets ticks ever 30 degrees
plt.xticks(ticks=ticks_x, labels=['0','', '60','','120','','180','','240','','300','']) #labels every second tick
plt.plot()

#savesfile as .svg
plt.savefig(savediagram)

# %%
