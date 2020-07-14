import seaborn as sns
df=sns.load_dataset('iris')

df.shape

#checking co-relation
df.corr()

#represent co_relation in graphical format
sns.pairplot(df)

