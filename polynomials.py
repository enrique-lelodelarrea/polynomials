#!/usr/bin/env python3

# polynomials.py - Implements a class for polynomials.

import numpy as np
import matplotlib.pyplot as plt
from itertools import zip_longest

class Polynomial:

    def __init__(self, *coefficients):
        ''' input: coefficient are in the form a_n, ..., a_1, a_0 '''
        self.coefficients = list(coefficients) # tuple is turned into a string

    def __repr__(self):
        '''
        method to return the canonical string representation
        of a polynomial
        '''
        return 'Polynomial' + str(tuple(self.coefficients))

    def __call__(self, x):
        res = 0
        for coeff in self.coefficients:
            res = res*x + coeff
        return res

    def degree(self):
        return len(self.coefficients) - 1

    def __add__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res[::-1])

    def __sub__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [t1 - t2 for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res[::-1])

    def derivative(self):
        derived_coeffs = []
        exponent = len(self.coefficients) - 1
        for i in range(len(self.coefficients) - 1):
            derived_coeffs.append(self.coefficients[i] * exponent)
            exponent -= 1
        return Polynomial(*derived_coeffs)

    def __str__(self):
        res = ""
        degree = self.degree()
        res += str(self.coefficients[0]) + "x^" + str(degree)
        for i in range(1, degree):
            coeff = self.coefficients[i]
            if coeff < 0:
                res += " - " + str(-coeff) + "x^" + str(degree - i)
            elif coeff > 0:
                res += " + " + str(coeff) + "x^" + str(degree - i)
            else:
                continue
        if self.coefficients[-1] < 0:
            res += " - " + str(-self.coefficients[-1])
        elif self.coefficients[-1] > 0:
            res += " + " + str(self.coefficients[-1])
        else:
            if degree == 0:
                res += '0'
        return res

###    

p = Polynomial(4, 0, -4, 3, 0)
print(p)
print('The degree of %s is %s' % (p, p.degree()))
X = np.linspace(-3, 3, 50, endpoint=True)
F = p(X)
#plt.plot(X, F)
#plt.show()

###

p1 = Polynomial(4, 0, -4, 3, 0)
p2 = Polynomial(-0.8, 2.3, 0.5, 1, 0.2)
p_sum = p1 + p2
p_diff = p1 - p2
X = np.linspace(-3, 3, 50, endpoint=True)
F1 = p1(X)
F2 = p2(X)
F_sum = p_sum(X)
F_diff = p_diff(X)
#plt.plot(X, F1, label="F1")
#plt.plot(X, F2, label="F2")
#plt.plot(X, F_sum, label="F_sum")
#plt.plot(X, F_diff, label="F_diff")
#plt.legend()
#plt.show()

###

p = Polynomial(-0.8, 2.3, 0.5, 1, 0.2)
p_der = p.derivative()
X = np.linspace(-2, 3, 50, endpoint=True)
F = p(X)
F_derivative = p_der(X)
plt.plot(X, F, label="F")
#plt.plot(X, F_derivative, label="F_der")
#plt.legend()
#plt.show()

###

p = Polynomial(1, 2, -3, 4, -55)
p2 = Polynomial(1, 2, 3)
p_der = p.derivative()
p3 = p + p2
print(p)
print(p_der)
print(p2)
print(p3)



print('Done.')
