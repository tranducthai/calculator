import pandas as pd
import numpy as np
data=pd.read_csv('C:/Users/thispc/Downloads/creditcard/creditcard.csv')
dataset=data[:5000]
from sklearn.model_selection import train_test_split
datatrain,datatest=train_test_split(dataset,test_size=0.3)
x_train=datatrain[['V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount']]
y_train=datatrain['Class']
x_test=datatest[['V1','V2','V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28','Amount']]
y_test=datatest['Class']
from sklearn.svm import SVC
model=SVC(kernel='linear')
model.fit(x_train,y_train)
from sklearn.metrics import accuracy_score
pre=model.predict(x_test)
print(accuracy_score(pre,y_test))