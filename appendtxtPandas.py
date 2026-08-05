import pandas as pd

data = ["NodeJS", "ExpressJS", "GOLANG"]
new_data = pd.DataFrame(data)

new_data.to_csv("students.txt", mode="a", header=False, index=False)
print("Data append completed")