import matplotlib.pyplot as plt
import numpy as np
# 1
e=np.zeros((1,10))
g=np.ones((1,10))
f=np.ones((1,10))*5
print(e)
print(g)
print(f)
# 2
array=np.arange(30,71)
print(array)
# 3
array=np.arange(30,71,2)
print(array)
# 4
x = np.eye(3)
print(x)
# 5
rand_num=np.random.normal(0,1)
print(rand_num)
# 6
a=np.arange(10,22).reshape((3,4))
for x in a:
    print(x)
# 7
x=np.arange(21)
print(x)
x[(x>=9)&(x<=15)]*=-1
print(x)

# 8
x=[1,8,3,5]
y=np.random.randint(0,11,4)
print("x*y:",x*y)
# 9
m= np.arange(10,22).reshape((3, 4))
print(m)
print(m.shape)
# 10
x = np.random.random((3, 3, 3))
print(x)
# 11
a=np.array([10,-1,2,5])
b=np.array([1,-6,0,10])
c=np.array([[1,8,2,5],[3,1,7,9]])
print("a-b: ",a-b)
print("a*b: ",a*b) 
print("a.dot(b): ",a.dot(b)) 
print("a*2: ",a*2) 
print("np.sin(a): ",np.sin(a)) 
print("a<3: ",a<3) 
print("a.sum(): ",a.sum()) 
print("a.sum(axis=0): ",a.sum(axis=0)) 
print("c.sum(): ",c.sum()) 
print("c.sum(axis=0): ",c.sum(axis=0)) 
print("a.min(): ",a.min()) 
print("a.max(): ",a.max()) 
print("a.mean(): ",a.mean()) 
print("a average(): ",np.average(a)) 
print("a median(): ",np.median(a)) 
print("a std(): ",np.std(a)) 
print("a var(): ",np.var(a)) 
print("c.cumsum(): ",c.cumsum()) 
print("a[1:2] :  ",a[1:2]) 
print("a[2:] :  ",a[2:]) 
print("c[-1] :  ",c[-1])
# 12
X = range(1, 50)
Y = [value * 3 for value in X]
print("Values of X:")
print(*range(1,50)) 
print("Values of Y (thrice of X):")
print(Y)
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
plt.show()
# 13
x1 = [10,20,30]
y1 = [20,40,10]
plt.plot(x1, y1, label = "line 1")
x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x2, y2, label = "line 2")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends ')
plt.legend()
plt.show()
# 14

t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
# 15
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()




























