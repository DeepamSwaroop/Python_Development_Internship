import pandas

data=pandas.read_csv("data.csv")
#---------------------------------  total clicks where report_start between dates 19/08/2017 to 22/08/2017------------------------------------------------------#
m=data[(data.reporting_start>'18/08/2017') & (data.reporting_start<'23/08/2017')]
m2=m['clicks'].tolist()


print(sum(m2))

