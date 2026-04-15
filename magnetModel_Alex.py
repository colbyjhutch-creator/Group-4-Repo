import numpy as np
import matplotlib.pyplot as plt
from matplot.animation import FuncAnimation

Temp = 500
size = 50

latt = np.random.choice([-0.5,0.5],size=(size,size))

print("origin lattice is \n", latt)

plt.imshow(latt)

def totalEnergy(latt):
    size=latt.shape[0]
    sum = 0
    for i in range(size):
        for j in range(size):
            if j < size -1:
                sum += latt[i][j] * latt[i][j+1]
        if i < size -1:
            sum += latt[i][j] * latt[i+1][j]
    return sum

print("total energy for original is",totalEnergy(latt))
    
def changeLatt(latt):
    latt2 = latt
    energy1= totalEnergy(latt)
    randomIndex1 = np.random.randint(0,latt.shape[0])
    randomIndex2 = np.random.randint(0,latt.shape[1])
    latt2[randomIndex1,randomIndex2] = -latt2[randomIndex1, randomIndex2]
    print("new lattice is \n",latt2)
    energy2=totalEnergy(latt)
    print("energy1",energy1,"energy2",energy2)
    if energy2 > energy1:
        return latt2
    else:
        a = np.random.random()*100
        prob = np.exp(-(energy2-energy1)/Temp)
        print("random number",a,"probability",prob)
        if prob < a:
            return latt2
        else:
            return latt1
        
plt.rcParams["animation.html"] = "jshtml"
plt.rcParams["figure.dpi"] = 60

def animate(latt):
    
plt.imshow(changeLatt(latt))