import pandas as pd

solidly = pd.DataFrame(pd.read_csv("solidly.csv",index_col=0))

print(solidly)