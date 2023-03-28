import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB

windows_path = "C:\\Users\\Admin\\Desktop\\Programowanie\\2Rok\\4Semestr\\inteligencja_obliczeniowa\\lab5\\iris.csv"

df = pd.read_csv(windows_path)

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=278830)

print(len(df))

def classify_iris(sl, sw, pl, pw):
    if sl <= 5.8 and sl >= 4.3 and sw > 2.3 and sw < 4.4 and pl >= 1.0 and pl <= 1.9 and pw >= 0.1 and pw <= 0.6:
        return("setosa")
    elif sl >= 4.9 and sl <= 7.0 and sw >= 2.0 and sw <= 3.4 and pl >= 3.0 and pl <= 5.1 and pw >= 1.0 and pw <= 1.8: 
        return("versicolor")
    elif sl >= 4.9 and sl <= 7.9 and sw >= 2.2 and sw <= 3.8 and pl >= 4.5 and pl <= 6.9 and pw >= 1.4 and pw <= 2.5:
        return("virginica")
    
good_predictions = 0
length = test_set.shape[0]

lista = df.values[100:150, 3]

lowest_value = 10
highest_value = 0

for i in range(len(lista)):
    if lista[i] < lowest_value:
        lowest_value = lista[i]
    if lista[i] > highest_value:
        highest_value = lista[i]
    
print(lowest_value)
print(highest_value)

for i in range(length):
    if classify_iris(test_set[i][0], test_set[i][1], test_set[i][2], test_set[i][3]) == test_set[i, 4]:
        good_predictions = good_predictions + 1

print(good_predictions)
print(good_predictions/length*100, "%")

clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=2, random_state=278830)
clf = clf.fit(train_set[:, 0:4], train_set[:, 4])

good_predictions = 0
length = test_set.shape[0]

for i in range(length):
    if clf.predict([test_set[i][0:4]]) == test_set[i, 4]:
        good_predictions = good_predictions + 1

y_true = test_set[:, 4]
y_pred = clf.predict(test_set[:, 0:4])

print(confusion_matrix(y_true, y_pred))

# print(good_predictions)

# print(good_predictions/length*100, "%")

clf = KNeighborsClassifier(n_neighbors=11)
clf = clf.fit(train_set[:, 0:4], train_set[:, 4])

good_predictions = 0
length = test_set.shape[0]

for i in range(length):
    if clf.predict([test_set[i][0:4]]) == test_set[i, 4]:
        good_predictions = good_predictions + 1

print(good_predictions)
print(good_predictions/length*100, "%")

y_true = test_set[:, 4]
y_pred = clf.predict(test_set[:, 0:4])

print(confusion_matrix(y_true, y_pred))

gnb = GaussianNB()

y_pred = gnb.fit(train_set[:, 0:4], train_set[:, 4]).predict(test_set[:, 0:4])

print("Number of mislabeled points out of a total %d points : %d" % (test_set.shape[0], (test_set[:, 4] != y_pred).sum()))

print(confusion_matrix(test_set[:, 4], y_pred))
