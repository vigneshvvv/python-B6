import pandas  as pd

data = ["Java", "Python", "C", "C++"]

df = pd.DataFrame(data)
df.to_csv("students.txt", index=False, header= False)
