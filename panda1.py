
import pandas as pd 

# data[10, 20, 30, 40, 49]
 #series = pd.Series(data, index=["a", "b", "c", "d", "e"])
#series.loc["c"] = 200
 #print(series[series >= 30])
# print(series.iloc[1]) # interger location based indexing
#print(series.loc["c"]) # label based indexing

# now with dictonary

calories = {"day 1": 1750, "day 2": 1800, "day 3": 2000}
series = pd.Series(calories)
print(series.loc["day 2"])

