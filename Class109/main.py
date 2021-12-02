import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

mean=sum(dice_result)/len(dice_result)
std_deviation=statistics.stdev(dice_result)
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)

first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)

print("The mean is:",mean)
print("The mode is ",mode)
print("The median is",median)
print("The standard deviation is" ,std_deviation)

list_of_data_under_one_standard_deviation=[result for result in dice_result if result> first_std_deviation_start and result<first_std_deviation_end]
list_of_data_under_second_standard_deviation=[result for result in dice_result if result> second_std_deviation_start and result<second_std_deviation_end]
list_of_data_under_third_standard_deviation=[result for result in dice_result if result> third_std_deviation_start and result<third_std_deviation_end]

print("percentage of data that lies between one standard deviation",(len(list_of_data_under_one_standard_deviation)*100.0/len(dice_result)))
print("percentage of data that lies between two standard deviation",(len(list_of_data_under_second_standard_deviation)*100.0/len(dice_result)))
print("percentage of data that lies between three standard deviation",(len(list_of_data_under_third_standard_deviation)*100/len(dice_result)))

fig = ff.create_distplot([dice_result],["Result"],show_hist=False) 
fig.show()