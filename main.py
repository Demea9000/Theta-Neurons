from Config import *


def get_chaos(plotting=True):
    M = 30000
    he = 1e-2

    time = np.linspace(0, M, M)/100


    thetas1 = np.array([0, 1, 6])
    thetas2 = np.array([1e-4, 1, 6])

    A = np.sin(euler(f,  eta=0.2, kappa=-0.75, h=he, y0=thetas1, N=M))[0]
    B = np.sin(euler(f, eta=0.2, kappa=-0.75, h=he, y0=thetas2, N=M))[0]
    print(thetas1)
    print(thetas2)
    plt.plot(time, A, linewidth=1)
    plt.plot(time, B, linewidth=1)
    plt.show()

if __name__ == '__main__':
    get_chaos()