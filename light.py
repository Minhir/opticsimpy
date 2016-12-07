from numpy import array, sqrt, sign
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from cmath import phase


class Light:
    """
    H == amplitude E_X
    K == amplitude E_y
    delta == phase difference phi_x - phi_y
    I = H**2 + K**2 = A**2
    Q = H**2 - K**2 = I * cos(2 * theta)
    U = 2 * H * K * cos(delta) = I * sin(2 * theta) ) cos(delta)
    V = 2 * H * K * cos(delta) = I * sin(2 * theta) ) sin(delta)
    """

    def __init__(self, I=1., Q=0., U=0., V=0.):
        self.I = sqrt(Q**2 + U**2 + V**2)
        self.Q = Q
        self.U = U
        self.V = V

    def __add__(self, other):
        if isinstance(other, Light):
            x1 = self.get_matrix()
            x2 = other.get_matrix()
            x = x1 + x2
            return Light(float(x[0]), float(x[1]), float(x[2]), float(x[3]))
        else:
            print('Not an instance of the class')
            return

    def __radd__(self, other):
        return self + other

    def __eq__(self, other):
        if isinstance(other, Light):
            return all((self.get_matrix() == other.get_matrix()))
        else:
            return False

    def get_matrix(self):
        return array([[self.I],
                      [self.Q],
                      [self.U],
                      [self.V]])

    def plot_ellipse(self):
        if self.Q**2 + self.U**2 + self.V**2 == 0:
            plt.plot([0], [0], 'ro')
            plt.show(block=False)
            return
        L = sqrt(self.Q ** 2 + self.U ** 2)
        Ip = sqrt(L ** 2 + self.V ** 2)
        A = sqrt(0.5 * (Ip + L))
        B = sqrt(0.5 * (Ip - L))
        size = 0.6 * max(A, B)
        theta = phase(complex(self.Q, self.U))
        h = sign(self.V)
        ellipse = Ellipse(xy=(0, 0), width=A, height=B, angle=theta * 180 / 3.1415, alpha=0.6, linewidth=5, edgecolor='green')
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect='equal')
        ax.set_title("Polarization ellipse")
        ax.set_ylim([-size, size])
        ax.set_xlim([-size, size])
        ax.axhline(0, color='black', alpha=1)
        ax.axvline(0, color='black', alpha=1)
        ax.add_patch(ellipse)
        ax.arrow(-0.3*size*h, 0.95*size, 0.6*size*h, 0, fc="k", ec="k", head_width=0.02, head_length=0.02)
        plt.show(block=True)


class LinearlyPolarizedHorizontal(Light):

    def __init__(self):
        self.I = 1
        self.Q = 1
        self.U = 0
        self.V = 0


class LinearlyPolarizedVertical(Light):

    def __init__(self):
        self.I = 1
        self.Q = -1
        self.U = 0
        self.V = 0


class LinearlyPolarizedP45(Light):

    def __init__(self):
        self.I = 1
        self.Q = 0
        self.U = 1
        self.V = 0


class LinearlyPolarizedM45(Light):

    def __init__(self):
        self.I = 1
        self.Q = 0
        self.U = -1
        self.V = 0


class CircularlyPolarizedRight(Light):

    def __init__(self):
        self.I = 1
        self.Q = 0
        self.U = 0
        self.V = 1


class CircularlyPolarizedLeft(Light):

    def __init__(self):
        self.I = 1
        self.Q = 0
        self.U = 0
        self.V = -1


class Unpolarized(Light):

    def __init__(self):
        self.I = 1
        self.Q = 0
        self.U = 0
        self.V = 0
