import pandas

data=pandas.read_csv("data.csv")
m=data[(data.campaign_id>'0')]
m2=m['ad_id'].to_list()


print(m2)



