import pandas as pd

data = {'Name': ['John', 'Mike', 'Caleb'],
        'Age': [26, 29, 34],
        'Salary': [3200, 4500, 6000]}

# gives specified indexing to rows
data = pd.DataFrame(data, index=['emp1', 'emp2', 'emp3'])
print(data)

# indexing format
# data[rows, columns]

# - Column Selection -

# known column name
print(data[['Age', 'Name']])
print(data.loc[:, ['Age', 'Name']])

# unknown column name
print(data.iloc[:, [0, 1]])

# - Row Selection -

# known index
print(data.loc['emp1':'emp2', :])

# unknown index
print(data.iloc[0:2, :])

# filter data
print(data.loc[data.Age > 30, ['Name', 'Salary']])
