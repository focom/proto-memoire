import numpy as np
import matplotlib.pyplot as plt 
from scipy.integrate import trapz, simps

def make_gauss(N, sig, mu):
    return lambda x: (N/(sig * (2*np.pi)**.5) * np.e ** (-(x-mu)**2/(2 * sig**2)))


def main():
    ax = plt.figure().add_subplot(1,1,1)
    x = np.arange(-100, 100, 0.1)
    s = np.sqrt([100])
    m = [40]
    c = ['b']

    for sig, mu, color in zip(s, m, c): 
        gauss = make_gauss(1, sig, mu)(x)
        ax.plot(x, gauss, color, linewidth=2)

    plt.xlim(-100, 100)
    plt.ylim(0, 1)
    plt.legend(['0.2', '1.0', '5.0', '0.5'], loc='best')
    

    xprime = np.arange(-1000, 43, 0.1)

    print(trapz( make_gauss(1, sig, mu)(xprime), xprime))
    plt.show()

if __name__ == '__main__':
   main()