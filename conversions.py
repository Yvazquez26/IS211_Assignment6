#!/usr/bin/env python
# coding: utf-8

import decimal

def convertCelsiusToKelvin(degrees):
    """A function to convert Celsius to Kelvin.
    
    Args:
        conversion(float): Celsius to Kelvin conversion.
    
    Returns:
        conversion(float): Returns Kelvin result
        
    """
    kelvin = float(celsius) + 273.15
    return round(kelvin, 2)


def convertCelsiusToFahrenheit(degrees):
    """A function to convert Celsius to Fahrenheit.
    
    Args:
        conversion(float): Celsius to Fahrenheit conversion.
    
    Returns:
        conversion(float): Returns Fahrenheit result.
        
    """
    farenheit = (float(celsius) * 1.8) +32
    return round(farenheight, 2)


def convertFahrenheitToCelsius(degrees):
    """a Function to convert Fahrenheit to Celsius.
    
    Args:
        conversion(float): Fahrenheit to Celsius conversion.
        
    Returns:
        conversion(float): Returns Celsius result.
        
    """
    celsius = (float(fahrenheit) -32) * 5 / 9
    return round(celsius, 2)


def convertFahrenheitToKelvin(degrees):
    """A function to convert Fahrenheit to Kelvin.
    
    Args:
        conversion(float): Fahrenheit to Kelvin conversion.
        
    Returns:
        conversion(float): Returns Kelvin result.
        
    """
    kelvin = (float(fahrenheit) + 459.67) * 5/9
    return round(kelvin, 2)


def convertKelvinToFahrenheit(degrees):
    """a Function to convert Kelvin to Fahrenheit.
    
    Args:
        conversion(float): Kelvin to Celsius conversion.
        
    Returns:
        conversion(float): Returns Celsius results.
        
    """
    fahrenheit = float(kelvin) * 9/5 - 459.67
    return round(fahrenheit, 2)

def convertKelvinToCelsius(degrees):
    """A function to convert Kelvin to Celsius.
    
    Args:
        conversion(float): Kelvin to Fahrenheit conversion.
        
    Returns:
        conversion(float): Returns Fahrenheit result.
        
    """
    celsius = kelvin - 273.15
    return round(celsius, 2)

