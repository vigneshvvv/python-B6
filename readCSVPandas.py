import pandas as pd

df = pd.read_csv("studentDetails.csv")
# print(df)
# print(df.head())
# print(df.head(3))
# print(df.tail())

# print(df.columns)
# print(df.dtypes)
# print(df.info())
# print(df["name"])

# print(df[["name", "Department"]])

# print(df.iloc[1:4])

print(df[df["Department"] == "EEE"])

print(df.sort_values("Marks"))