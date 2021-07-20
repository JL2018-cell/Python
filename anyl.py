import pickle
import pandas as pd
from scipy.stats import gmean
import datetime
from datetime import timedelta



#Load data
data = pickle.load(open('data_test.pickle', "rb" ))
#Convert pickle file to pandas DataFrame.
data_pd = pd.read_pickle('data_test.pickle') 



#----Q.1----#
#Idea of Q.1: Use python's Built-in function to calculate pecentage change.
#Calculate daily percentage change of portfolio value.
pct_Chg_data = data_pd['strategy']['value'].pct_change()
pct_Chg_data.columns = {'Daily return'} #Rename name of column

print('----Q.1----')
print(pct_Chg_data.dropna(),'\n\n')



#----Q.2----#
#Idea of Q.2: Calculate Geometric mean and variance of return each year. Geometric mean and variance can be calculated using Python's built-in function.
print('----Q.2----')
#Add 1 to each daily return datum, which is used to prepare calculaing geometric mean.
tmp_data = pct_Chg_data.apply(lambda x: x + 1)
tmp_data = tmp_data.dropna() #Drop data that are NAN.

#Start calculating mean return from the most recent years.
#Format of End_date_Stamp = Pandas TimeStamp
End_date_Stamp = data_pd['return_data'].index[len(data_pd['return_data']) - 1]

#Emulate a do While loop in Python
while (1):
 #Start_date (Format: Python DateTime) = Start_date_Stamp (Format: Pandas TimeStamp) = 1 year earlier than End_date_Stamp.
 #Start_date = Start date of a year, End_date_Stamp = end date of the same year, e.g. Start_date = 1st Jan 2020, End_date_Stamp = 1st Jan, 2021
 Start_date = End_date_Stamp.to_pydatetime()
 Start_date = Start_date - timedelta(days = 365)
 Start_date_Stamp = pd.to_datetime(Start_date)

 #Selects dates that are within the range from Start_date_Stamp to End_date_Stamp.
 OneYr_dates = list(filter(lambda x: x > Start_date_Stamp and x <= End_date_Stamp, data_pd['return_data'].index))

 #Use Python's built-in function to calculate Geometric mean of return.
 print("Annualized mean return from", Start_date_Stamp, "to", End_date_Stamp, "\n=", gmean(tmp_data.loc[OneYr_dates,'Daily return']) - 1)
 #Use Python's built-in function to calculate variance of return.
 print("Annualized volatility (Variance) from", Start_date_Stamp, "to", End_date_Stamp, "\n=", tmp_data.loc[OneYr_dates,'Daily return'].cov(tmp_data.loc[OneYr_dates,'Daily return'])) #Sample Variance of return

 #Shift timeframe of calculating return statistics to 1 year earlier.
 End_date_Stamp = Start_date_Stamp
 #The loop ends if most N years of data are calculated. N = round down number of years of data available to nearest integer.
 if (Start_date_Stamp.to_pydatetime() - (data_pd['return_data'].index[0]).to_pydatetime() < timedelta(365)):
  break

print('\n\n')



#----Q.3----#
#Idea of Q.3: Calculate accumulated return between the dates when weights have records. Then, calculate weight.
#Note that timeframe of 'return_data' and 'weight' does not match. So, only their common timeframe is considered.
#Also, the time frequency of 'return_data' and 'weight' does not match. So, calculate new weight w_i_t+L for stock i at time t+L using w_i_t and return data from day t+1 to t+L. L = number of days between adjacent 2 rows in data 'weight'.

#Replace all NAN in 'return_data' with 0.
data_pd['return_data'].fillna(0)

#common_cols is a list collecting common stocks stored in data 'weight' and 'return_data'.
common_cols = list(set(data_pd['strategy']['weight'].columns) & set(data_pd['return_data'].columns))
#common_rows is a list collecting common dates stored in data 'weight' and 'return_data'.
common_rows = list(set(data_pd['strategy']['weight'].transpose().columns) & set(data_pd['return_data'].transpose().columns))
common_rows = sorted(common_rows)
return_data = data_pd['return_data'].fillna(0) #Replace NAN with 0.

#Setup a empty pandas DataFrame with called 'final_weight' to hold result of Q.3.
final_weight = pd.DataFrame(columns = common_cols)

for i in range(1,len(common_rows)):
 #tmp_data is a DataFrame holding return data from time t+1 to t+L. L = number of days between adjacent 2 rows in data 'weight'.
 tmp_data = return_data.loc[common_rows[i - 1]:common_rows[i],:]
 #Add 1 to each datum. This prepares calculating cumulative return form time t+1 to t+L.
 tmp_data = tmp_data.apply(lambda x: x + 1)

 #Calculate new weight after return. In this case, total weight of all stocks > 1. This is not the final answer.
 weight = data_pd['strategy']['weight'].loc[common_rows[i - 1],common_cols].multiply(tmp_data.loc[common_rows[i - 1]:common_rows[i],common_cols].product())
 #Calculate val = total weight of all stocks.
 val = data_pd['strategy']['weight'].loc[common_rows[i - 1],common_cols].dot(tmp_data.loc[:,common_cols].product())
 #Adjust weight of each stock by being divided with total weight (val) such that the sum of weight = 1.
 weight.div(val)
 final_weight.loc[common_rows[i - 1]] = weight

#Show final answer
print('----Q.3----')
print(final_weight, '\n\n')



#----Q.4----#
#Idea of Q.4: Collect the most recent 6 months data, Then, use Python's built-in function to calculate covariance matrix of 6 months data.
#"str_date" calculates date that is 6 months ago from the most recent date shown in data.
str_date = pd.to_datetime(data_pd['return_data'].index[len(data_pd['return_data'].index) - 1].to_pydatetime() + timedelta(days = -180))

#SixMth_dates is a list, holding all dates shown in data that are with recent 6 months.
SixMth_dates = list(filter(lambda x: x >= str_date, data_pd['return_data'].index))

print('----Q.4----')
#Call Python's built-in function to calculate covariance matrix
print(data_pd['return_data'].loc[SixMth_dates].cov(), '\n\n')














