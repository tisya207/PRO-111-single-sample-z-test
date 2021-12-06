import statistics
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import csv
import random

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

#fig= ff.create_distplot([data],['Math_score'], show_hist=False)
#fig.show()

mean= statistics.mean(data)
std_dev = statistics.stdev(data)
print('mean of data: ',mean)
print('std dev of data: ', std_dev)


def rand_set_of_mean(counter):

    dataset=[]
    for i in range(0,counter):
        rand=random.randint(0, len(data)-1)
        value = data[rand]
        dataset.append(value)

    mean= statistics.mean(dataset)
    return mean

meanlist= []
for i in range(0,100):
    set_of_mean=rand_set_of_mean(100)
    meanlist.append(set_of_mean)

mean= statistics.mean(meanlist)
std_of_sampling_data= statistics.stdev(meanlist)
print('mean of sampling data: ',mean)
print('std dev of sampling data: ', std_of_sampling_data)

#fig = ff.create_distplot([meanlist], ["student marks"], show_hist=False) 
#fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN")) 
#fig.show()

first_std_deviation_start, first_std_deviation_end = mean-std_of_sampling_data, mean+std_of_sampling_data
second_std_deviation_start, second_std_deviation_end = mean-(2*std_of_sampling_data), mean+(2*std_of_sampling_data)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_of_sampling_data), mean+(3*std_of_sampling_data)
print("std1",first_std_deviation_start, first_std_deviation_end)
print("std2",second_std_deviation_start, second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)


#fig = ff.create_distplot([meanlist], ["student marks"], show_hist=False)
#fig.show()

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample3:- ",mean_of_sample1)
fig = ff.create_distplot([meanlist], ["reading time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 1], mode="lines", name="MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 1], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.show()

z_score = (mean - mean_of_sample1)/std_dev
print("The z score is = ",z_score)
