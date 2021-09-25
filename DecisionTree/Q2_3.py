import numpy as np
import matplotlib.pyplot as plt
import os
from IG3 import *
from entropy import entropy
from majority_error import majority_error
from gini import gini
from helper import *
import matplotlib.pyplot as plt
from tabulate import tabulate

path = "bank"
os.chdir(path)

S_train,label_train = open_file('train.csv')
S_test,label_test = open_file('test.csv')


v_dict = {'age':numericalAttribute(S_train,S_test,S_train[:,0],0),
          'job':["admin.","unknown","unemployed","management","housemaid","entrepreneur","student",\
                 "blue-collar","self-employed","retired","technician","services"],
          'marital':["married","divorced","single"],
          'education':["unknown","secondary","primary","tertiary"],
          'default':["yes","no"],
          'balance':numericalAttribute(S_train,S_test,S_train[:,5],5),
          'housing':["yes","no"],
          'loan':["yes","no"],
          'contact':["unknown","telephone","cellular"],
          'day':numericalAttribute(S_train,S_test,S_train[:,9],9),
          'month':['dec','feb','sep','jun','mar','jul','may','aug','jan','oct','apr','nov'],
          'duration':numericalAttribute(S_train,S_test,S_train[:,11],11),
          'campaign':numericalAttribute(S_train,S_test,S_train[:,12],12),
          'pdays':numericalAttribute(S_train,S_test,S_train[:,13],13),
          'previous':numericalAttribute(S_train,S_test,S_train[:,14],14),
          'poutcome':["unknown","other","failure","success"]}

print("###### Q2.3 START ######")
print("### Q2.3 (a) START ###")
print('1. Entropy')
fn = entropy
errsTr1 = []
errsTe1 = []
data1 = []
for maxDepth in range(1,17):
    Tree1 = genTree(S_train,v_dict,label_train,maxDepth,fn)
    y_pred_train1 = predict(Tree1,S_train,label_train,v_dict)
    y_pred_test1 = predict(Tree1,S_test,label_test,v_dict)
    errsTr1.append(error(label_train,y_pred_train1))
    errsTe1.append(error(label_test,y_pred_test1))
    data1.append([maxDepth, errsTr1[-1],errsTe1[-1]])
    
print(tabulate(data1,headers=['Depth','Train','Test']))
plt.plot(errsTr1,label='Training')
plt.plot(errsTe1,label='Test')
plt.xlabel('Depth')
plt.ylabel('Error')
plt.legend()
plt.grid()
plt.show()

print('2. ME')
errsTr2 = []
errsTe2 = []
data2 = []
fn = majority_error
for maxDepth in range(1,17):
    Tree2 = genTree(S_train,v_dict,label_train,maxDepth,fn)
    y_pred_train2 = predict(Tree2,S_train,label_train,v_dict)
    y_pred_test2 = predict(Tree2,S_test,label_test,v_dict)
    errsTr2.append(error(label_train,y_pred_train2))
    errsTe2.append(error(label_test,y_pred_test2))
    data2.append([maxDepth, errsTr2[-1],errsTe2[-1]])
    
print(tabulate(data2,headers=['Depth','Train','Test'])) 
plt.plot(errsTr2,label='Training')
plt.plot(errsTe2,label='Test')
plt.xlabel('Depth')
plt.ylabel('Error')
plt.legend()
plt.grid()
plt.show()
print('3. GINI')
fn = gini
errsTr3 = []
errsTe3 = []
data3 = []
for maxDepth in range(1,17):
    Tree3 = genTree(S_train,v_dict,label_train,maxDepth,fn)
    y_pred_train3 = predict(Tree3,S_train,label_train,v_dict)
    y_pred_test3 = predict(Tree3,S_test,label_test,v_dict)
    errsTr3.append(error(label_train,y_pred_train3))
    errsTe3.append(error(label_test,y_pred_test3))
    data3.append([maxDepth, errsTr3[-1],errsTe3[-1]])
    
print(tabulate(data3,headers=['Depth','Train','Test']))
plt.plot(errsTr3,label='Training')
plt.plot(errsTe3,label='Test')
plt.xlabel('Depth')
plt.ylabel('Error')
plt.legend()
plt.grid()
plt.show()

