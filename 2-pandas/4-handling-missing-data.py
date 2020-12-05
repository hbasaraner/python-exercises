import pandas as pd

data = pd.DataFrame([[2.3, 3.3, NaN],
                     [7.5, Nan, 9.8], [NaN, 2.2., 6.8],
                     [5.6, 9.2, 7.4], [NaN, NaN, NaN]])

# 1. filtering missing data

# delete rows with null values
print(data.dropna())

# delete row with all null values
print(data.dropna(how='all'))

# 2. filling missing data

# fill null values with zero
print(data.fillna(0))

# fill null values with mean
print(data.fillna(mean(data)))

# null values for specific column
print(data.fillna({0: 2.5, 1: 3.0, 2: 5.5}))
