
import numpy as np 
import pandas as pd 
import math



stdata = pd.read_csv(input())

stdata.head()




stdata.drop(['Certifications/Achievement/ Research papers','Link to updated Resume (Google/ One Drive link preferred)','link to Linkedin profile','How Did You Hear About This Internship?'],axis=1,inplace=True)



stdata.drop(['First Name','Last Name','City','State','Zip Code','DOB [DD/MM/YYYY]','Gender','Email Address',
             'Contact Number','Emergency Contact Number','College name','University Name',],axis=1,inplace=True)


degree = pd.get_dummies(stdata['Degree'],drop_first = True)
areaofstudy = pd.get_dummies(stdata['Major/Area of Study'])
year = pd.get_dummies(stdata['Which-year are you studying in?'],drop_first = True)


def rating_function(x):
    if x == "yes":
        return 1
    else:
        return 0
stdata["java"] = stdata["Have you worked core Java"].apply(rating_function)



lan = pd.get_dummies(stdata['Programming Language Known other than Java (one major)'])



def rating_function(x):
    if x == "yes":
        return 1
    else:
        return 0
stdata["sql"] = stdata["Have you worked on MySQL or Oracle database"].apply(rating_function)


def rating_function(x):
    if x == "yes":
        return 1
    else:
        return 0
stdata["oops"] = stdata["Have you studied OOP Concepts"].apply(rating_function)


def rating_function(x):
    if x == "yes":
        return 1
    else:
        return 0
stdata["py3"] = stdata["Programming Language Known other than Java (one major)"].apply(rating_function)


interest = pd.get_dummies(stdata['Areas of interest'],drop_first=True)
stdata = pd.concat([stdata,degree,areaofstudy,year,lan,interest],axis = 1)


stdata.drop(['Degree','Major/Area of Study', 'Course Type', 'Which-year are you studying in?','Areas of interest','Current Employment Status', 'Have you worked core Java',
       'Programming Language Known other than Java (one major)','Have you worked on MySQL or Oracle database',
       'Have you studied OOP Concepts','Python'],axis = 1, inplace = True)


select = pd.get_dummies(stdata['Label'],dtype = int)
stdata = pd.concat([stdata,select],axis = 1)


stdata = stdata.drop(['ineligible','Label'],axis = 1)



stdata.head()



X = stdata.drop('eligible',axis = 1) 
y = stdata['eligible']


from sklearn.model_selection import train_test_split



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)



from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler



from sklearn.svm import SVC



clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))



clf.fit(X_train, y_train)


prediction = clf.predict(X_test)







from sklearn.metrics import classification_report 
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
from sklearn.metrics import f1_score



classification_report(y_test,prediction)



f = f1_score(y_test, prediction,average = None)
print("F1 Score ::",f[0])






