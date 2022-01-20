import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import scipy.stats

col_names = ['x','y']
# load dataset
food = pd.read_csv("Food-Truck-LineReg.csv", names=col_names)

print(food)
X=food['x'].values
Y=food['y'].values

n=np.size(X)
print(n)

m_x = np.mean(X)
m_y = np.mean(Y)
print('Mean of X:',m_x)
print('Mean of Y:', m_y)

Sx=st.stdev(X)
Sy=st.stdev(Y)
print('Std dev of X',Sx)
print('Std dev of Y',Sy)

r=scipy.stats.pearsonr(X,Y)[0]
print("Correlation Coefficient r:",r)

m = r*(Sy/Sx)
print('Slope:',m)

#intercept
c = m_y - (m*m_x)
print('Intercept:',c)

y_pred = (m*X)+c

plt.scatter(X, Y, color = "m", marker = "o", s = 30)
 
# plotting the regression line
plt.plot(X, y_pred, color = "g")
 
# putting labels
plt.xlabel('x')
plt.ylabel('y')
 
# function to show plot
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st

col_names = ['x','y']
# load dataset
food = pd.read_csv("Food-Truck-LineReg.csv", names=col_names)

print(food)

X=food['x'].values
Y=food['y'].values
n=np.size(X)
print(n)

m_x = np.mean(X)
m_y = np.mean(Y)
print('Mean of X:',m_x)
print('Mean of Y:', m_y)

Sx=st.stdev(X)
Sy=st.stdev(Y)
print('Std dev of X',Sx)
print('Std dev of Y',Sy)

import scipy.stats
r=scipy.stats.pearsonr(X,Y)[0]
print("Correlation Coefficient r:",r)

m = r*(Sy/Sx)
print('Slope:',m)

plt.scatter(X, Y, color = "m",
               marker = "o", s = 30)

#intercept
c = m_y - (m*m_x)
print('Intercept:',c)

y_pred = (m*X)+c
y_pred


plt.scatter(X, Y, color = "m", marker = "o", s = 30)
 
# plotting the regression line
plt.plot(X, y_pred, color = "g")
 
# putting labels
plt.xlabel('x')
plt.ylabel('y')
 
# function to show plot
plt.show()

#cost(error) is y - y_pred

cost = Y - y_pred
cost

#SSE
sub=(Y-y_pred)**2
sse=sum(sub)
print('SSE:',sse)
SSE: 868.5324469391842

#SSR
sub1=(y_pred-m_y)**2
ssr=sum(sub1)
print('SSR:',ssr)
SSR: 2046.3146047180403

#SST
sub2=(Y-m_y)**2
sst=sum(sub2)
print('SST:',sst)
SST: 2914.8470516572247

#R2
R_2=ssr/sst
print('R2:',R_2)
R2: 0.7020315537841398
