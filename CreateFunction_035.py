def convert(value: float, unit: str) -> str:
    formatted_unit = unit.upper()

    if formatted_unit == 'C':
        fahrenheit = (value * 9 / 5) + 32
        return f"{value}°C = {fahrenheit:.2f}°F"
    elif formatted_unit == 'F':
        celsius = (value - 32) * 5 / 9
        return f"{value}°F = {celsius:.2f}°C"
    else:
        return "Unit tidak valid! Gunakan 'C' untuk Celsius atau 'F' for Fahrenheit."
print(convert(100, 'C'))
print(convert(0, 'C'))
print(convert(98.6, 'F'))

import math

luaslingkaran= lambda r : 3.14 * r * r;
print ("Luas lingkaran dengan jari-jari 5: ", luaslingkaran(5))