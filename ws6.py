import pandas as pd

print(pd.__version__)
df = pd.DataFrame({"Name":["Alice","Bob","Charlie"],"Age":[25,30,35],"City":["New York","Los Angeles","Chicago"]})
print(df)

s1 = pd.Series([100,200,300,400,500])
print(s1)
print(s1.iloc[1], s1.iloc[3])

s2 = pd.Series([10,20,30,40,50])
print(s1 + s2)

print(df[["Name","City"]])
df["Salary"] = [50000,60000,70000]
print(df)
print(df["Age"].mean(), df["Salary"].sum())

print(df[df["Age"]>28])
df2 = df.set_index("Name")
print(df2)
df2 = df2.reset_index()
print(df2)

import io
csv = io.StringIO("""Name,Department,Salary
John,Sales,50000
Jane,Marketing,60000
Emily,HR,55000
""")
emp = pd.read_csv(csv)
print(emp)
print(emp[emp["Salary"]>55000][["Name","Department"]])

grp = emp.groupby("Department")["Salary"].mean()
print(grp)
agg = emp.groupby("Department")["Salary"].agg(["min","max"])
print(agg)

df1 = pd.DataFrame({'Name':['John','Jane','Emily'],'Department':['Sales','Marketing','HR']})
df2 = pd.DataFrame({'Name':['John','Jane','Emily'],'Experience (Years)':[5,7,3]})
merged = df1.merge(df2,on="Name")
print(merged)
print(merged.sort_values("Experience (Years)",ascending=False))