print('4. Average prediction')
data1 = np.array(data1)
data2 = np.array(data2)
data3 = np.array(data3)

avg_data = []
en_avg = ['Entropy']+np.mean(data1[:,1:],axis=0).tolist()
avg_data.append(en_avg)
me_avg = ['ME']+np.mean(data2[:,1:],axis=0).tolist()
avg_data.append(me_avg)
gini_avg = ['GINI']+np.mean(data3[:,1:],axis=0).tolist()
avg_data.append(gini_avg)
print(tabulate(avg_data,headers=['Method','Train','Test']))

print("### Q2.3 (a) END ###")
print("### Q2.3 (b) START ###")
S_train_fix = missingData(S_train)
S_test_fix = missingData(S_test)
print('1. Entropy')
fn = entropy
errsTr1 = []
errsTe1 = []
data1 = []
for maxDepth in range(1,17):
    Tree1 = genTree(S_train_fix,v_dict,label_train,maxDepth,fn)
    y_pred_train1 = predict(Tree1,S_train_fix,label_train,v_dict)
    y_pred_test1 = predict(Tree1,S_test_fix,label_test,v_dict)
    errsTr1.append(error(label_train,y_pred_train1))
    errsTe1.append(error(label_test,y_pred_test1))
    data1.append([maxDepth, errsTr1[-1],errsTe1[-1]])
    
print(tabulate(data1,headers=['Depth','Train','Test']))
plt.plot(errsTr1,label='Training')
plt.plot(errsTe1,label='Test')
plt.xlabel('Depth')
plt.ylabel('Error')
plt.legend()
plt.grid()
plt.show()

print('2. ME')
errsTr2 = []
errsTe2 = []
data2 = []
fn = majority_error
for maxDepth in range(1,17):
    Tree2 = genTree(S_train_fix,v_dict,label_train,maxDepth,fn)
    y_pred_train2 = predict(Tree2,S_train_fix,label_train,v_dict)
    y_pred_test2 = predict(Tree2,S_test_fix,label_test,v_dict)
    errsTr2.append(error(label_train,y_pred_train2))
    errsTe2.append(error(label_test,y_pred_test2))
    data2.append([maxDepth, errsTr2[-1],errsTe2[-1]])
    
print(tabulate(data2,headers=['Depth','Train','Test'])) 
plt.plot(errsTr2,label='Training')
plt.plot(errsTe2,label='Test')
plt.xlabel('Depth')
plt.ylabel('Error')
plt.legend()
plt.grid()
plt.show()

print('3. GINI')
fn = gini
errsTr3 = []
errsTe3 = []
data3 = []
for maxDepth in range(1,17):
    Tree3 = genTree(S_train_fix,v_dict,label_train,maxDepth,fn)
    y_pred_train3 = predict(Tree3,S_train_fix,label_train,v_dict)
    y_pred_test3 = predict(Tree3,S_test_fix,label_test,v_dict)
    errsTr3.append(error(label_train,y_pred_train3))
    errsTe3.append(error(label_test,y_pred_test3))
    data3.append([maxDepth, errsTr3[-1],errsTe3[-1]])
    
print(tabulate(data3,headers=['Depth','Train','Test']))
plt.plot(errsTr3,label='Training')
plt.plot(errsTe3,label='Test')
plt.xlabel('Depth')
plt.ylabel('Error')
plt.legend()
plt.grid()
plt.show()
print('4. Average prediction')
data1 = np.array(data1)
data2 = np.array(data2)
data3 = np.array(data3)

avg_data = []
en_avg = ['Entropy']+np.mean(data1[:,1:],axis=0).tolist()
avg_data.append(en_avg)
me_avg = ['ME']+np.mean(data2[:,1:],axis=0).tolist()
avg_data.append(me_avg)
gini_avg = ['GINI']+np.mean(data3[:,1:],axis=0).tolist()
avg_data.append(gini_avg)
print(tabulate(avg_data,headers=['Method','Train','Test']))
print("### Q2.3 (b) END ###")
print("###### Q2.3 END ######")

