import pandas as pd

# use this to read the data file
wine_reviews = pd.read_csv("./data.csv", index_col=0)

# Native accessors
# to check how big the result dataframe is
# print(wine_reviews.head())

# show the total dataframe
# print(wine_reviews)

# only certain columns
# print(wine_reviews.country)

# only certain columns if its dictionary we can do it with columns too
# print(wine_reviews["country"])

# also can call a certain index of that column
# print(wine_reviews["country"][0])

# indexing in pandas
# print(wine_reviews.iloc[1])
# print(wine_reviews.loc[1])

# it means first to 3 indexed data
# print(wine_reviews.iloc[:3, 0])

# it means 1 to 3 indexed data
# print(wine_reviews.iloc[1:3, 0])

# print(wine_reviews.iloc[[0, 1, 2], 0])

# print(wine_reviews.iloc[-5:])

# Label based selection
# print(wine_reviews.loc[0, "country"])

# Manipulating the index
# print(wine_reviews.set_index("country"))

# conditional selection
# print(wine_reviews.country == "US")

# print(wine_reviews.loc[wine_reviews.country == "Italy"])

# print(wine_reviews.loc[(wine_reviews.country == "Italy") & (wine_reviews.points >= 90)])

# only these data
# print(wine_reviews.loc[wine_reviews.country.isin(["Italy", "France"])])

# find not value
# print(wine_reviews.loc[wine_reviews.price.notnull()])

# assign data
wine_reviews["critic"] = "everyone"
print(wine_reviews["critic"])
