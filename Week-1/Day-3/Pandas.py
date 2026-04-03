import pandas as pd
# a=pd.DataFrame([10,58,65,5,8])

# print(a)

# A={
#     "Name":["Jairam","ABC","XYZ"],
#     "Age":[25,23,21],
#     "Address":["Aditi","CDS","ADS"]
# }

# df=pd.DataFrame(A)
# print(df)

df1=pd.read_csv("DataSets/StudentPerformanceFactors.csv")
# df2=pd.read_excel("DataSets/StudentPerformanceFactors.csv")

# print(df1.head())

# print(df1.tail())

# print(df1.info())

# print(df1.describe())


# a23=[1,2,5]

# myvar=pd.Series(a23,index=["x","y","z"])

# print(myvar)

# de=["hello","King","kins"]

# ds=pd.Series(de,index=["A","B","C"])



# fg={
#     "Name":["Jai","Ram","Adsd"],
#     "age":[62,69,58]
# }
# fg={"sdsds","dsfds","adfw"}
# print(fg.loc[1])
# fg1=pd.DataFrame(fg)
# print(fg1)

# ad={
#     "A":[1,2,4],
#     "b":["fsd","adfa","sf"]
# }

# dfr=pd.DataFrame(ad)
# print(dfr)
# print(dfr.loc[0])



# print(df1["Hours_Studied"])
# print(df1[df1["Sleep_Hours"]>7])

# print(df1[df1["Attendance"]>75])

# print(df1.isnull())

# print(df1.dropna())


l1=[1,23,6]
l1.append([1,6,9])
print(l1)