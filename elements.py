from numpy import array, cos, sin, pi


class Element:
    """
    comment
    """

    def __init__(self,
                 M11=0, M12=0, M13=0, M14=0,
                 M21=0, M22=0, M23=0, M24=0,
                 M31=0, M32=0, M33=0, M34=0,
                 M41=0, M42=0, M43=0, M44=0,
                 theta = 0):
        self.M11 = M11
        self.M12 = M12
        self.M13 = M13
        self.M14 = M14
        self.M21 = M21
        self.M22 = M22
        self.M23 = M23
        self.M24 = M24
        self.M31 = M31
        self.M32 = M32
        self.M33 = M33
        self.M34 = M34
        self.M41 = M41
        self.M42 = M42
        self.M43 = M43
        self.M44 = M44
        self.theta = theta

    def get_matrix(self):
        return array([[self.M11, self.M12, self.M13, self.M14],
                      [self.M21, self.M22, self.M23, self.M24],
                      [self.M31, self.M32, self.M33, self.M34],
                      [self.M41, self.M42, self.M43, self.M44]])


class QuarterWavePlate(Element):

    def __init__(self, theta=0):
        theta = theta * pi / 180
        c2 = cos(2 * theta)
        s2 = sin(2 * theta)
        self.theta = theta
        self.M11 = 1
        self.M12 = 0
        self.M13 = 0
        self.M14 = 0
        self.M21 = 0
        self.M22 = c2 ** 2
        self.M23 = c2 * s2
        self.M24 = -s2
        self.M31 = 0
        self.M32 = c2 * s2
        self.M33 = s2 ** 2
        self.M34 = c2
        self.M41 = 0
        self.M42 = s2
        self.M43 = -c2
        self.M44 = 0


class HalfWavePlate(Element):

    def __init__(self, theta=0):
        theta = theta * pi / 180
        c4 = cos(4 * theta)
        s4 = sin(4 * theta)
        self.theta = theta
        self.M11 = 1
        self.M12 = 0
        self.M13 = 0
        self.M14 = 0
        self.M21 = 0
        self.M22 = c4
        self.M23 = s4
        self.M24 = 0
        self.M31 = 0
        self.M32 = s4
        self.M33 = -c4
        self.M34 = 0
        self.M41 = 0
        self.M42 = 0
        self.M43 = 0
        self.M44 = -1


class DeltaWavePlate(Element):

    def __init__(self, delta=0, theta=0):
        theta = theta * pi / 180
        delta = delta * pi / 180
        beta = cos(delta)
        mu = sin(delta)
        c2 = cos(2 * theta)
        s2 = sin(2 * theta)
        self.theta = theta
        self.delta = delta
        self.M11 = 1
        self.M12 = 0
        self.M13 = 0
        self.M14 = 0
        self.M21 = 0
        self.M22 = c2 ** 2 + beta * s2 ** 2
        self.M23 = c2 * s2 * (1 - beta)
        self.M24 = -mu * s2
        self.M31 = 0
        self.M32 = c2 * s2 * (1 - beta)
        self.M33 = s2 ** 2 + beta * c2 ** 2
        self.M34 = mu * c2
        self.M41 = 0
        self.M42 = mu * s2
        self.M43 = -mu * c2
        self.M44 = beta


class LinearPolarizer(Element):

    def __init__(self, theta=0):
        theta = theta * pi / 180
        c2 = cos(2 * theta)
        s2 = sin(2 * theta)
        self.theta = theta
        self.M11 = 0.5
        self.M12 = c2 * 0.5
        self.M13 = s2 * 0.5
        self.M14 = 0
        self.M21 = c2 * 0.5
        self.M22 = c2 ** 2 * 0.5
        self.M23 = c2 * s2 * 0.5
        self.M24 = 0
        self.M31 = s2 * 0.5
        self.M32 = c2 * s2 * 0.5
        self.M33 = s2 ** 2 * 0.5
        self.M34 = 0
        self.M41 = 0
        self.M42 = 0
        self.M43 = 0
        self.M44 = 0


class LinearPolarizerHorizontal(Element):

    def __init__(self):
        self.M11 = 0.5
        self.M12 = 0.5
        self.M13 = 0
        self.M14 = 0
        self.M21 = 0.5
        self.M22 = 0.5
        self.M23 = 0
        self.M24 = 0
        self.M31 = 0
        self.M32 = 0
        self.M33 = 0
        self.M34 = 0
        self.M41 = 0
        self.M42 = 0
        self.M43 = 0
        self.M44 = 0


class LinearPolarizerVertical(Element):

    def __init__(self):
        self.M11 = 0.5
        self.M12 = -0.5
        self.M13 = 0
        self.M14 = 0
        self.M21 = -0.5
        self.M22 = 0.5
        self.M23 = 0
        self.M24 = 0
        self.M31 = 0
        self.M32 = 0
        self.M33 = 0
        self.M34 = 0
        self.M41 = 0
        self.M42 = 0
        self.M43 = 0
        self.M44 = 0


class LinearRetarder(Element):

    def __init__(self, theta=0, delta=0):
        """
        :param theta: axis angle
        :param delta: phase delta
        """
        theta = theta * pi / 180
        delta = delta * pi / 180
        self.delta = delta
        self.theta = theta
        c2 = cos(2 * theta)
        s2 = sin(2 * theta)
        cd = cos(delta)
        sd = sin(delta)
        self.M11 = 1
        self.M12 = 0
        self.M13 = 0
        self.M14 = 0
        self.M21 = 0
        self.M22 = c2 ** 2 + cd * s2 ** 2
        self.M23 = c2 * s2 - c2 * cd * s2
        self.M24 = -s2 * sd
        self.M31 = 0
        self.M32 = c2 * s2 - c2 * cd * s2
        self.M33 = cd * c2 ** 2 + s2 ** 2
        self.M34 = c2 * sd
        self.M41 = 0
        self.M42 = s2 * sd
        self.M43 = -c2 * sd
        self.M44 = cd


