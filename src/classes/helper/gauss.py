import numpy as np
# import matplotlib.pyplot as plt
from scipy.integrate import trapz, simps


def make_gauss(N, sig, mu):
    return lambda x: (N/(sig * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sig**2)))


def getScore(history, array):
    print('history: ',history)
    print('array: ',array)
    percentage = [0, 0.4, 0.6, 0.8, 1]
    importance = 1/len(array)
    totalScore = 0
    for score in array:
        temp = percentage[score] * importance
        totalScore += temp
    s80 = totalScore * 80 / 100
    s20 = percentage[history] * 20 / 100
    print('s80: '+str(s80))
    print('s20: '+str(s20))
    print('score du vecteur: '+ str(s80 + s20))
    return s80 + s20


def generateRepartition(score):
    x = np.arange(-100, 100, 0.1)
    sig = np.sqrt(100)
    sig=0.1
    mu = score  # Correspond a p(m) => esperance
    mu = 0.44

    x1 = np.arange(-1000, 0.4, 0.001)
    x2 = np.arange(0.4, 0.6, 0.001)
    x3 = np.arange(0.6, 0.8, 0.001)
    x4 = np.arange(0.8, 1000, 0.001)
    p1 = trapz(make_gauss(1, sig, mu)(x1), x1)
    p2 = trapz(make_gauss(1, sig, mu)(x2), x2)
    p3 = trapz(make_gauss(1, sig, mu)(x3), x3)
    p4 = trapz(make_gauss(1, sig, mu)(x4), x4)
    
    print('p(0) == 1 si le vecteur est nul sinon p(0) == 0')
    print('p(1): '+str(p1))
    print('p(2): '+str(p2))
    print('p(3): '+str(p3))
    print('p(4): '+str(p4))
    print('Somme des probabilite : '+ str(p1 + p2 + p3 + p4))


def printGaussian(m):
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(-100, 100, 0.1)
    s = np.sqrt(100)
    # m = [30] # Correspond a p(m) => esperance
    c = ['b']

 
    gauss = make_gauss(1, s, m)(x)
    ax.plot(x, gauss, c, linewidth=2)

    plt.xlim(-100, 100)
    plt.ylim(0, 1)
    plt.legend(['m='+str(m)+' s=sqrt(100)'], loc='best')
    plt.show()

def getGrade(score):
    if(score < 0.4):
        return 1
    if (0.4<= score and score < 0.6):
        return 2
    if (0.6<= score and score < 0.8):
        return 3
    if (0.8 <= score and score < 1):
        return 4
    else:
        return 0

def main():
    result = getScore(1, [2,1,0,3])
    print(result)
    # generateRepartition(result)
    # printGaussian(result)
if __name__ == '__main__':
    main()
