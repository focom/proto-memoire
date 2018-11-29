import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz, simps


def make_gauss(N, sig, mu):
    return lambda x: (N/(sig * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sig**2)))


def getScore(history, array):
    percentage = [0, 40, 60, 80, 100]
    importance = 100/len(array)
    totalScore = 0
    for score in array:
        temp = percentage[score] * importance / 100
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
    mu = score  # Correspond a p(m) => esperance

    x1 = np.arange(-1000, 50, 0.1)
    x2 = np.arange(50, 70, 0.1)
    x3 = np.arange(70, 90, 0.1)
    x4 = np.arange(90, 1000, 0.1)
    p1 = trapz(make_gauss(1, sig, mu)(x1), x1)
    p2 = trapz(make_gauss(1, sig, mu)(x2), x2)
    p3 = trapz(make_gauss(1, sig, mu)(x3), x3)
    p4 = trapz(make_gauss(1, sig, mu)(x4), x4)
    print('p(0) == 1 si le veteur est nul sinon p(0) == 0')
    print('p(1): '+str(p1))
    print('p(2): '+str(p2))
    print('p(3): '+str(p3))
    print('p(4): '+str(p4))
    print('Somme des probabilité : '+ str(p1 + p2 + p3 + p4))


def main():
    result = getScore(2, [2, 2])
    generateRepartition(result)
    # print(result)

    # ax = plt.figure().add_subplot(1,1,1)
    # x = np.arange(-100, 100, 0.1)
    # s = np.sqrt([100])
    # m = [30] # Correspond a p(m) => esperance
    # c = ['b']

    # for sig, mu, color in zip(s, m, c):
    #     gauss = make_gauss(1, sig, mu)(x)
    #     ax.plot(x, gauss, color, linewidth=2)

    # plt.xlim(-100, 100)
    # plt.ylim(0, 1)
    # plt.legend(['0.2', '1.0', '5.0', '0.5'], loc='best')

    # x1 = np.arange(-1000, 40, 0.1)
    # x2 = np.arange(40, 60, 0.1)
    # x3 = np.arange(60, 80, 0.1)
    # x4 = np.arange(80, 1000, 0.1)

    # print('p(1): '+str(trapz( make_gauss(1, sig, mu)(x1), x1)))
    # print('p(2): '+str(trapz( make_gauss(1, sig, mu)(x2), x2)))
    # print('p(3): '+str(trapz( make_gauss(1, sig, mu)(x3), x3)))
    # print('p(4): '+str(trapz( make_gauss(1, sig, mu)(x4), x4)))

    # plt.show()
if __name__ == '__main__':
    main()
