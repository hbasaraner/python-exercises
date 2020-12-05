import pandas as pd

data = {'Name': ['John', 'Mike', 'Caleb'],
        'Age': [26, 29, 34],
        'Salary': [3200, 4500, 6000]}
data = pd.DataFrame(data)

# prints multiple statistics
print(data.describe())

# prints minimum age of employee
print(data.loc[:, 'Age'].min())
