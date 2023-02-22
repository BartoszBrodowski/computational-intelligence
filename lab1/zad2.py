import pandas as pd
from matplotlib import pyplot as plt

# 2010,460,555,405

 
# Data of year 2010

data = {
    'Rok': [2010],
    'Gdansk': [460],
    'Poznan': [555],
    'Szczecin': [405]
}
 
# Make data frame of above data
df = pd.DataFrame(data)
 
# Add row to csv file

# df.to_csv('/home/LABPK/bbrodowski/ROK2/4semestr/AI/lab1/miasta.csv', mode='a', index=False, header=False, columns=['Rok', 'Gdansk', 'Poznan', 'Szczecin'])

# print(pd.read_csv('/home/LABPK/bbrodowski/ROK2/4semestr/AI/lab1/miasta.csv'))

# Dla Gdanska
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Gdansk", "Rok", "Poznan", "Szczecin"]
df2 = pd.read_csv("/home/LABPK/bbrodowski/ROK2/4semestr/AI/lab1/miasta.csv", usecols=columns)
print("Contents in csv file:", df2)
plt.plot(df2.Rok, df2.Gdansk)
plt.plot(df2.Rok, df2.Poznan)
plt.plot(df2.Rok, df2.Szczecin)

# plt.show()

# columns_many = ['Rok', 'Gdansk', 'Poznan', 'Szczecin']
# df_many = pd.read_csv("/home/LABPK/bbrodowski/ROK2/4semestr/AI/lab1/miasta.csv", usecols=columns_many)
# df_many.plot(df_many.Rok, df_many.Gdansk, df_many.Poznan, df_many.Szczecin)
    
plt.show()
