#dataframe example df

import pandas as pd

data = {"name": ["kanika", "rizul", "veda"]
        , "age": [18, 19, 18]
        }

df = pd.DataFrame(data, index =["employee1", "employee2", "employee3"])

#add a new column
df["job"] = ["cashier", "N/A", "cook"]

#add a new row
new_row = pd.DataFrame([{"name": "aradhya", "age": 18, "job": "intern"}], 
                       index=["employee4"])
df = pd.concat([df, new_row])

print(df)


