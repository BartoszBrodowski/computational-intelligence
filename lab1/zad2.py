import pandas as pd
import scipy
from matplotlib import pyplot as plt

# 2010,460,555,405

miasta_csv = "/home/LABPK/bbrodowski/ROK2/4semestr/AI/lab1/miasta.csv"

miasta_csv_windows = r"C:\Users\Admin\Desktop\Programowanie\2Rok\4Semestr\inteligencja_obliczeniowa\lab1\miasta.csv"
 
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
df2 = pd.read_csv(r'C:\Users\Admin\Desktop\Programowanie\2Rok\4Semestr\inteligencja_obliczeniowa\lab1\miasta.csv', usecols=columns)
print("Contents in csv file:", df2)
plt.plot(df2.Rok, df2.Gdansk)
plt.plot(df2.Rok, df2.Poznan)
plt.plot(df2.Rok, df2.Szczecin)
plt.legend(["Gdansk", "Poznan", "Szczecin"], loc="upper left")

df2.Gdansk

# df['Gdansk'] = (df['Gdansk'] - df['Gdansk'].mean()) / df['Gdansk'].std()
print('------------------------')

# Standarize Gdansk column
print("Standarize Gdansk column")
print((df2['Gdansk'] - df2['Gdansk'].mean()) / df2['Gdansk'])

print("Mean of Gdansk column: ", ((df2['Gdansk'] - df2['Gdansk'].mean()) / df2['Gdansk']).mean())
print("Standard deviation of Gdansk column: ", ((df2['Gdansk'] - df2['Gdansk'].mean()) / df2['Gdansk'].std()).std())
print('------------------------')


# Standarize Poznan column
print("Standarize Poznan column")
print((df2['Poznan'] - df2['Poznan'].mean()) / df2['Poznan'])
print("Mean of Poznan column: ", ((df2['Poznan'] - df2['Poznan'].mean()) / df2['Poznan']).mean())
print("Standard deviation of Poznan column: ", ((df2['Poznan'] - df2['Poznan'].mean()) / df2['Poznan'].std()).std())
print('------------------------')

# Standarize Szczecin column
print("Standarize Szczecin column")
print((df2['Szczecin'] - df2['Szczecin'].mean()) / df2['Szczecin'])
print("Mean of Szczecin column: ", ((df2['Szczecin'] - df2['Szczecin'].mean()) / df2['Szczecin']).mean())
print("Standard deviation of Szczecin column: ", ((df2['Szczecin'] - df2['Szczecin'].mean()) / df2['Szczecin'].std()).std())
print('------------------------')

# # Normalize Gdansk column
# print("Normalize Gdansk column")
# print((df2['Gdansk'] - df2['Gdansk'].min()) / (df2['Gdansk'].max() - df2['Gdansk'].min()))
# print("Max value of Gdansk column: ", (df2['Gdansk'] - df2['Gdansk'].min()) / (df2['Gdansk'].max() - df2['Gdansk'].min()).max())
# print("Min value of Gdansk column: ", (df2['Gdansk'] - df2['Gdansk'].min()) / (df2['Gdansk'].max() - df2['Gdansk'].min()).min())
# print('------------------------')

# # Normalize Poznan column
# print("Normalize Poznan column")
# print((df2['Poznan'] - df2['Poznan'].min()) / (df2['Poznan'].max() - df2['Poznan'].min()))
# print("Max value of Poznan column: ", (df2['Poznan'] - df2['Poznan'].min()) / (df2['Poznan'].max() - df2['Poznan'].min()).max())
# print("Min value of Poznan column: ", (df2['Poznan'] - df2['Poznan'].min()) / (df2['Poznan'].max() - df2['Poznan'].min()).min())
# print('------------------------')

# # Normalize Szczecin column
# print("Normalize Szczecin column")
# print((df2['Szczecin'] - df2['Szczecin'].min()) / (df2['Szczecin'].max() - df2['Szczecin'].min()))
# print("Max value of Szczecin column: ", (df2['Szczecin'] - df2['Szczecin'].min()) / (df2['Szczecin'].max() - df2['Szczecin'].min()).max())
# print("Min value of Szczecin column: ", (df2['Szczecin'] - df2['Szczecin'].min()) / (df2['Szczecin'].max() - df2['Szczecin'].min()).min())
# print('------------------------')



# plt.show()

# columns_many = ['Rok', 'Gdansk', 'Poznan', 'Szczecin']
# df_many = pd.read_csv(miasta_csv_windows, usecols=columns_many)
# df_many.plot(df_many.Rok, df_many.Gdansk, df_many.Poznan, df_many.Szczecin)
    
# plt.show()


# scipy.stats.zscore(['Rok'])