import time
import numpy as np 
import pandas as pd 
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import math

with PdfPages('visualization-output.pdf') as pdf:
    stdata = pd.read_csv(input())
    stdata.head(10)
    
    plt.rc('text', usetex=False)
    fig = plt.figure(figsize=(13,10))
    chart = sns.countplot(x = "Areas of interest", data = stdata)
    plt.title("The number of students applied to different technologies.")
    txt = 'Visualization Graphs'
    plt.text(0.35,0.95,txt, transform=fig.transFigure, size=24)
    plt.xticks(
        rotation=30, 
        horizontalalignment='right',
        fontweight='light',
        fontsize='medium'  
    )
    pdf.savefig()
    


    plt.rc('text', usetex=False)
    plt.figure(figsize=(13,10))
    chart = sns.countplot(x = "How Did You Hear About This Internship?", data = stdata)
    plt.title("The different ways students learned about this program")
    plt.xticks(
        rotation=35, 
        horizontalalignment='right',
        fontweight='light',
        fontsize='medium'  
    )
    pdf.savefig()
    #pdf.close()
    
    plt.rc('text', usetex=False)
    fig = plt.figure(figsize=(13,7))
    chart = sns.countplot(x = "Which-year are you studying in?", hue = "Major/Area of Study", data = stdata)
    plt.title("Year-wise and area of study wise classification of students.")
    plt.xticks(
        rotation=0,
        horizontalalignment='right',
        fontweight='light',
        fontsize='medium'  
    )
    pdf.savefig(fig)
    #pdf.close()
    
    plt.rc('text', usetex=False)
    fig = plt.figure(figsize=(15,25))
    chart = sns.countplot(x = "College name",data = stdata)
    chart.set_title('College wise classification of students')
    plt.xticks(
        rotation=42, 
        horizontalalignment='right',
        fontweight='light',
        fontsize='small'  
    )
    pdf.savefig(fig)
    #pdf.close()
    
    plt.rc('text', usetex=False)
    fig = plt.figure(figsize=(13,7))
    chart1 = sns.countplot(x = "City",data = stdata)
    chart1.set_title('City wise classification of students')
    plt.xticks(
        rotation=0, 
        horizontalalignment='center',
        fontweight='light',
        fontsize='x-large'  
    )
    pdf.savefig(fig)
    #pdf.close()
    
    ln = pd.get_dummies(stdata['Programming Language Known other than Java (one major)'],dtype = int, drop_first=True)

    stdata = pd.concat([stdata,ln],axis = 1)

    stdata.drop(['C','C#','C++','HTML/CSS','JavaScript','PHP'],axis=1,inplace=True)


    stdata['Python'] = (stdata['Python'] == True ).astype(int)

    dt = stdata[stdata["Areas of interest"] == "Data Science "]
    s = dt["Python"]
    
    plt.rc('text', usetex=False)
    fig = plt.figure(figsize=(13,5))
    chart = sns.countplot(x = s, hue ="Python", data = stdata)
    chart.set_title('Students apllied for data science')

    plt.xticks(
        rotation=0,
        horizontalalignment='right',
        fontweight='light',
        fontsize='x-large'  
    )
    pdf.savefig(fig)
    #pdf.close()



    yr = pd.get_dummies(stdata['Which-year are you studying in?'],dtype = int, drop_first=True)

    stdata = pd.concat([stdata,yr],axis = 1)

    stdata.drop(['Second-year','Third-year'],axis=1,inplace=True)



    dt = stdata[stdata["Fourth-year"] == 1]
    y1 = dt["Fourth-year"]
    def rating_function(x):
        if x > 8.0:
            return "yes"
        else:
            return "No"
    stdata["CGPA >8"] = stdata["CGPA/ percentage"].apply(rating_function)



    plt.rc('text', usetex=False)
    fig = plt.figure(figsize=(13,5))
    chart = sns.countplot(x = y1, hue ="CGPA >8", data = stdata)
    chart.set_title('Fourth year students')
    chart.set_xticklabels([''])
    plt.xticks(
        rotation=0,
        horizontalalignment='right',
        fontweight='light',
        fontsize='x-large'  
    )
    pdf.savefig(fig)
    #pdf.close()

    #Rate your verbal communication skills [1-10]
    yr = pd.get_dummies(stdata['Areas of interest'],dtype = int, drop_first=True)

    stdata = pd.concat([stdata,yr],axis = 1)

    stdata.drop(['Cloud Computing ', 'IoT ','Python ', 'QMS/Testing ', 'Data Science ',
           'Machine Learning', 'Blockchain ', 'RPA ', 'DevOps ', 'Big Data ',
           'Web Development ', 'Cyber Security ', 'Mobility',
           'Information Security'],axis=1,inplace=True)


    def rating_function(x):
       if x > 8:
           return "yes"
       else:
           return "N"
    stdata["written skills > 8"] = stdata["Rate your written communication skills [1-10]"].apply(rating_function)
    stdata.head(10)
    def rating_functions(x):
       if x > 8:
           return "yes"
       else:
           return "No"
    stdata["verbal skills > 8"] = stdata["Rate your verbal communication skills [1-10]"].apply(rating_functions)
    stdata['werbel and written skills'] = np.where(stdata['written skills > 8'] ==  stdata['verbal skills > 8'], 'yes', 'no')


    dt = stdata[stdata["Digital Marketing "] == 1]
    
    y = dt["Digital Marketing "]
    
    plt.rc('text', usetex=False)
    fig = plt.figure(figsize=(13,5))
    chart = sns.countplot(x = y, hue ="werbel and written skills", data = stdata)
    chart.set_xticklabels([''])
    chart.set_title('Students apllied for digital marketing')
    chart.set_xlabel('Verbal and written skills greater than 8')
    plt.xticks(
        rotation=0,
        horizontalalignment='right',
        fontweight='light',
        fontsize='x-large'  
    )
    pdf.savefig(fig)
    #pdf.close()

    j = stdata.Label
    plt.rc('text', usetex=False)
    fig = plt.figure(figsize=(13,5))
    relation = sns.scatterplot(x = j, y="CGPA/ percentage", data = stdata)
    plt.title("relationship between the CGPA and the target variable")
    pdf.savefig(fig)
    #pdf.close()
    #j.head()

    plt.rc('text', usetex=False)
    fig = plt.figure(figsize=(13,11))
    relation = sns.scatterplot(x = "Areas of interest", y=j, data = stdata)
    plt.title("relationship between the Area of Interest and the target variable")
    plt.xticks(
        rotation=42,
        horizontalalignment='right',
        fontweight='light',
        fontsize='x-large'  
    )
    pdf.savefig(fig)
    #pdf.close()

    plt.rc('text', usetex=False)
    fig = plt.figure(figsize=(13,8))
    relation = sns.scatterplot(x = "Major/Area of Study", y=j, data = stdata)
    plt.title("relationship between the year of study, major, and the target variable")
    relation.set_xticklabels(['EE','E&TC','CSE'])
    plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='x-large'  
    )

    pdf.savefig(fig)
    
    