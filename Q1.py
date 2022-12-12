import pandas

data=pandas.read_csv("data.csv")

#--------------------------------- Total impressions for the age group 30-34------------------------------------------------------#
m=(data.loc[data.age=='30-34','impressions'])
print(sum(m))


