#import pandas
import pandas as pd

# prepare data
data = {'Name': ['John', 'Mike', 'Caleb'],
        'Age': [26, 29, 34],
        'Salary': [3200, 4500, 6000]}

obj = pd.DataFrame(data)

# prints dataframe in tabular form
print(obj)
print('\n'+'-'*6+'\n')

# prints specific column
print(obj['Salary'])
print('\n'+'-'*6+'\n')

# prints column details
print(obj.Salary)
print('\n'+'-'*6+'\n')

# prints the columns of dataframe
print(obj.columns)
print('\n'+'-'*6+'\n')

# prints data as 2d array
print(obj.values)
print('\n'+'-'*6+'\n')

# deletes row
print(obj.drop(1))
print('\n'+'-'*6+'\n')

# deletes column
print(obj.drop('Age', axis=1))
