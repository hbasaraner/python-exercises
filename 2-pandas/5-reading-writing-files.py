import pandas as pd

# read csv file
data = pd.read_csv('data.csv')

# print top 5
print(data.head())

# save dataframe to a csv file
pd.DataFrame(data).to_csv('myfile.csv')
