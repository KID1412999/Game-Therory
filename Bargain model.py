#《博弈论经典》-第二章-讨价还价模型分析
import numpy as np
import matplotlib.pyplot as plt
b=[[2,4],[2,2],[2,1],[2,2],[4,1]]#比尔的选择
k=[[10,1],[4,1],[6,2],[2,2]]#杰克的选择
u=[]
def conver(n):
	b=[]
	c=[]
	for i in range(2**n):
		b.append(bin(i))
	for i in b:
		t='0'*(n-len(i[2:]))+i[2:]
		c.append([int(j) for j in t])
	return c
def mute(arr,d):
	for i in arr:
		s+=i*d
	return()
for s1 in conver(5):
	for s2 in conver(4):
		t=1
		u.append([-sum(([a*b for a,b in zip(s1,[i[0] for i in b])]))+sum(([a*b for a,b in zip(s2,[i[0] for i in k])])),sum(([a*b for a,b in zip(s1,[i[1] for i in b])]))-sum(([a*b for a,b in zip(s2,[i[1] for i in k])])),s1,s2])
for i in u:
	print(i)

x=[]
y=[]
a=0
for i in u:
	if i[0]==i[1]:
		a=i[0]
	x.append(i[0])
	y.append(i[1])

plt.figure(figsize=(7,4)) 
# 绘制散点图
plt.scatter(x, y, marker = 'x',color = 'red', s = 40 ,label = 'First')
x_=np.linspace(1, 30, 100)

for i in range(40,80,2):#绘制无差异曲线
	y_=i/x_
	plt.plot(x_,y_,color="red",linewidth=1)
plt.xlabel("Time(s)") 
plt.ylabel("Volt") 
plt.title("PyPlot First Example") 
plt.legend(loc='best') 

# # 设置坐标轴范围
plt.xlim((-10, 30))
plt.ylim((-10, 30))
plt.show()
		
	

