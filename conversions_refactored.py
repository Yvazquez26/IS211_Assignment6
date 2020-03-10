#!/usr/bin/env python
# coding: utf-8

class ConversionNotPossible(Exception):
    """Message should be thrown if either a conversion unit is not found or if there are no units to convert
    """
    pass

def convert(src=str, dest=str, value=int):
    """A function to convert units of measurements."""
    srcUnit = src.lower()
    destUnit = dest.lower()

    unitDict = {
        'kelvin': {'fahrenheit': (float(value) * 9/5) - 459.67, 'celsius': float(value) - 273.15},
        'celsius': {'fahrenheit': float(value) * 9/5 + 32, 'kelvin': float(value) + 273.15},
        'fahrenheit': {'celsius': (float(value) - 32) * 5/9,
                       'kelvin': (float(value) + 459.67) * 5/9},
        'miles': {'yards': value * 1760, 'meters': value * 1609.344},
        'yards': {'miles': float(value) / 1760, 'meters': float(value) / 1.094},
        'meters': {'miles': float(value) / 1609.344, 'yards': float(value) * 1.094}
    }

    if srcUnit == destUnit:
        answer = float(value)
        return round(answer, 2)
    else:
        try:
            answer = unitDict[srcUnit][destUnit]
            return round(answer, 2)
        except KeyError:
            raise ConversionNotPossible
