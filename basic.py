import pandas
import matplotlib.pyplot as plt
%matplotlib inline
dataset = pandas.read_csv('C:/Users/Dell/Downloads/international-airline-passengers.csv',usecols=[1],engine='python',skipfooter=3)
plt.plot(dataset)
plt.show()
