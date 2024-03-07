from gi.repository import Adw, Gio, Gtk
import math

class Equations():
    def __init__(self):
        self.equations = {
            "Coeficient A": self.coefA,
            "Coeficient B": self.coefB,
            "Logarithm": self.logarithm,
            "Natural Logarithm": self.natural_logarithm,
            "Sine": self.sine,
            "Cosine": self.cosine,
            "Tangent": self.tangent,
            "Inverse Sine": self.inverse_sine,
            "Inverse Cosine": self.inverse_cosine,
            "Inverse Tangent": self.inverse_tangent,
            "Hyperbolic Sine": self.hyperbolic_sine,
            "Hyperbolic Cosine": self.hyperbolic_cosine,
            "Hyperbolic Tangent": self.hyperbolic_tangent,
            "Inverse Hyperbolic Sine": self.inverse_hyperbolic_sine,
            "Inverse Hyperbolic Cosine": self.inverse_hyperbolic_cosine,
            "Inverse Hyperbolic Tangent": self.inverse_hyperbolic_tangent,
            "Factorial": self.factorial,
            "Absolute Value": self.absolute_value,
            "Percentage": self.percentage,
            "Degrees to Radians": self.degrees_to_radians,
            "Radians to Degrees": self.radians_to_degrees,
            "Gradians to Degrees": self.gradians_to_degrees,
            "Degrees to Gradians": self.degrees_to_gradians,
            "Radians to Gradians": self.radians_to_gradians,
            "Gradians to Radians": self.gradians_to_radians,
            "Binary to Decimal": self.binary_to_decimal,
            "Decimal to Binary": self.decimal_to_binary,
            "Octal to Decimal": self.octal_to_decimal,
            "Decimal to Octal": self.decimal_to_octal,
            "Hexadecimal to Decimal": self.hexadecimal_to_decimal,
            "Decimal to Hexadecimal": self.decimal_to_hexadecimal,
        }

    def coefA(str):
        if str == 'x²':
            return 1.0
        else:
            a = str.split('x')
            return float(a[0])
        
    def coefB(str):
        if str == 'x':
            return 1.0
        else:
            b = str.split('x')
            return float(b[0])
        
    def logarithm(str):
        return math.log(float(str))
    
    def natural_logarithm(str):
        return math.log1p(float(str))
    
    def sine(str):
        return math.sin(float(str))
    
    def cosine(str):
        return math.cos(float(str))
    
    def tangent(str):
        return math.tan(float(str))
    
    def inverse_sine(self, str):
        return math.asin(float(str))
            
    def inverse_cosine(self, str):
        return math.acos(float(str))
    
    def inverse_tangent(self, str):
        return math.atan(float(str))
    
    def hyperbolic_sine(self, str):
        return math.sinh(float(str))

    def hyperbolic_cosine(self, str):
        return math.cosh(float(str))
    
    def hyperbolic_tangent(self, str):
        return math.tanh(float(str))
    
    def inverse_hyperbolic_sine(self, str):
        return math.asinh(float(str))
    
    def inverse_hyperbolic_cosine(self, str):
        return math.acosh(float(str))
    
    def inverse_hyperbolic_tangent(self, str):
        return math.atanh(float(str))
    
    def factorial(self, str):
        return math.factorial(int(str))
    
    def absolute_value(self, str):
        return abs(float(str))
    
    def percentage(self, str):
        return float(str) / 100
    
    def degrees_to_radians(self, str):
        return math.radians(float(str))
    
    def radians_to_degrees(self, str):
        return math.degrees(float(str))
    
    def gradians_to_degrees(self, str):
        return float(str) * (180/200)
    
    def degrees_to_gradians(self, str):
        return float(str) * (200/180)
    
    def radians_to_gradians(self, str):
        return self.degrees_to_gradians(self.radians_to_degrees(str))
    
    def gradians_to_radians(self, str):
        return self.degrees_to_radians(self.gradians_to_degrees(str))
    
    def binary_to_decimal(self, str):
        return int(str, 2)
    
    def decimal_to_binary(self, str):
        return bin(int(str))
    
    def octal_to_decimal(self, str):
        return int(str, 8)
    
    def decimal_to_octal(self, str):
        return oct(int(str))
    
    def hexadecimal_to_decimal(self, str):
        return int(str, 16)
    
    def decimal_to_hexadecimal(self, str):
        return hex(int(str))
    