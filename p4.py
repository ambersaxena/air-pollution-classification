import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
data = pd.read_csv('aqifinal.csv', header=0)
print data.shape
X = data.iloc[:,0:3]
y = data.iloc[:,3:4]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.30)
print X_train.shape
print X_test.shape
#X_test=[[36,53,128],[27,80,154],[17,45,138],[24,150,80]]
#y_test=[[1],[1],[1],[0]]
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print "confusion matrix"
print (confusion_matrix)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(classifier.score(X_test, y_test)))
