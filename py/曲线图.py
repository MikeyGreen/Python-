import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(start=0,stop=40,endpoint=True) #start初始值，stop终值
y=np.e**x #e属于np模块里面的变量
plt.figure(figsize=(10,15)) #指定坐标轴的大小范围
plt.plot(x,y,color='green',linewidth=4) #线条的颜色，及宽度
plt.show() #展现

