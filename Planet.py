# Author: Guillaume Garde


import numpy as np
import sympy as sp

class Planet(mass, radius, position, color, name):
    
    G = 6.67430e-11 # m^3 kg^-1 s^-2 - adviced value of the Gravitational constant given by CODATA
    Planets = []

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
        self.Planets.append(self)

    def __str__(self):
        return self.name + " :\n"
        + "Mass : " + str(self.m) + "\n"
        + "Radius : " + str(self.radius) + "\n"
        + "Position : " + str(self.pos) + "\n"
        + "Velocity : " + str(self.v) + "\n"
        + "Color : " + str(self.color) + "\n"

    def compute_single_force(self, other):
        dist = np.linalg.norm(self.cartesian - other.cartesian)
        Force = np.array([[-self.G * (self.m * other.m) / (dist**2)],
                          [0],
                          [0]]) 
        return Force
    
    def compute_single_force_symbolic(self, other):
        G, m1, m2, x1, x2, y1, y2, z1, z2, r1, r2, theta1, theta2, phi1, phi2 = sp.symbols(f'G m_{self.name} m_{other.name} x_{self.name} x_{other.name} y_{self.name} y_{other.name} z_{self.name} z_{other.name} r_{self.name} r_{other.name} theta_{self.name} theta_{other.name} phi_{self.name} phi_{other.name}')
        OM1 = sp.Matrix([r1, theta1, phi1])
        OM2 = sp.Matrix([r2, theta2, phi2])
        OM1_cartesian = sp.Matrix([x1, y1, z1])
        OM2_cartesian = sp.Matrix([x2, y2, z2]) 
        
        dist = sp.simplify((OM1_cartesian - OM2_cartesian).norm())

    