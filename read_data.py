import pandas as pd

# use this to read the data file
wine_reviews = pd.read_csv("./data.csv")

# to check how big the result dataframe is
print(wine_reviews.shape)
