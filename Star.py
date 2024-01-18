# Author: Guillaume Garde


import numpy as np
import sympy as sp

class Star(mass, radius, position, color, name):

    G = 6.67430e-11 # m^3 kg^-1 s^-2 - adviced value of the Gravitational constant given by CODATA

    def __init__(self, mass, position, color):
        self.name = name
        self.m = mass
        self.radius = radius
        self.pos = position
        self.r, self.theta, self.phi = self.pos
        self.x = self.r*np.sin(self.theta)*np.cos(self.phi)
        self.y = self.r*np.sin(self.theta)*np.sin(self.phi)
        self.z = self.r*np.cos(self.theta)
        self.cartesian = np.array([[self.x, self.y, self.z]]).T
        self.v = np.zeros(3)
        self.color = color

    def __str__(self):
        return self.name + " :\n"
        + "Mass : " + str(self.m) + "\n"
        + "Radius : " + str(self.radius) + "\n"
        + "Position : " + str(self.pos) + "\n"
        + "Velocity : " + str(self.v) + "\n"
        + "Color : " + str(self.color) + "\n"

    
    